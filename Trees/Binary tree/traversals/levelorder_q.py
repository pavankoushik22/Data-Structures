def levelorder(root):
    q = []
    if root is None:
        return 0
    q.append(root)
    while len(q) > 0:
        temp = q.pop(0)
        print(temp.data, end=' ')
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    levelorder(root)