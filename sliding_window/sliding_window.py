def highest_sum_list(lst: list, n: int) -> int:
    """
    Returns highest sum for n consecutive numbers in a list

    Using sliding window technique that is an O(n) in time complexity

    Args:
        lst (list): list of ints
        n (int): n, consecutive nums

    Returns:
        highest sum for n consecutive numbers
    """
    initial = sum(lst[:n])
    max_num = initial

    i = 0
    while i+n < len(lst):
        max_num = max_num - lst[i] + lst[i+n]
        i += 1

    return max_num
