import collections

# 1. 命名的元组
Sale = collections.namedtuple("Sale", "productid customerid date quantity price")
sales = []
sales.append(Sale(432, 921, "2008-09-14", 3, 7.99))
sales.append(Sale(431, 874, "2009-09-15", 1, 18.49))

total = 0
for sale in sales:
	total += sale.quantity * sale.price
print("Total ${0:.2f}".format(total))

Aircraft = collections.namedtuple("Aircraft", "manufacturer model seating")
Seating = collections.namedtuple("Seating", "minimum maximum")
aircraft = Aircraft("Airbus", "A320-200", Seating(100, 220))
print("aircraft.seating.maximum: ", aircraft.seating.maximum)
print("{0} {1}".format(aircraft.manufacturer, aircraft.model))
print("{0.manufacturer} {0.model}".format(aircraft))
print("{manufacturer} {model}".format(**aircraft._asdict()))


# 2. 列表
# 1) 序列拆分操作符 *
first, *rest = [9, 2, -4, 8, 7]
print("first: ", first, ", rest: ", rest)

first, *mid, last = "Charles Philip Arthur George Windsor".split()
print("first: ", first, ", mid: ", mid, ", last: ", last)

*directories, executable = "/usr/local/bin/gvim".split("/")
print("directories: ", directories, ", executable: ", executable)

# 2) 带 * 号的参数
def product(a, b, c):
    return a * b * c; # here, * is the multiplication operator
mul = product(2, 3, 5)
print("mul1: ", mul)

L = [2, 3, 5]
mul = product(*L)
print("mul2: ", mul)

mul = product(2, *L[-2:])
print("mul3: ", mul)

# 3) 列表内涵
leaps = []
for year in range(1900, 1940):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leaps.append(year)
print("leaps: ", leaps)

leaps2 = [y for y in range(1900, 1940)
          if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)]
print("leaps2: ", leaps2)

codes = []
for sex in "MF": # Male, Female
    for size in "SMLX": # Small, Medium, Large, eXtra large
        if sex == "F" and size == "X":
            continue
        for color in "BGW": # Black, Gray, White
            codes.append(sex + size + color)
print("codes: ", codes);

codes2 = [s + z + c for s in "MF" for z in "SMLX" for c in "BGW"
          if not (s == "F" and z == "X")]
print("codes2: ", codes2)




