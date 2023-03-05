import collections
import sys
n = int(input())
a = collections.deque(map(int, input().split()))
b = collections.deque(map(int, input().split()))
c = 0
while a and b:
    if c == 200000:
        print("draw")
        sys.exit()
    x = a.popleft()
    y = b.popleft()
    if x == 0 and y == n - 1:
        a.append(x)
        a.append(y)
    elif x == n - 1 and y == 0:
        b.append(x)
        b.append(y)
    elif x < y:
        b.append(x)
        b.append(y)
    else:
        a.append(x)
        a.append(y)
    c += 1

if a:
    print("first", c)
else:
    print("second", c)
