class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def construct(inorder, preorder, instrt, inend):
    root = Node(preorder[instrt])
    rooti = inorder[instrt, inend].index(root)
    if rooti == 0:
        #no left sub tree

    for i in range(0,rooti):
