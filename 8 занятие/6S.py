n = int(input())

X = list(map(int, input().split()))
X.sort()

X = [0] + X
dp = [0 for i in range(n + 1)]

dp[1] = 1000000000
dp[2] = X[2] - X[1]

for i in range(3, n + 1):
    dp[i] = min(dp[i - 1], dp[i - 2]) + (X[i] - X[i - 1])
print(dp[n])
