n, k = map(int, input().split())

dp = [0 for i in range(50)]

dp[1] = 1

for i in range(2, n + 1):
    dp[i] = 0
    # for j in range(i - k, i):
    #     if j >= 1:
    #         dp[i] += dp[j]
    for j in range(max(i - k, 1), i):
        dp[i] += dp[j]
print(dp[n])
