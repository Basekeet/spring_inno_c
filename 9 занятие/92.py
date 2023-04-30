n = int(input())
res = []

for i in range(n):
    tmp = [0 for _ in range(n)]
    a = list(map(int, input().split()))
    for el in a[1:]:
        tmp[el - 1] = 1
    res.append(tmp)

for i in range(n):
    print(*res[i])
