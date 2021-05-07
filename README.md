# social-media-stocks-tracker
Social media stocks tracker

# Install & Setup
```sh
$ git clone https://github.com/abdellatifLabr/social-media-stocks-tracker
$ cd social-media-stocks-tracker
$ pip install pipenv
$ pipenv shell --three
$ pipenv install
```
# Usage
```
$ python src/main.py --help
usage: main.py [-h] [-p {reddit}] [--days DAYS] [--hours HOURS] [--minutes MINUTES] [-s SUBREDDIT]

Track stocks on social media

optional arguments:
  -h, --help            show this help message and exit
  -p {reddit}, --provider {reddit}
                        Social media website to fetch stocks mentions from
  --days DAYS           Number of past days to fetch data from
  --hours HOURS         Number of past hours to fetch data from
  --minutes MINUTES     Number of past minutes to fetch data from
  -s SUBREDDIT, --subreddit SUBREDDIT
                        Subreddit to fetch stocks data from
```
## Example
Analyse posts on subreddir `r/wallstreetbets` from the last 2 hours
```
$ python src/main.py --provider reddit --subreddit wallstreetbets --hours 2
Fetching data...
$GME: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 78
$RKT: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 54
$MVI: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 52
$CLO: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 50
$AMC: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 37
$SOS: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 34
$mnm: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 32
$NOK: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 24
$PLT: ▇▇▇▇▇▇▇▇▇▇▇▇ 19
$VXR: ▇▇▇▇▇▇▇▇▇▇ 17
$NAK: ▇▇▇▇▇▇▇▇▇▇ 16
$prp: ▇▇▇▇▇▇▇ 12
$OCG: ▇▇▇▇▇▇▇ 12
$AHT: ▇▇▇▇▇▇▇ 11
$FAM: ▇▇▇▇▇▇ 10
$nue: ▇▇▇▇▇ 9
$CUM: ▇▇▇▇▇ 9
$RHE: ▇▇▇▇▇ 9
$WSB: ▇▇▇▇▇ 9
$PNN: ▇▇▇▇▇ 8
$TSL: ▇▇▇▇▇ 8
$Roo: ▇▇▇▇ 7
$TLR: ▇▇▇▇ 7
$DSC: ▇▇▇▇ 7
```
