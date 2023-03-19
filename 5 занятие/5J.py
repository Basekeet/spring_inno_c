n = int(input())

z = "abcdefghijklmnopqrstuvwxyz"

s = ""

def f(k):
    global s
    if k == n:
        if len(s) > 0:
            print(s)
        return
    s += z[k]
    f(k + 1)
    s = s[:-1]
    f(k + 1)

f(0)
