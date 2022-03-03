class CircularQueue:
    def __init__(self, size=0) -> None:

        # first element is set to None, queue will start at index 1 instead of 0
        self.size = size + 1

        self.front = 0
        self.rear = 0
        self.q = [None]

    def enqueue(self, value):
        if self.is_full():
            raise Exception("queue is full")
        else:
            self.rear = (self.rear + 1) % self.size
            self.q.insert(self.rear, value)

    def dequeue(self):
        if self.is_empty():
            raise Exception("queue is empty")
        else:
            self.front = (self.front + 1) % self.size
            val = self.q[self.front]
            self.q[self.front] = None
            return val

    def display(self):
        print([val for val in self.q if val is not None])
        print("front", self.front)
        print("rear", self.rear)

    def is_full(self):
        return ((self.rear + 1) % self.size) == self.front

    def is_empty(self):
        return self.front == self.rear


if __name__ == "__main__":
    cq = CircularQueue(size=3)

    print("enqueue")
    cq.enqueue(0)
    cq.enqueue(1)
    cq.enqueue(2)

    cq.display()

    print("dequeue")
    val = cq.dequeue()

    cq.display()

    print("enqueue")
    cq.enqueue(13)
    cq.display()

    cq.enqueue(12)
