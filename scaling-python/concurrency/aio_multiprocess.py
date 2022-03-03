from typing import Dict
from asyncio import run, gather
from aiomultiprocess import Pool
from aiohttp import request
from time import perf_counter

async def get(url: str) -> Dict:
    data = {
        "key": "value"
    }
    async with request(method="GET",url=url,json=data) as response:
        return await response.json(encoding='utf-8')

async def main():
    # default: number of process
    async with Pool(queuecount=2) as pool:
        while True:
            inpt = input('enter delay (1-3): ')
            print('Run..')
            kwds = {
                "url": f"https://httpbin.org/delay/{inpt}"
            }
            start = perf_counter()
            # run several fetch url concurrently on several child processes
            results = await gather(
                pool.apply(get, kwds=kwds),
                pool.apply(get, kwds=kwds),
                pool.apply(get, kwds=kwds),
                pool.apply(get, kwds=kwds),
                pool.apply(get, kwds=kwds),
                pool.apply(get, kwds=kwds),
                pool.apply(get, kwds=kwds),
                pool.apply(get, kwds=kwds),
            )
            end = perf_counter()

            for result in results:
                print(result.get('url'))

            print(f"elapsed time: {end-start}")



if __name__ == "__main__":
    run(main())
