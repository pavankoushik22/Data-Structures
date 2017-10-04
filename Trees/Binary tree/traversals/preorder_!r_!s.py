def morrispre(root):
    while root:
        if not root.left:
            print(root.data)
            root = root.right
        else:
            pre = root.left
            while (pre.right and pre.right != root):
                pre = pre.right
            if not pre:
                pre.right = root
            if pre.right == root:
                pre.right = None
                root = root.right

# this function is applicable only when the file is writable
