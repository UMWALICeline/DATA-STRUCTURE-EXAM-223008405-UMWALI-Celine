
# Stack and Circular Linked List Implementation for Booking System

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def display(self):
        return self.items


class CircularLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.last = None

    def add(self, data):
        new_node = self.Node(data)
        if not self.last:
            self.last = new_node
            self.last.next = self.last
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node

    def display(self):
        if not self.last:
            return []
        result = []
        current = self.last.next
        while True:
            result.append(current.data)
            current = current.next
            if current == self.last.next:
                break
        return result


# Example usage
stack = Stack()
stack.push("Booking1")
stack.push("Booking2")
print("Stack:", stack.display())

circular_list = CircularLinkedList()
circular_list.add("Booking1")
circular_list.add("Booking2")
print("Circular Linked List:", circular_list.display())
