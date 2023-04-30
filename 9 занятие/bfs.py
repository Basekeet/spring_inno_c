n, m = map(int, input().split())

g = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

vis = [False for i in range(n + 1)]
dist = [0 for i in range(n + 1)]
q = [1]
dist[1] = 0

while len(q) > 0:
    t = q[0]
    q = q[1:]
    print(t)
    vis[t] = True
    for el in g[t]:
        if not vis[el]:
            dist[el] = dist[t] + 1
            q.append(el)
print(dist)

