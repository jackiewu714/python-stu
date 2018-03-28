import random

gc = ["the", "a", "anthor"]
zt = ["cat", "dog", "man", "woman", "horse"]
dc = ["sang", "ran", "jumped"]
zy = ["loudly", "quietly", "well", "badly"]


def get_int():
    while True:
        inputStr = input("enter a number or Enter to finish: ")
        try:
            if inputStr:
                intVal = int(inputStr)
                if intVal <= 0:
                    print("must greater than 0")
                    continue
                return intVal
            else:
                break
        except ValueError as err:
            print(err)
            continue
        except EOFError as err:
            print(err)
            break


times = get_int();
if times is None:
    times = 5;
print("times: ", times)

i = 0
while i < times:
    gcIndex = random.randint(0, len(gc) - 1)
    ztIndex = random.randint(0, len(zt) - 1)
    dcIndex = random.randint(0, len(dc) - 1)
    zyIndex = random.randint(0, len(zy) - 1)

    content = gc[gcIndex] + " " + zt[ztIndex] + " " + dc[dcIndex] + " " + zy[zyIndex]
    print(content)
    i += 1
