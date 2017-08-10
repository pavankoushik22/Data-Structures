class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):

        return self.items[-1]

tp = None
stk = Stack()
n = int(input())
x = list(map(int, input().split(' ')))

i = 0
maxi = 0
while (i < n):
    if stk.is_empty() or x[stk.peek()] <= x[i]:
        stk.push(i)
        i += 1

    else:
        tp = stk.peek()
        stk.pop()
        if stk.is_empty():
            temp = x[tp] * i
        else:
            temp = x[tp] * (i - stk.peek() - 1)
        if maxi < temp:
            maxi = temp
while not stk.is_empty():
    tp = stk.peek()
    stk.pop()
    if stk.is_empty():
        temp = x[tp] * i
    else:

        temp = x[tp] * (i - stk.peek() - 1)
    if maxi < temp:

        maxi = temp

print(maxi)