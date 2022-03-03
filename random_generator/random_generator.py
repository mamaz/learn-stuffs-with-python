from random import choice

def get_random():
    id_length = 10
    numbers = "0123456789"
    nums = []
    append = nums.append

    for index in range(id_length):
        rand_number = choice(numbers)
        append(rand_number)

    return "".join(nums)


if __name__ == "__main__":
    print(get_random())
