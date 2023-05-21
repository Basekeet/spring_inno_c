n, m = map(int, input().split())

g = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False for i in range(n + 1)]
def dfs(v):
    visited[v] = True
    for el in g[v]:
        if not visited[el]:
            dfs(el)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)
