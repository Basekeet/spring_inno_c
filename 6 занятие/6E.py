n = int(input())


dp_r = [0 + 1 for _ in range(10**6 + 10)]
dp = [10**6 + 1 for _ in range(10**6 + 10)]
dp[1] = 0


for i in range(2, n + 1):
    dp[i] = dp[i - 1]
    dp_r[i] = 1

    if i % 2 == 0 and dp[i] > dp[i // 2]:
        dp[i] = dp[i // 2]
        dp_r[i] = 2
    if i % 3 == 0 and dp[i] > dp[i // 3]:
        dp[i] = dp[i // 3]
        dp_r[i] = 3
    dp[i] += 1

print(dp[n])

result = []
while n > 1:
    result.append(n)
    if dp_r[n] == 1:
        n -= 1
    else:
        n //= dp_r[n]
result = result[::-1]
print(1, *result)
