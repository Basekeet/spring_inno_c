n = int(input())
A = [0] + list(map(int, input().split()))
m = int(input())
B = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dp_r = [[0 for _ in range(m + 1)] for _ in range(n + 1)] # 1 - диагональ, 2 - наверх, 3 - влево

dp[0][0] = 0

for i in range(n + 1):
    for j in range(m + 1):
        if i == 0:
            dp[i][j] = 0
            dp_r[i][j] = 3
        elif j == 0:
            dp[i][j] = 0
            dp_r[i][j] = 2
        elif A[i] == B[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            dp_r[i][j] = 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            dp[i][j] = dp[i - 1][j]
            dp_r[i][j] = 2
        else:
            dp[i][j] = dp[i][j - 1]
            dp_r[i][j] = 3

print(dp[n][m])

ans = []
while n != 0 and m != 0:
    if dp_r[n][m] == 1:
        ans.append(A[n])
        n -= 1
        m -= 1
    elif dp_r[n][m] == 2:
        n -= 1
    else:
        m -= 1

ans.reverse()
print(*ans)
