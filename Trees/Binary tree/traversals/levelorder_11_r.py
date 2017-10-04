def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left) + 1
        rheight = height(root.right) + 1
        return max(lheight, rheight)


def levelorder(root):
    h = height(root)
    if h == 0:
        return 0
    for i in range(1, h + 1):
        printlevel(root, i)
        print('')


def printlevel(root, i):
    if i == 1:
        print(root.data, end=' ')
    else:
        if root.left:
            printlevel(root.left, i - 1)
        if root.right:
            printlevel(root.right, i - 1)


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    levelorder(root)

