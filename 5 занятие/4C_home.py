n = int(input())
a = list(map(int, input().split()))
d = {}

for i, val in enumerate(a):
    if val in d:
        print(i - d[val], end=" ")
    else:
        print(-1, end=" ")
    
    d[val] = i
