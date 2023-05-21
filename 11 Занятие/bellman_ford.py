n, m, x, t = map(int, input().split())

g = []

for i in range(m):
    a, b, w = map(int, input().split())
    g.append((a, b, w))
    g.append((b, a, w))

dist = [10**8 for _ in range(n + 1)]
dist[x] = 0

rev = [-1 for _ in range(n + 1)]

for _ in range(n - 1):
    for edge in g:
        a, b, w = edge
        if dist[b] > dist[a] + w:
            dist[b] = dist[a] + w
            rev[b] = a

print(dist[t])
result = [t]
while rev[t] != -1:
    t = rev[t]
    result.append(t)

print(*reversed(result))
