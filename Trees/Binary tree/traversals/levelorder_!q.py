def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)+1
        rheight = height(root.right)+1
        return max(lheight, rheight)


def levelorder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)


def printGivenLevel(root, h):
    if h == 1:
        print(root.data, end=' ')
    else:

        if root.left:
            printGivenLevel(root.left, h-1)
        if root.right:
            printGivenLevel(root.right, h-1)


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
