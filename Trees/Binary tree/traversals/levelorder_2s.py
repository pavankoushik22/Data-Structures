def levelorder(root):
    s1 = []
    s2 = []
    if root is None:
        return 0
    s1.append(root)
    while len(s1) > 0 or len(s2) > 0:
        while len(s1) > 0:
            temp = s1.pop()
            print(temp.data, end=' ')
            if temp.left:
                s2.append(temp.left)
            if temp.right:
                s2.append(temp.right)
        while len(s2) > 0:
            s1.append(s2.pop())


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

