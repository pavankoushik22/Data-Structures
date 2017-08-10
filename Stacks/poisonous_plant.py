n = int(input())
x = list(map(int, input().split(' ')))
stk = [0]*n
left = stk[0]
first = 0
for i in range(n):
    print(i)
    if first == 0:
        first += 1
    else:
        if x[i] > x[i-1]:
            stk[i] += 1

        else:
            h = x[i]
            temp = i-1
            day = 0
            while temp >= 0 and x[i] <= x[temp] and stk[temp] != 0:
                if day < stk[temp]:
                    day = stk[temp]
                temp = temp - 1
                h = x[temp]
            if x[i] > h:
                stk[i] += day+1



print(max(stk))