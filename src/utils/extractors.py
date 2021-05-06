import re


def extract_tickers(text):
    return re.findall(r'([$][A-Za-z]{3})[\S]*', text)
