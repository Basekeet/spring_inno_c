import collections

d1 = collections.deque()
d2 = collections.deque()

n = int(input())
for i in range(n):
    a = input().split()
    if a[0] == "+":
        d2.append(int(a[1]))
    elif a[0] == "*":
        d2.appendleft(int(a[1]))
    else:
        print(d1.popleft())
    
    if len(d2) > len(d1):
        d1.append(d2.popleft())
