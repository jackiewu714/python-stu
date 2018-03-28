import random

def get_int(msg):
    while True:
        try:
            i = int(input(msg))
            return i;
        except ValueError as err:
            print(err)

age = get_int("enter your age: ")

x = random.randint(1, 6)
y = random.choice(["iphone", "xiaomi", "huawei", "meizu", "zhongxing", "vivo", "oppo"])
print("x=", x, ", y=", y)
