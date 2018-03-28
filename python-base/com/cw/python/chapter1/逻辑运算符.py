# 身份操作符 is
print("身份操作符")
a = ['aaa', 'bbb', 31]
b = ['aaa', 'bbb', 31]
print("a is b: ", a is b)

b = a
print("a is b: ", a is b)

a = "Something"
b = None
print("a is not None: ", a is not None, ", b is None: ", b is None);

# 比较操作符  >, >=, ==, !=, <=, <
print("比较操作符")
a = 2
b = 6
print("a==b: ", a == b)
print("a<b: ", a < b)
print("0<=a<=1: ", 0 <= a <= 1)
print("0<=a<=10: ", 0 <= a <= 10)

print("three" < "fourth")

a = "many paths"
b = "many paths"
print("a is b:", a is b, ", a==b:", a == b)

#成员操作符 in, not in
print("成员操作符")
p = (4, "frog", 9, -33, 9, 2)
print("2 in p: ", 2 in p)
print("\"dog\" not in p: ", "dog" not in p)

phrase = "Wild Swans by Jung Chang"
print("\"J\" in phrase: ", "J" in phrase);
print("\"han\" in phrase: ", "han" in phrase);

# 逻辑运算符 and, or, not
print("逻辑运算符")
five = 5;
two = 2;
zero = 0;
print(five and two)
print(two and five)

print(five or two)
print(two or five)

print(five and zero)

print(not (five and zero))
print(not (five and two))
