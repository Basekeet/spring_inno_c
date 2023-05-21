n, m = map(int, input().split())

dist = []

for _ in range(n):
    a = list(map(int, input().split()))
    dist.append(a)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j],
                             dist[i][k] + dist[k][j])
for el in dist:
    print(*el)
