def sum_nums(*numbers: list) -> int:
    return do_sum(numbers, 0)

def do_sum(numbers: list, total: int) -> int:
    if len(numbers) == 0:
        return total
    else:
        return do_sum(numbers[1:], numbers[0]+total)

if __name__ == "__main__":
    print(sum_nums(1,2,3,4,5,6))
