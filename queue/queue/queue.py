class Queue:
    """
    Define queue with 2 pointers
    """

    def __init__(self, initial_size=0) -> None:
        self.size = initial_size
        self.front = -1
        self.rear = -1
        self.q = []

    def enqueue(self, number: int):
        if self.is_full():
            raise Exception("queue is full")
        else:
            self.rear += 1
            self.q.insert(self.rear, number)

    def dequeue(self):
        if self.is_empty():
            self.first = self.front = -1
            raise Exception("queue is empty")
        else:
            self.front += 1
            value = self.q[self.front]
            self.q[self.front] = None

            return value

    def is_full(self):
        return self.rear == (self.size - 1)

    def is_empty(self):
        return self.front == self.rear

    def display(self):
        print([num for num in self.q if num is not None])


if __name__ == "__main__":
    queue = Queue(5)
    print("size of queue", queue.size)

    queue.enqueue(1)
    queue.enqueue(2)

    queue.display()

    val = queue.dequeue()
    print("dequeue:", val)
    queue.display()

    val = queue.dequeue()

    print("dequeue", val)
    queue.display()
    queue.dequeue()
