
from operator import le
from typing import List

from typing import List

def bubble_sort(lst: list) -> List:
    for _ in range(0,len(lst)):
        for i in range(0,len(lst)):
            if (i < len(lst)-1):
                if (lst[i] > lst[i+1]):
                    lst[i],lst[i+1] = lst[i+1], lst[i]


if __name__ == "__main__":
    numbers = [312,323,7595,1,342894,346]
    bubble_sort(numbers)

    print(numbers)
