n = int(input())
res = 0
for i in range(n):
    t = list(map(int, input().split()))
    res += sum(t)
print(res // 2) 
