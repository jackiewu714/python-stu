import os
import shutil


# 移动文件
def move_file(olddir, destdir, fileName):
    src_file = olddir + "/" + fileName
    dest_file = destdir + "/" + fileName
    shutil.move(src_file, dest_file)
    print("success move ", src_file, " to ", dest_file)


#创建文件夹，并拷贝文件进去
def createdir_and_move_file(root_dir, filename):
    if os.path.isdir(root_dir + "/" + filename):
        print("createdir_and_move_file: ", filename, " is dir, continue")
        return

    portion = os.path.splitext(filename);
    if len(portion) == 2:
        filename_prefix = portion[0]
        last_idx = filename_prefix.rfind("-")
        sub_dirname = filename_prefix[0:last_idx]
        sub_dir = root_dir+"/" + sub_dirname
        print("filename_prefix=" + filename_prefix, ", last_idx=" + str(last_idx), ", sub_dirname=" + sub_dirname,
              ", sub_dir=" + sub_dir)

        if not os.path.exists(sub_dir) or not os.path.isdir(sub_dir):
            os.chdir(root_dir)
            os.mkdir(sub_dir)

        move_file(root_dir, sub_dir, filename)


# 将目录中的文件名中的空格替换成"-"，eg: 6.2.1 查询号源 类图.png  ->  6.2.1-查询号源-类图.png
rootDir = "E:/工作资料/CMMI4-资料/CMMI 4-文档编写分析/时序图-彭云飞"
files = os.listdir(rootDir)     #列出当前目录下所有的文件

for filename in files:
    print("filename=" + filename)

    if len(filename) > 0:
        try:
            if filename.index(" ") > 0:
                newfilename = filename.replace(" ", "-")    #替换掉文件名中的" "为"-"
                print("newfilename=" + newfilename)

                os.chdir(rootDir)                           #切换文件路径，如无路径则要新建或者路径同上，做好备份
                os.rename(filename, newfilename)            #执行重命名操作
        except ValueError:
            print(filename + " not contain space character")

    # 创建目录并移动文件
    createdir_and_move_file(rootDir, filename)



