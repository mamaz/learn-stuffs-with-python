"""
Demo of multiprocessing asyncio call to an API
"""
from concurrent.futures import ProcessPoolExecutor, wait
from multiprocessing import cpu_count
from api import call_api, do_call_api
from asyncio import run

def main():
    CPU_COUNT = cpu_count()

    NUM_OF_CALLS = 100
    URL = "https://httpbin.org/anything"

    futures = []

    with ProcessPoolExecutor() as executor:
        for i in range(NUM_OF_CALLS):
            print(f"call number {i}")
            future = executor.submit(
                do_call_api,
                url=URL
            )
            futures.append(future)

    print("waiting...")
    wait(futures)

    for f in futures:
        print(f.result())

if __name__ == "__main__":
    main()

