
for t in zip(range(4), range(0, 10, 2), range(1, 10, 2)):
    print(t)

l1 = list(range(6))
l2 = list(reversed(range(6)))
print("l1:", l1)
print("l2:", l2)

x = []
for t in zip(range(-10, 0, 1), range(0, 10, 2), range(1, 10, 2)):
    x += t
print("x:", x)

x1 = sorted(x)
print("x1:", x1)

x2 = sorted(x, reverse=True)
print("x2:", x2)

x3 = sorted(x, key=abs)
print("x3:", x3)