n, m = map(int, input().split())
W = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dp_r = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j]
        dp_r[i][j] = 0

        if j - W[i] >= 0 and dp[i - 1][j - W[i]] + C[i] > dp[i][j]:
            dp[i][j] = dp[i - 1][j - W[i]] + C[i]
            dp_r[i][j] = 1
ans = []

while n != 0:
    if dp_r[n][m] == 1:
        ans.append(n)
        m -= W[n]
    n -= 1
ans.sort()
print(len(ans))
print(*ans)
