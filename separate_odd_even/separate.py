from typing import List
from collections import deque
from collections import Counter


def separate_odd_even(nums: List) -> List:
    odds = []
    evens = []

    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    return odds + evens


def separate_odd_even_in_place(nums: List) -> List:
    for index in range(len(nums)):
        num = nums[index]

        if num % 2 == 0:
            nums.append(num)
            nums[index] = "a"

    c = Counter(nums)

    for _ in range(c["a"]):
        nums.remove("a")


if __name__ == "__main__":
    a = [0, 0, 1]
    separate_odd_even_in_place(a)
    print(a)
