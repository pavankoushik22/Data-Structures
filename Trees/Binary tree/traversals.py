class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.value = key

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end='')
        inorder(node.right)
    else:
        return 0
    return 0

def preorder(node):
    if node:
        print(node.value, end='')
        preorder(node.left)
        preorder(node.right)
    else:
        return 0
    return 0

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end='')
    else:
        return 0
    return 0

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print('------------inorder---------------')
inorder(root)
print('------------preorder--------------')
preorder(root)
print('------------postorder-------------')
postorder(root)
