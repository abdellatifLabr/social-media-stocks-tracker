import argparse
from datetime import timedelta

from db.models import Mention, Stock
from db.session import db_session
from providers import get_prodvider, get_providers
from utils.extractors import extract_tickers

parser = argparse.ArgumentParser(description='Track stocks on social media')
parser.add_argument(
    '-p',
    '--provider',
    type=str,
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

for provider in get_providers():
    provider.add_args(parser)

args = parser.parse_args()

with db_session() as db:
    for submission in get_prodvider(args.provider, last=timedelta(days=args.days, hours=args.hours, minutes=args.minutes), **dict(args._get_kwargs())):
        tickers = extract_tickers(submission['message'])
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
