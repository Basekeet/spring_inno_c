n = int(input())
a = [0] + list(map(int, input().split()))

dp = [0 for i in range(110)]

dp[0] = 0
dp[1] = a[1]

for i in range(2, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2]) + a[i]
print(dp[n])
