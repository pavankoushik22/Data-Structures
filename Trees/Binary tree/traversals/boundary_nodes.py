# for printing leaves


def printleaves(root):
    if not root.left and not root.right:
        print(root.data)
    else:
        if root.left:
            printleaves(root.left)
        if root.right:
            printleaves(root.right)


# for printing left line


def printleftline(root):
    if root:
        print(root.data)
        if root.left:
            root = root.left
            printleftline(root)
        elif root.right:
            root = root.right
            printleftline(root)

# for printing right line


def printrightline(root):
    if root:
        print(root.data)
        if root.right:
            root = root.right
            printrightline(root)
        elif root.left:
            root = root.left
            printrightline(root)


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)
    printleftline(root)
    printleaves(root)
    printrightline(root)


# need to remove the duplicate the values in the output
