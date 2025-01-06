
# Circular Queue Implementation

class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            return False  # Queue is full
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        return True

    def dequeue(self):
        if self.front == -1:
            return None  # Queue is empty
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item

    def display(self):
        if self.front == -1:
            return []
        items = []
        i = self.front
        while True:
            items.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        return items


# Example usage
cq = CircularQueue(5)
cq.enqueue("Task1")
cq.enqueue("Task2")
print("Circular Queue:", cq.display())
