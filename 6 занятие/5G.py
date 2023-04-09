a, b = map(int, input().split())

def f(a, b):
    if a == b:
        return str(a)
    elif b % 2 != 0 or b < 2 * a:
        return "(" + f(a, b - 1) + " + 1)"
    else:
        return f(a, b // 2) + " * 2"

print(b, "=", f(a, b))
