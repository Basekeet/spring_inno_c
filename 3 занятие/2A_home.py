n = int(input())
arr = list(map(int, input().split()))
q = int(input())

arr.sort()
res = []
for i in range(q):
    a, b = map(int, input().split())

    l = -1
    r = n
    while r - l > 1:
        mid = (r + l) // 2

        if arr[mid] >= a:
            r = mid
        else:
            l = mid
    
    left = r

    l = -1
    r = n
    while r - l > 1:
        mid = (r + l) // 2

        if arr[mid] > b:
            r = mid
        else:
            l = mid
    rigth = r
    res.append(str(rigth - left))
print(" ".join(res))
