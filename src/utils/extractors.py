import re


def extract_tickers(text, stock_symbol_length, *args, **kwargs):
    return re.findall('([$][A-Za-z]{' + stock_symbol_length + '})[\S]*', text)
