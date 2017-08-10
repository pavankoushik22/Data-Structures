
# stack implementation
class Stack:
    lis = []

    def __init__(self, l):
        self.lis = l[::-1]

    def push(self, data):
        self.lis.append(data)

    def peek(self):
        return self.lis[-1]

    def pop(self):
        self.lis.pop()

    def is_empty(self):
        return len(self.lis) == 0


# number of test cases
tests = int(input())
for i in range(tests):
    na, nb, x = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    temp = []
    stk_a = Stack(a)
    stk_b = Stack(b)
    score = 0
    count = 0
# first taking elements from stack A , till score becomes just less than desired total
    for j in range(len(a)):
        if score + stk_a.peek() <= x:
            score += stk_a.peek()

            count += 1
            temp.append(stk_a.peek())
            # storing the popped elements in temporary stack such that we can again remove them from score
            # when we find better element in stack B
            stk_a.pop()
# this is maximum number of moves using only stack A
    max_now = count
# now iterating through stack B for element lets say k which on adding to total score should be less than desired
    # or else we will remove each element of stack A from score till it becomes just less than desired total.
    for k in range(len(b)):
        score += stk_b.peek()
        stk_b.pop()
        count += 1
        while score > x and count > 0 and len(temp) > 0:
            count = count - 1
            score = score - temp[-1]
            temp.pop()
        # if the score after adding element from stack B is greater than max_now then we have new set of moves which will also lead
        # to just less than desired so we should pick maximum of both
        if score <= x and count > max_now:
            max_now = count
    print(max_now)
