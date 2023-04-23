n = int(open("input.txt").read())

dp = [0 for _ in range(n + 1)]

dp[1] = 2
if n > 1:
    dp[2] = 4
if n > 2:
    dp[3] = 7

for i in range(4, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
f = open("output.txt", "w")

f.write(str(dp[n]))
f.close()
