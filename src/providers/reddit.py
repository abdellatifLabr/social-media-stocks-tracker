from datetime import datetime

from psaw import PushshiftAPI

PROVIDER_NAME = 'reddit'

# Provider contant variables
FILTER_FIELDS = ['url', 'author', 'title', 'subreddit']
DEFAULT_SUBREDDIT = 'wallstreetbets'


def add_args(parser):
    parser.add_argument(
        '-s',
        '--subreddit',
        type=str,
        default=DEFAULT_SUBREDDIT,
        help='Subreddit to fetch stocks data from'
    )


def run(last, subreddit, *args, **kwargs):
    api = PushshiftAPI()
    submissions = api.search_submissions(
        after=int((datetime.now() - last).timestamp()),
        subreddit=subreddit,
        filter=FILTER_FIELDS
    )

    for submission in submissions:
        yield {
            'provider': PROVIDER_NAME,
            'message': submission.title,
            'url': submission.url,
            'source': submission.subreddit,
            'created_at': datetime.fromtimestamp(submission.created_utc)
        }
