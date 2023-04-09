t = list(map(int, input().split()))

t.sort()

a, b, c, d = t

if a * d + b * c < a * c + b * d:
    print(a, c, b, d)
else:
    print(a, d, b, c)
