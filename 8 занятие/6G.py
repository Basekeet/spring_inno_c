n, m = map(int, input().split())
X = []
C = []

for i in range(n):
    t = int(input())
    X.append(t)

for i in range(m):
    t = int(input())
    C.append(t)
X.sort()

for i in range(m - 2, -1, -1):
    C[i] = min(C[i], C[i + 1])
X = [0] + X
C = [0] + C

dp = [1000000000000 for _ in range(n + 1)]

dp[0] = 0
dp[1] = C[1]

for i in range(2, n + 1):
    for j in range(i):
        dp[i] = min(dp[i], C[X[i] - X[i - j] + 1] + dp[i - 1 - j])

print(dp[n])
