# author: long nguyen (nguyenhailong253@gmail.com)

import smtplib
import requests
import pandas as pd
from itertools import cycle
from contextlib import contextmanager
from datetime import datetime, timedelta
# from src.common import get_proxy, get_headers

class Scraper(object):
    ''' Parent class of all scrapers '''

    def __init__(self):
        self.NOW = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        proxies = self.load_proxies()
        headers = self.load_user_headers()
        self.proxy_pool = cycle(proxies)
        self.header_pool = cycle(headers)

    # +  -  -  - PROXIES & HEADERS -  -  - +

    def load_proxies(self):
        ''' Load proxies from csv file and return a set of proxies'''
        proxies = set()
        try:
            df = pd.read_csv("./src/csv/proxies.csv")
            for i, r in df.iterrows():
                proxy = ':'.join([r['IP Address'], str(r['Port'])[:-2]])
                proxies.add(proxy)
        except Exception as e:
            print(e)

        return proxies

    def load_user_headers(self):
        ''' Load headers from csv file and return a set of headers'''
        headers = set()
        df = pd.read_csv("./src/csv/user_agents.csv")
        for i, r in df.iterrows():
            headers.add(r['User agent'])
        return headers

    def get_proxies(self):
        ''' Get the next proxy in proxy pool'''
        proxy = next(self.proxy_pool)
        return {"http": proxy, "https": proxy}

    def get_headers(self):
        ''' Get the next header in header pool'''
        headers = next(self.header_pool)
        return {"User-Agent": headers}

    def reset_proxy_pool(self):
        ''' Download new proxies, save to csv and load csv'''
        get_proxy()
        proxies = self.load_proxies()
        self.proxy_pool = cycle(proxies)


if __name__ == '__main__':
    test_scraper = Scraper()
    print(test_scraper.load_user_headers())
    