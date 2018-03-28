import os

# 字典初始化方式
d1 = dict({"id": 1948, "name": "Washer", "size": 3})
d2 = dict(id=1948, name="Washer", size=3)
d3 = dict([("id", 1948), ("name", "Washer"), ("size", 3)])
d4 = dict(zip(("id", "name", "size"), (1948, "Washer", 3)))
d5 = {"id": 1948, "name": "Washer", "size":3}
print(d1, d2, d3, d4, d5)

for item in d1.items():
    print("loop kv1:", item[0], item[1])

for key, value in d1.items():
    print("loop kv2:", key, value)

for key in d1.keys():
    print("loop key:", key)

for value in d1.values():
    print("loop value:", value)

# 字典内涵
file_sizes = {name: os.path.getsize(name) for name in os.listdir(".")}
print("file_sizes: ", file_sizes)

file_sizes2 = {name: os.path.getsize(name) for name in os.listdir(".")
               if os.path.isfile(name)}
print("file_size2: ", file_sizes2)

# 利用字典内涵创建反转的字典
inverted_d1 = {v: k for k, v in d1.items()}
print("inverted_d1: ", inverted_d1)

