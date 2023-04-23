n, k = map(int, input().split())
l = int(input())
a = list(map(int, input().split()))

dp = [0 for _ in range(n + 1)]

for el in a:
    dp[el] = -1

dp[1] = 1

for i in range(1, n + 1):
    if dp[i] == -1:
        dp[i] = 0
    else:
        for j in range(max(i - k, 1), i):
            dp[i] += dp[j]
print(dp[n])

