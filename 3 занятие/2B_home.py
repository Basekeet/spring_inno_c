n, x, y = map(int, input().split())

def f(t):
    return (n - 1) <= (t // x + t // y)

l = -1
r = 2 * n * max(x, y)

while r - l > 1:
    t = (r + l) // 2
    if f(t):
        r = t
    else:
        l = t

print(min(x, y) + r)
