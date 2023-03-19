import sys
n, m = map(int, input().split())
a = list(map(int, input().split()))

d = {}
tmp = 0
for el in a:
    d[el] = 2
    tmp += 2 * el

if tmp < n:
    print(-1)
    sys.exit(0)

ans = {
    0: 0
}

def f(n):
    MIN = 32
    for k in d:
        if d[k] > 0:
            if n - k < 0:
                continue
            d[k] -= 1
            t = f(n - k) + 1
            if t < MIN:
                MIN = t
                ans[n] = k
            MIN = min(t, MIN)
            d[k] += 1
    return MIN

print(f(n))
while ans[n] != 0:
    print(ans[n], end=" ")
    n = n - ans[n]
