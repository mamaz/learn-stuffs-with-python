from asyncio import run, gather
from aiomultiprocess import Pool
from aiohttp import ClientSession
from time import perf_counter
from random import randint

async def call_api(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json(encoding='utf-8')

            return data

async def compute_async(range_num: int):
    return (sum([randint(1, 100) for _ in range(range_num)]))

def compute_sync(range_num: int):
    return (sum([randint(1, 100) for _ in range(range_num)]))

async def main():
    """
    Running paralelly using aiomultiprocess and sequentially
    have no difference on computing
    """

    print("Running several computation sequentially")
    start = perf_counter()
    result = [compute_sync(1000_000) for _ in range(12)]
    end = perf_counter()
    print(f"Result in synchronous {result}")
    print(f"Elapsed time_s {end - start}")


    async with Pool() as pool:
        start = perf_counter()
        results = await pool.map(compute_async, [1000_000 for _ in range(12)])
        end = perf_counter()

        print("\n\n")
        print("Running several computation paralelly")
        print(f"Results {results}")
        print(f"Elapsed time_s {end - start}")


if __name__ == "__main__":
    run(main())
