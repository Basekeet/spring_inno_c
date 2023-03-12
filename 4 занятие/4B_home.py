d = {}
n = int(input())
for i in range(n):
    t = input().split()
    if t[0] == "1":
        d.setdefault(t[1], 0)
        d[t[1]] += int(t[2])
    elif t[0] == "2":
        if t[1] not in d:
            print("ERROR")
        else:
            print(d[t[1]])
 