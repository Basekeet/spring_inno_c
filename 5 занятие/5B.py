import sys
sys.setrecursionlimit(10000000)

d = {}
def A(m, n):
    if (m, n) in d:
        return d[m, n]
    if m == 0:
        t = n + 1
    elif m > 0 and n == 0:
        t = A(m - 1, 1)
    elif m > 0 and n > 0:
        t = A(m - 1, A(m, n - 1))
    d[m, n] = t
    return t
m, n = map(int, input().split())
print(A(m, n))
