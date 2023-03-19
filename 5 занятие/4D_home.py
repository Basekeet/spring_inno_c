n = int(input())
a = list(map(int, input().split()))

k = len(set(a))

ans = n + 1

d = {}
r = 0
for l in range(n):
    while r < n and len(d) < k:
        d.setdefault(a[r], 0)
        d[a[r]] += 1
        r += 1
    
    if r == n and len(d) != k:
        break

    ans = min(ans, r - l)

    d[a[l]] -= 1
    if d[a[l]] == 0:
        del d[a[l]]
    l += 1

print(ans)
