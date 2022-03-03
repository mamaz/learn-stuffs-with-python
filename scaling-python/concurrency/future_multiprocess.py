from random import randint
from concurrent import futures
from time import perf_counter
from asyncio import run

def compute():
    return (sum([randint(1, 100) for _ in range(1000_000)]))

async def main():
    """
    Run compute parallely on different sub process
    """

    # this is blocking
    with futures.ProcessPoolExecutor() as executor:
        start = perf_counter()
        futs = [executor.submit(compute) for _ in range(12)]
        results = [f.result() for f in futs]
        end = perf_counter()

        print(f'Results: {results}')
        print(f"Elapsed time_s {end - start}")

if __name__ == "__main__":
    run(main())
