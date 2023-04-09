n = int(input())
a = [0] + list(map(int, input().split()))

pref = 0
min_pref = 0
min_ind = 0
res = -1
MAX_SUM = -10000000000

for i in range(1, n + 1):
    pref += a[i]

    if MAX_SUM < pref - min_pref:
        MAX_SUM = pref - min_pref
        res = (min_ind, i)

    if min_pref > pref:
        min_pref = pref
        min_ind = i
print(res[0] + 1, res[1], MAX_SUM)

