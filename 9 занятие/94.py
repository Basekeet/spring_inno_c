n = int(input())

g = []
for i in range(n):
    t = list(map(int, input().split()))
    g.append(t)
input()
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(n):
        if g[i][j] == 1 and a[i] != a[j]:
            ans += 1
print(ans // 2)
