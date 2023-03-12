import collections
d = collections.deque()
enter = 0
exit = 0
wait = [-1 for i in range(100001)]
n = int(input())
for i in range(n):
    t = list(map(int, input().split()))
    if t[0] == 1:
        d.append(t[1])
        wait[t[1]] = enter
        enter += 1
    elif t[0] == 2:
        d.popleft()
        exit += 1
    elif t[0] == 3:
        d.pop()
        enter -= 1
    elif t[0] == 4:
        print(wait[t[1]] - exit)
    elif t[0] == 5:
        print(d[0])
