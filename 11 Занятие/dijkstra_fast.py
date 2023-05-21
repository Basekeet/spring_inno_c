import heapq

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

pq = []
heapq.heappush(pq, (0, x))

while len(pq) > 0:
    tmp = heapq.heappop(pq)[1]
    if vis[tmp]:
        continue
    vis[tmp] = True

    for el in g[tmp]:
        if dist[el[0]] > dist[tmp] + el[1]:
            dist[el[0]] = dist[tmp] + el[1]
            heapq.heappush(pq, (-dist[el[0]], el[0]))

print(*dist)

