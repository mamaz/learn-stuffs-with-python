from concurrent import futures
import random
import urllib.request
from typing import Optional

def compute():
    return sum(
        [random.randint(1, 100) for i in range(1000000)])

def load_url(url: str, timeout: float):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

def run():
    with futures.ThreadPoolExecutor() as executor:
        futs = [executor.submit(compute) for _ in range(8)]
        results = [f.result() for f in futs]

        print("Results: %s" % results)

def fetch_urls():
    URLS = [
        'https://www.foxnews.com/',
        'https://www.cnn.com/',
        'https://www.bbc.co.uk/',
        'https://google.com',
    ]

    # this is blocking
    with futures.ThreadPoolExecutor() as executor:
        futs = {executor.submit(load_url, url, 10.0): url for url in URLS}
        try:
            results = [(f.result(), futs.get(f)) for f in futs.keys()]
        except Exception as exc:
            print(f'{exc}')
        else:
            for tup in results:
                print(f'URL: {tup[1]}, length: {len(tup[0])} bytes')


if __name__ == "__main__":
    fetch_urls() # slow as fuck average 4-6 seconds

