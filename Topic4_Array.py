
# Array Implementation for Fixed Orders

class OrderArray:
    def __init__(self, size):
        self.orders = [None] * size
        self.size = size
        self.index = 0

    def add_order(self, order):
        if self.index < self.size:
            self.orders[self.index] = order
            self.index += 1
            return True
        return False

    def display(self):
        return self.orders[:self.index]


# Example usage
order_array = OrderArray(5)
order_array.add_order("Order1")
order_array.add_order("Order2")
print("Order Array:", order_array.display())
