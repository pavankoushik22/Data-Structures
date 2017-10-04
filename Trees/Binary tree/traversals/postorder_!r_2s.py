def postorder(root):
    if not root:
        return 0
    stk1 = []
    stk2 = []
    stk1.append(root)
    while len(stk1)>0:
        temp = stk1.pop()
        stk2.append(temp)
        if temp.right:
            stk1.append(temp.right)
        if temp.left:
            stk1.append(temp.left)

    while(len(stk2)>0):n
        print(stk2.pop(),end=' ')

