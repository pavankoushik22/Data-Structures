def preorder(root):
    if not root:
        return 0
    stk = []
    stk.append(root)
    while len(stk) > 0:
        temp = stk.pop()
        print(temp.data)
        if temp.right:
            stk.append(temp.right)
        if temp.left:
            stk.append(temp.left)
