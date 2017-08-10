class Editor:
    lis = ''
    previous = []
    def append(self, data):
        self.lis += data
        temp = [1, len(data)]
        self.previous.append(temp)
    def delete(self, kk):
        k = 0-kk

        temp = [2, k, self.lis[kk-1:]]
        self.lis = self.lis[:k]
        self.previous.append(temp)
    def print(self, k):
        return self.lis[k-1]
    def undo(self):
        if self.previous[-1][0] == 1:
            added = 0- self.previous[-1][1]
            self.lis = self.lis[:added]
            self.previous.pop()
        else:
            print(self.previous)
            index = self.previous[-1][1]
            dat = self.previous[-1][2]
            print(dat)
            self.lis = self.lis + dat
    def peek(self):
        print(self.lis)

n = int(input())
file = Editor()
res = []
for i in range(n):
    xx = input().split(' ')
    if xx[0] == '1':
        file.append(xx[1])

    elif xx[0] == '2':
        file.delete(int(xx[1]))

    elif xx[0] == '3':
        res.append(file.print(int(xx[1])))
    else:
        file.undo()
for i in res:
    print(i)
