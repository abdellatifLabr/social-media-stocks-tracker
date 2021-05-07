import argparse
from datetime import timedelta

from termgraph.termgraph import AVAILABLE_COLORS, chart

from db.models import Mention, Stock
from db.session import db_session
from providers import get_prodvider, get_providers
from utils.extractors import extract_tickers

parser = argparse.ArgumentParser(description='Track stocks on social media')
parser.add_argument(
    '-p',
    '--provider',
    type=str,
    choices=[provider.PROVIDER_NAME for provider in get_providers()],
    help='Social media website to fetch stocks mentions from'
)
parser.add_argument(
    '--days',
    type=int,
    default=7,
    help='Number of past days to fetch data from'
)
parser.add_argument(
    '--hours',
    type=int,
    default=0,
    help='Number of past hours to fetch data from'
)
parser.add_argument(
    '--minutes',
    type=int,
    default=0,
    help='Number of past minutes to fetch data from'
)
parser.add_argument(
    '--stock-symbol-length',
    type=str,
    default='3,5',
    help='Stock symbol length range'
)

for provider in get_providers():
    provider.add_args(parser)

args = parser.parse_args()

termgraph_args = {
    "no_labels": False,
    "format": "{0}",
    "suffix": "",
    "stacked": False,
    "histogram": False,
    "width": 50,
    "different_scale": False,
    "no_values": False,
    "vertical": False,
}

colors = [
    AVAILABLE_COLORS.get("blue"),
]

MESSAGE = 'Fetching data...'

with db_session() as db:
    print(MESSAGE)
    for submission in get_prodvider(
            args.provider,
            last=timedelta(days=args.days, hours=args.hours,
                           minutes=args.minutes),
            **dict(args._get_kwargs())):
        tickers = extract_tickers(
            submission['message'], **dict(args._get_kwargs()))
        for ticker in tickers:
            stock = db.query(Stock).filter(
                Stock.symbol.like(f'%{ticker}')).first()
            if not stock:
                stock = Stock(symbol=ticker)
                db.add(stock)

            mention = Mention(
                stock_id=stock.id,
                provider=submission['provider'],
                message=submission['message'],
                url=submission['url'],
                source=submission['source'],
                created_at=submission['created_at'],
            )
            db.add(mention)

    result = db.execute(
        f"""
        SELECT stock.symbol, count(mention.stock_id) as num_of_mentions
        FROM stock
        LEFT JOIN mention ON (stock.id = mention.stock_id)
        GROUP BY stock.id
        ORDER BY num_of_mentions desc
        """
    )

    labels = []
    data = []
    for row in result:
        labels.append(row[0])
        data.append([row[1] if (row[1] > 0) else 1])

    if len(data) > 0 and len(labels) > 0:
        chart(colors, data, termgraph_args, labels)
