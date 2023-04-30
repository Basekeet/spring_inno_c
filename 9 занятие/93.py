n = int(input())
g = []
ans1 = []
ans2 = []
for i in range(n):
    t = list(map(int, input().split()))
    g.append(t)

    if sum(t) == 0:
        ans1.append(i + 1)

for i in range(n):
    s = 0
    for j in range(n):
        s += g[j][i]
    if s == 0:
        ans2.append(i + 1)

print(len(ans2), *ans2)
print(len(ans1), *ans1)
