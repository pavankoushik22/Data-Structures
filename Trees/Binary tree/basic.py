# python program for basic binary tree implementation
# basic building block for binary tree


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# next one is typically god node

root = Node(1)
root.left = Node(2)
root.right = Node(3)

print(root.val)