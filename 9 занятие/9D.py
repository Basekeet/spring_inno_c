import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

col = [0 for i in range(n + 1)]
g = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)

IS_CIRCLE = False


circle = []

def dfs(v):
    global IS_CIRCLE, circle
    if IS_CIRCLE:
        return
    col[v] = 1
    circle.append(v)
    for el in g[v]:
        if col[el] == 1:
            IS_CIRCLE = True
            print("YES")
            ind = circle.index(el)
            print(circle[ind:])
            sys.exit(0)
            return
        elif col[el] == 0:
            dfs(el)
    col[v] = 2
    circle = circle[:-1]

for i in range(1, n + 1):
    if col[i] == 0:
        dfs(i)

print("NO")
