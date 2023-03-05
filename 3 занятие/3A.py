import collections

q = collections.deque()

n = int(input())

for i in range(n):
    a = list(input().split())
    if a[0] == "+":
        q.append(a[1])
    else:
        print(q.popleft())
