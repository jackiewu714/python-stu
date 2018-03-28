#if 语句
x = "aaa";
x = 1
x = 0
if x:
    print("x is nonzero")
else:
    print("x is none")

lines = 20000
if lines < 1000:
    print("small")
elif lines < 10000:
    print("medium")
else:
    print("large")

# while 循环
a = 1
while a < 10:
    print("a=", a)
    a += 1;

# for...in语句
countryList = ["Denmark", "Finland", "Norway", "Sweden"]
i = 0
for country in countryList:
    print("countryList[", i, "]: ", country);
    i += 1;

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if letter in "AEIOU":
        print(letter, "is a vowel")
    else:
        print(letter, "is a consonant")

# 基本的异常处理
s = input("enter an integer")
try:
    i = int(s)
    print("valid integer entered: ", i)
except ValueError as err:
    print(err)


