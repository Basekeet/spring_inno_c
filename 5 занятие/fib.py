def fib_slow(n):
    if n == 1 or n == 2:
        return 1

    return fib_slow(n - 1) + fib_slow(n - 2)

ans = {
    1: 1,
    2: 1
}
def fib(n):
    if n in ans:
        return ans[n]

    t = fib(n - 1) + fib(n - 2)
    ans[n] = t
    return t
