A = " " + input()
B = " " + input()

dp = [[0 for _ in range(len(B))] for _ in range(len(A))]


for i in range(len(A)):
    for j in range(len(B)):
        if i == 0 and j == 0:
            dp[i][j] = 0
        elif i == 0 and j != 0:
            dp[i][j] = j
        elif i != 0 and j == 0:
            dp[i][j] = i
        else:
            dp[i][j] = min(dp[i - 1][j] + 1,
                           dp[i][j - 1] + 1,
                           dp[i - 1][j - 1] + (0 if A[i] == B[j] else 1))
print(dp[len(A) - 1][len(B) - 1])

 