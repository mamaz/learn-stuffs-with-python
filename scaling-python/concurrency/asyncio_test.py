import aiohttp
import asyncio
import time

# more info:
# https://julien.danjou.info/python-and-fast-http-clients/
# https://realpython.com/async-io-python

"""
Superfast async fetch
"""

async def get(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json(encoding='utf-8')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    URLS = ['http://httpbin.org/anything' for i in range(100)]
    coroutines = [get(url) for url in URLS]

    start = time.perf_counter()
    results = loop.run_until_complete(asyncio.gather(*coroutines))
    end = time.perf_counter()

    lodict = [x for x in results]
    print(f'Results: {len(lodict)}')
    print(f"Elapsed: {end - start}")
    loop.close()
