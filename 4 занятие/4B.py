import heapq

n = int(input())
a = list(map(int, input().split()))
heapq.heapify(a)

MAX = -1

while len(a) > 1:
    a1 = heapq.heappop(a)
    a2 = heapq.heappop(a)
    MAX = max(MAX, a2)
    if a1 == a2:
        heapq.heappush(a, a1 + a2)
    else:
        heapq.heappush(a, a2)

if len(a) == 1:
    MAX = max(a[0], MAX)

print(MAX)
