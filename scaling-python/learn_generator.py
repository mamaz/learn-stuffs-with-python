def ret_generator():
    """Function that return generator uses "yield"
    to return values.
    Difference with return is yield returns value lazily as the __next__
    function is executed

    Yields:
        [int]: returns int
    """
    for i in range(0, 10):
        yield i

if __name__ == "__main__":
    coro = ret_generator()

    for i in range(0,10):
        print(coro.__next__())
