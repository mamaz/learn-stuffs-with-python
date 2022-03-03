from typing import List
from random import randint


class Stack:
    def __init__(self, size_of_stack=0) -> None:
        self.size = size_of_stack
        self.top = -1  # last in the list
        self.the_stack: List[int] = []

    def is_empty(self) -> bool:
        return self.top == -1

    def is_full(self) -> bool:
        return self.top == self.size - 1

    def push(self, number: int):
        if not self.is_full():
            self.the_stack.append(number)
            self.top += 1
        else:
            raise Exception("Stackoverflow")

    def pop(self):
        if self.is_empty():
            raise Exception("Stack underflow")

        value = self.the_stack.pop()
        self.top -= 1
        return value

    def peek(self, position: int):
        if self.is_empty():
            return None

        index = self.top - position + 1
        return self.the_stack[index]

    def display(self):
        for index, num in enumerate(reversed(self.the_stack)):
            position = index + 1
            print(f"{position}: {num}")


if __name__ == "__main__":
    rand_nums = [randint(0, 100) for i in range(0, 5)]
    print(f"randoms: {rand_nums}")

    stack = Stack(5)

    for num in rand_nums:
        stack.push(num)

    stack.display()

    stack.pop()
    stack.pop()

    print("pop two")

    stack.display()

    print("push twice")

    stack.push(12)
    stack.push(13)

    stack.display()

    print("peek at pos 5")
    print(stack.peek(5))

    stack.display()
