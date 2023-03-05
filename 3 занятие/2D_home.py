k, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
CONST = [2, 2, 2, 1, 1, 8]


def f(x):
    to_buy = 0
    for i in range(len(a)):
        to_buy += max(0, CONST[i] * x - a[i]) * k
    for i in range(len(b)):
        to_buy += max(0, CONST[i] * x - b[i]) * k

    return x * n - to_buy

l = -1
r = 10**18

while (r - l) > 1:
    mid = (r + l) // 2
    if (f(mid) < f(mid + 1)):
        l = mid
    else:
        r = mid

print(f(r))
