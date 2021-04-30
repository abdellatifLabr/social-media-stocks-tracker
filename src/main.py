from psaw import PushshiftAPI
import argparse
from datetime import datetime

from utils.extractors import extract_tickers
from db.session import db_session
from db.models import Stock, Mention


parser = argparse.ArgumentParser(description='Track stocks on social media')
parser.add_argument('-s', '--subreddit', type=str, help='Subreddit to fetch stocks mentions from')
args = parser.parse_args()

api = PushshiftAPI()

start_time = int(datetime(2021, 4, 26).timestamp())
submissions = api.search_submissions(
  after=start_time, 
  subreddit='wallstreetbets',
  filter=['url', 'author', 'title', 'subreddit']
)

with db_session() as db:
  for submission in submissions:
    tickers = extract_tickers(submission.title)
    for ticker in tickers:
        stock = db.query(Stock).filter(Stock.symbol.like(f'%{ticker}')).first()
        if not stock:
          stock = Stock(symbol=ticker)
          db.add(stock)

        mention = Mention(
          stock_id=stock.id,
          message=submission.title,
          url=submission.url,
          source=submission.subreddit,
          created_at=datetime.fromtimestamp(submission.created_utc),
        )
        db.add(mention)
