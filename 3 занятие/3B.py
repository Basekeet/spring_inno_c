import collections
s = collections.deque()

n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == 1:
        if s:
            s.append(min(s[-1], a[1]))
        else:
            s.append(a[1])
    elif a[0] == 2:
        s.pop()
    else:
        print(s[-1])

