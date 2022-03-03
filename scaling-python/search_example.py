from timeit import default_timer as timer
from typing import List

def search_with_tuple(haystack: List, needle: int) -> bool:
   return any((needle == item for item in haystack))

def search_with_list(haystack: List, needle: int) -> bool:
   return any([needle == item for item in haystack])


if __name__ == "__main__":
    start = timer()
    result = search_with_tuple([x for x in range(1,100)], 50)
    print(f'result: {result}')
    end = timer()

    print(f'Elapsed with tuple: {end - start}')

    start = timer()
    result = search_with_list([x for x in range(1,100)], 50)
    print(f'result: {result}')
    end = timer()

    print(f'Elapsed with list: {end - start}')
