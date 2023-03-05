import random
a = [random.randint(0, 10000) for i in range(1000)]

print(a[100])

print(12 in a)

a.insert(500, 10)
print(a)

a[10000] = 129

a.pop(10)
a.remove(100)
