n, k = map(int, input().split())

v = list(map(int, input().split()))
t = list(map(int, input().split()))

for tmp in t:
    l = 0
    r = n

    while r - l > 1:
        mid = (r + l) // 2
        if v[mid] > tmp:
            r = mid
        else:
            l = mid
    if v[l] == tmp:
        print("YES")
    else:
        print("NO")

