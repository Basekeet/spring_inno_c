import heapq

a = []

n = int(input())

for i in range(n):
    t = list(map(int, input().split()))
    if t[0] == 0:
        heapq.heappush(a, -t[1])
    elif t[0] == 1:
        print(-heapq.heappop(a))
