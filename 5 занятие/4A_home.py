d = {}
n = int(input())

for i in range(n):
    t = input().split()
    if t[0] == "+":
        d[t[1]] = 1
    elif t[0] == "-":
        d[t[1]] = 0
    elif t[0] == "?":
        d.setdefault(t[1], 0)
        print(d[t[1]])
