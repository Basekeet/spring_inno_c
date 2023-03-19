n = int(input())
p = []
for i in range(n):
    a = tuple(map(int ,input().split()))
    p.append(a)
p.sort()

res = set()

prev = p[0]
for el in p[1:]:
    if prev[0] == el[0]:
        res.add(('y', el[1]))
    else:
        res.add(('x', el[0]))
    prev = el

print(len(res))
for el in res:
    print(el[0], el[1])
