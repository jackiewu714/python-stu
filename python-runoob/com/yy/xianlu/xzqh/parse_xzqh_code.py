
xzqhDict = {}
file = open("data/2016年7月县以上行政区划代码.txt", encoding="utf8")
line = file.readline()
while line:
    line = line.split()
    # print(line)
    if len(line) == 2:
        # xzqhDict.append(line)
        xzqhDict[line[0]] = line[1]
    line = file.readline()
file.close()
print("xzqhDict:", xzqhDict)
print("xzqhDict[\"110106\"]:", xzqhDict["110106"])

#遍历 dict 写入文件的是无序的
fileWrite = open("data/2016年7月县以上行政区划代码-mod-dict.txt", "w", encoding="utf8")
for key, value in xzqhDict.items():
    lineStr = "{0}-{1}\n".format(key, value)
    fileWrite.write(lineStr)
fileWrite.close()

list1 = sorted(xzqhDict.items(), key=lambda xzqhDict: xzqhDict[0]) #安key排序生成新list
list2 = [(k, xzqhDict[k]) for k in sorted(xzqhDict.keys())] #使用 list内涵，按key升序生成列表
print("list1:", list1)

#遍历 list1 写入文件的是有序的
fileWrite = open("data/2016年7月县以上行政区划代码-mod-list.txt", "w", encoding="utf8")
for item in list1:
    lineStr = "{0}-{1}\n".format(item[0], item[1])
    fileWrite.write(lineStr)
fileWrite.close()