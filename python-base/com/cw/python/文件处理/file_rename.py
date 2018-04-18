
import os

# 将目录中的文件名加上后缀".mp3"，eg: 李克勤 - 月半小夜曲  ->  李克勤 - 月半小夜曲.mp3

dir = "F:/个人资料/123"
files = os.listdir(dir)  #列出当前目录下所有的文件

for fileName in files:
    portion = os.path.splitext(fileName)    #分离文件名和后缀
    print("fileName=" + fileName + ", portion=" + str(portion))

    if portion[1] == "":                    #根据后缀来修改，如后缀为空则修改
        newName = portion[0] + ".mp3"       #新的文件名
        os.chdir(dir)                       #切换文件路径，如无路径则要新建或者路径同上，做好备份
        os.rename(fileName, newName)        #执行重命名操作
