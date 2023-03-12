import collections

a = [collections.deque() for i in range(150001)]

n = int(input())
for i in range(n):
    t = input().split()

    if t[0] == "pushback":
        a[int(t[1])].append(int(t[2]))
    elif t[0] == "pushfront":
        a[int(t[1])].appendleft(int(t[2]))
    elif t[0] == "popback":
        print(a[int(t[1])].pop())
    elif t[0] == "popfront":
        print(a[int(t[1])].popleft())
