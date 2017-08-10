class Stack:
    lis = []
    def push(self,data):
        self.lis.append(data)
    def pop(self):
        if len(self.lis) != 0:
            self.lis.pop()
    def is_empty(self):
        return len(self.lis) == 0

    def peek(self):
        return self.lis[-1]
    def dump(self):
        self.lis = []


left = ['(', '{', '[']
right = {')' : '(', '}' : '{', ']' : '['}

n = int(input())
stk = Stack()
for i in range(n):
    x = input()

    for j in range(len(x)):
        if x[j] in left:
            stk.push(x[j])
        elif not stk.is_empty() and right[x[j]] == stk.peek():
                stk.pop()
        else:
            pass

    if stk.is_empty():
        print('YES')
    else:
        print(stk.peek())
        print('NO')
    stk.dump()