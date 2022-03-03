from typing import List


def is_subseries(first: List[int], second: List[int]) -> bool:
    """
    returns True if second is subseries of first

    Args:
        first (List[int]): source of subseries
        second (List[int]): series that will be checked against first series

    Returns:
        bool: True if second is subquery, False otherwise
    """
    counter = 0
    pivot = 0

    for s in range(0, len(second)):
        for i in range(pivot, len(first)):
            if first[i] == second[s]:
                counter += 1
                pivot = i
                break

    return counter == len(second)


if __name__ == "__main__":
    first = [1, 3, 5, 8, 9]
    checkers = [[3, 8, 9], [1, 5, 9], [1, 3, 5], [1], [1, 3, 18], [8, 5], [9, 8, 5]]

    for checker in checkers:
        print(is_subseries(first, checker))
