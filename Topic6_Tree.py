
# Tree Implementation

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print(" " * level * 2 + str(self.data))
        for child in self.children:
            child.display(level + 1)


# Example usage
root = TreeNode("Services")
child1 = TreeNode("Cleaning")
child2 = TreeNode("Laundry")
root.add_child(child1)
root.add_child(child2)
child1.add_child(TreeNode("Kitchen"))
child1.add_child(TreeNode("Bathroom"))
root.display()
