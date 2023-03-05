w, h, n = map(int, input().split())

def f(l):
    return n <= (l // w) * (l // h)

l = -1
r = 2 * n * max(w, h)

while r - l > 1:
    t = (r + l) // 2
    if f(t):
        r = t
    else:
        l = t

print(r)
