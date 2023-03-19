def f(x):
    print(x)
    if x == 0:
        return 1

    t = f(x - 1) + 2
    return t

print(f(10))
