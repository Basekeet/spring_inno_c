n, m = map(int, input().split())

NEG_INF = -100000000000

C = []

for i in range(n):
    row = list(map(int, input().split()))
    C.append(row)

dp = [[NEG_INF for _ in range(m)] for _ in range(n)]
dp_r = [["" for _ in range(m)] for _ in range(n)]

dp[0][0] = 0

for i in range(n):
    for j in range(m):
        if i != 0 and dp[i - 1][j] > dp[i][j]:
            dp[i][j] = dp[i - 1][j]
            dp_r[i][j] = "D"
        
        if j != 0 and dp[i][j - 1] > dp[i][j]:
            dp[i][j] = dp[i][j - 1]
            dp_r[i][j] = "R"

        dp[i][j] += C[i][j]
print(dp[n - 1][m - 1])

n = n - 1
m = m - 1
ans = ""
while dp_r[n][m] != "":
    ans = dp_r[n][m] + ans
    if dp_r[n][m] == "D":
        n -= 1
    else:
        m -= 1
print(ans)
