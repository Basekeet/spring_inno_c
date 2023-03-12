import collections

s = collections.deque()

n = int(input())

for i in range(n):
    t = list(map(int, input().split()))
    if t[0] == 1:
        s.append(t[1])
    elif t[0] == 2:
        print(s.pop())
