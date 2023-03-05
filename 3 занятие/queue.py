import collections

d = collections.deque()

d.append("asdfasd")
d.append("adsfdsfsd")
d.append("fdafs")

print(d)
print(d.popleft())
print(d.popleft())
print(d)
print(d.popleft())
