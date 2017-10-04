def morristraversal(root):
    current = root
    while current:
        if current.left:
            temp = current.left
            while (temp.right and temp.right !=current):
                temp = temp.right
            if not temp.right:
                temp.right = current
                current = current.left
            elif temp.right == current:
                print(current.data, end=' ')
                temp.right = None
                current = current.right

        else:
            print(current.data, end=' ')
            current = current.right


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

    morristraversal(root)
