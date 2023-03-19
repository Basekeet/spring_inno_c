import sys
sys.setrecursionlimit(10000000)

def gcd_slow(a, b):
    if a < b:
        a, b = b, a

    if a > 0 and b > 0:
        return gcd_slow(a - b, b)
    else:
        return a + b
    
def gcd(a, b):
    if a == 0 or b == 0:
        return a + b
    return gcd(b, a % b)
