import json;

# 1. 处理字符串
# Python 字典类型转换为json
data = {
    "no" : 1,
    "name" : "jackie",
    "url" : "http://www.runoob.com"
};

jsonStr = json.dumps(data);
print("Python 原始数据：", repr(data));
print("JSON 对象：", jsonStr);

# 将json对象转换为pythohn字典
data2 = json.loads(jsonStr);
print("data2['name']=", data2['name']);
print("data2['url']=", data2['url']);

# 2. 处理文件
# 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。例如：
# 写入JSON数据
with open("data.json", "w") as f:
    json.dump(data, f);

# 读取数据
with open("data.json", "r") as f:
    jData = json.load(f);
    print("jData=", jData);
