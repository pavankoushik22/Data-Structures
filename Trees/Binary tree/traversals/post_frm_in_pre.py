def printleaves(root):
    if not root.left and not root.right:
        print(root.data, end=' ')
    else:
        if root.left:
            printleaves(root.left)
        if root.right:
            printleaves(root.right)


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

if __name__ == "__main__":
    root = Node(0)
    root.left = Node(1)
    root.right = Node(5)
    root.left.rightd = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(7)
    printleaves(root)