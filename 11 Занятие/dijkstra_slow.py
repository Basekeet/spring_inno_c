n, m, x, t = map(int, input().split())

g = {}

for i in range(m):
    a, b, w = map(int, input().split())
    g.setdefault(a, [])
    g.setdefault(b, [])
    g[a].append((b, w))
    g[b].append((a, w))

dist = [10**8 for _ in range(n + 1)]
dist[x] = 0
vis = [False for _ in range(n + 1)]

while True:
    tmp = 0
    for i in range(1, n + 1):
        if not vis[i] and dist[tmp] > dist[i]:
            tmp = i
    if tmp == 0:
        break

    vis[tmp] = True

    for el in g[tmp]:
        dist[el[0]] = min(dist[el[0]], dist[tmp] + el[1])

print(*dist)

