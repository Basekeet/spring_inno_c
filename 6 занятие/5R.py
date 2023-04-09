import sys
sys.setrecursionlimit(100000)
n = int(input())
a = list(map(int, input().split()))

def f(i):
    if i == n:
        return 
    f(i + 1)
    print(a[i], end=" ")
f(0)
