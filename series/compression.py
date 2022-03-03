## a = [1,2,3,6,7,8,12,13]
def compress(lst: list) -> list:
    subresult = []
    counter = 0
    temp = []

    for i, val in enumerate(lst):
        if counter == 3:
            subresult.append(temp)
            counter = 0
            temp = []

        temp.append(val)
        counter += 1

        if i == len(lst) - 1 and counter < 3:
            subresult.append(temp)

    for val in subresult:
        if len(val) == 3:
            del val[1]

    return subresult


if __name__ == "__main__":
    print(compress([1, 2, 3, 6, 7, 8, 12]))
