s1 = set()
s2 = set()

for i in range(1, 9):
    s1.add(i)

for i in range(5, 12):
    s2.add(i)

print(s1, s2)
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s2 - s1)

for el in s1:
    print(el)

print(s1[2])

