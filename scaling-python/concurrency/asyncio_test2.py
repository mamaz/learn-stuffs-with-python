import asyncio
import time

async def do_task(msg: str, delay_s: int):
    await asyncio.sleep(delay_s)
    return msg


if __name__ == "__main__":
    """
    Running 3 task concurrently, it will wait until all's finished

    Max time is the longest time
    """
    start = time.perf_counter()
    loop = asyncio.get_event_loop()
    future = asyncio.gather(
        do_task('one_s', 1),
        do_task('two_s', 2),
        do_task('three_s', 3)
    )
    results = loop.run_until_complete(future)
    end = time.perf_counter()
    print(results)
    loop.close()

    print(f"Elapsed time for concurrent: {end - start}")

    """
    Running 3 task serially

    Max time is task 1,2,3 elapsed time, combined
    """
    async def tasks():
        for coro in (do_task('one_s', 1),do_task('two_s', 2),do_task('three_s', 3)):
            print(await coro)

    start = time.perf_counter()
    asyncio.run(tasks())
    end = time.perf_counter()
    print(f"Elapsed time for serial: {end - start}")
