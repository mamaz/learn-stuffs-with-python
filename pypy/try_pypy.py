"""
Testing a pypy3 to run simple but CPU intensive calculation

To run on pypy, install pypy3 then run:

>> pypy3 try_pypy.py

"""
import sys
from time import perf_counter

def count(n):
    total = 0
    for i in range(1, n):
        for j in range(1, n):
            total += (i+j)

    return total


if __name__ == "__main__":
    number = int(sys.argv[1]) or 100

    start = perf_counter()
    result = count(number)
    end = perf_counter()

    print(f"Result is {result}, elapsed time {(end - start) * 1000} ms")
