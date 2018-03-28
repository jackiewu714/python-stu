import sys
import math
import decimal

# 内置的 float
def equal_float(a, b):
    return abs(a-b) <= sys.float_info.epsilon

print("equal_float(3.14, 3.141): ", equal_float(3.14, 3.141))
print("equal_float(3.14, 3.14): ", equal_float(3.14, 3.141))

s = 14.25.hex()
f = float.fromhex(s)
t = f.hex()
print("s=", s, ", f=", f, ", t=", t)

x = math.pi * (5 ** 2)
y = math.hypot(5, 12)
z = math.modf(13.732)
print("x=", x, ", y=", y, ", z=", z)

# 复数

# 十进制数字, decimal模块可以提供固定的十进制数，计算比浮点数慢
a = decimal.Decimal(9876)
b = decimal.Decimal("54321.012345678987654321")
c = a + b
print("a=", a, ", b=", b, ", c=", c)

m = 23 / 1.05
print("m=", m)
print("23 / 1.05=", 23 / 1.05)

n = decimal.Decimal(23) / decimal.Decimal("1.05")
print("n=", n)
print("decimal.Decimal(23) / decimal.Decimal(\"1.05\")=", decimal.Decimal(23) / decimal.Decimal("1.05"))
