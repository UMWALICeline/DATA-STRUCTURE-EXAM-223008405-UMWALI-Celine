
# Singly Linked List Implementation for Booking System

class SinglyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


# Example usage
linked_list = SinglyLinkedList()
linked_list.add("Booking1")
linked_list.add("Booking2")
print("Singly Linked List:", linked_list.display())
