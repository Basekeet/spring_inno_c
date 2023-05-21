import sys
sys.setrecursionlimit(10000000)

n, m = map(int, input().split())

A = []

for i in range(n):
    t = list(map(int, input().split()))
    A.append(t)

dp = [[-1 for _ in range(m)] for _ in range(n)]

def check(i, j):
    return 0 <= i < n and 0 <= j < m

def f(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = 1
    if check(i + 1, j) and A[i][j] + 1 == A[i + 1][j]:
        dp[i][j] = max(dp[i][j], f(i + 1, j) + 1)
    if check(i - 1, j) and A[i][j] + 1 == A[i - 1][j]:
        dp[i][j] = max(dp[i][j], f(i - 1, j) + 1) 
    if check(i, j + 1) and A[i][j] + 1 == A[i][j + 1]:
        dp[i][j] = max(dp[i][j], f(i, j + 1) + 1)
    if check(i, j - 1) and A[i][j] + 1 == A[i][j - 1]:
        dp[i][j] = max(dp[i][j], f(i, j - 1) + 1)
    return dp[i][j]

ans = -1
for i in range(n):
    for j in range(m):
        ans = max(ans, f(i, j))
print(ans)
