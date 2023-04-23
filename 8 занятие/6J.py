n, m = map(int, input().split())
A = []
for i in range(n):
    t = list(map(int, input().split()))
    A.append(t)

dp = [[0 for _ in range(m)] for _ in range(n)]

ans = 0

for i in range(n):
    dp[i][0] = A[i][0]
    ans = max(ans, dp[i][0])
for j in range(m):
    dp[0][j] = A[0][j]
    ans = max(ans, dp[0][j])

for i in range(1, n):
    for j in range(1, m):
        if A[i][j] == 1:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            ans = max(ans, dp[i][j])
print(ans)

