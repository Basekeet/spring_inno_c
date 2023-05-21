N, x = map(int, input().split())
x -= 1
g = []
for i in range(N):
    t = list(map(int, input().split()))
    g.append(t)

dist = [-1 for _ in range(N)]

dist[x] = 0

q = [x]

while len(q) > 0:
    t = q[0]
    q = q[1:]
    
    for i in range(N):
        if g[t][i] == 1 and dist[i] == -1:
            dist[i] = dist[t] + 1
            q.append(i)


print(*dist)
