hashh = {}


def levelorder(root, index=1):
    hashh[index] = root.data
    if root.left:
        levelorder(root.left, 2*index)
    if root.right:
        levelorder(root.right, 2*index + 1)


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

if __name__ == "__main__":
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.right = Node('e')

    levelorder(root)
    print(hashh)