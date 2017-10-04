def inorder(root):
    s = []
    current = root
    while True:
        if current:
            s.append(current)
            current = current.left
        else:
            if len(s) > 0:
                current = s.pop()
                print(current.data)
                current = current.right
            else:
                return 0


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

    inorder(root)


