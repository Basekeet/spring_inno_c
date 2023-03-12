s = []

a = input().split()

for el in a:
    if el == "+":
        a1 = s.pop()
        a2 = s.pop()
        s.append(a1 + a2)
    elif el == "-":
        a1 = s.pop()
        a2 = s.pop()
        s.append(a2 - a1)
    elif el == "*":
        a1 = s.pop()
        a2 = s.pop()
        s.append(a1 * a2)
    else:
        s.append(int(el))
print(s.pop())
