import random
import threading
import urllib.request
from typing import List

"""
Spawning multiple worker threads
but it can not use threads from different CPU cores, because of GIL

Results:
>> time python thread_workers_multithreading.py
Results  [50495613, 50481759, 50480297, 50508250, 50496227, 50510490, 50438170, 50483940]
python thread_workers_multithreading.py  5.76s user 0.13s system 100% cpu 5.834 total
"""

compute_results = []

def compute():
    compute_results.append(sum([random.randint(1, 100) for _ in range(1000_000)]))

def load_url(url: str, timeout: float, result: List):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        result.append(conn.read())

def run_load_url():
    result = []
    URLS = [
            'https://www.foxnews.com/',
            'https://www.cnn.com/',
            'https://www.bbc.co.uk/',
            'https://google.com',
    ]

    workers = [threading.Thread(target=load_url, args=(url, 10, result)) for url in URLS]

    # starting
    for worker in workers:
        worker.start()

    # join makes workers result to be passed to main thread
    for worker in workers:
        worker.join()

    print('Results ', [len(res) for res in result])

if __name__ == "__main__":
    run_load_url() # kind of slow
