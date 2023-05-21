import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

ans = []

col = [0 for i in range(n + 1)]
g = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)

IS_CIRCLE = False

def dfs(v):
    global IS_CIRCLE
    if IS_CIRCLE:
        return
    col[v] = 1

    for el in g[v]:
        if col[el] == 1:
            IS_CIRCLE = True
            return
        elif col[el] == 0:
            dfs(el)
    col[v] = 2
    ans.append(v)

for i in range(1, n + 1):
    if col[i] == 0:
        dfs(i)
ans.reverse()
if IS_CIRCLE:
    print(-1)
else:
    print(*ans)
