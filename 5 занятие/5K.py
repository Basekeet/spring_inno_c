n = int(input())


used = {}
for i in range(1, n + 1):
    used[i] = False

s = ""

def f(k):
    global s
    if k == n:
        print(s)
        return
    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            s += str(i)
            f(k + 1)
            
            used[i] = False
            s = s[:-1]

f(0)
