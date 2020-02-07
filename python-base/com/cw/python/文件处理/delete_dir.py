import os
import shutil
import logging


# 查找根目录下指定名称的目录及其子目录下所有文件
def search_del_dir(rootdir, search_dir_name):
    if os.path.isdir(rootdir):
        dir_list = os.listdir(rootdir)
        for dir in dir_list:
            if dir == search_dir_name:
                path = os.path.join(rootdir, dir)
                print("deleting dir: " + path)
                try:
                    # 第二个参数忽略错误
                    shutil.rmtree(path, ignore_errors=True)
                    # os_del_file(path)
                except Exception as e:
                    print("ERROR：deleting dir: " + path + ", exception:" + repr(e))
                    logging.exception(e)
            else:
                search_del_dir(os.path.join(rootdir, dir), search_dir_name)
    else:
        # print(rootdir + " is not a directory")
        return

#使用 os 模块删除文件（最顶层目录未删删掉，待分析原因？）
def os_del_file(path):
    for fp in os.listdir(path):
        #取文件绝对路径
        path_file = os.path.join(path, fp)
        # print("path_file: {0}", path_file)
        # print("length: " + str(len(path_file)) + ", path_file: " + path_file)
        if len(path_file) > 260:
            print("file path over 260 character, length: " + str(len(path_file)) + ", path_file: " + path_file)
            continue

        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            os_del_file(path_file)



# 删除target目录
search_del_dir("C:/work/code-hec-gitlab/TJH", "target")
search_del_dir("C:/work/code-hec-gitlab/TJH-CORE", "target")
search_del_dir("C:/work/code-hec-gitlab/TJH-GWT2.8.2", "target")
search_del_dir("C:/work/code-hec-gitlab/ZJYYXM-OLD", "target")
search_del_dir("C:/work/code-hec-gitlab/ZJYYXM", "target")
search_del_dir("C:/work/code-hec-gitlab/ZJYYXM-CORE", "target")
search_del_dir("C:/work/code-hec-gitlab/LZSFY", "target")
search_del_dir("C:/work/code-hec-gitlab/TJXN", "target")
search_del_dir("C:/work/code-hec-gitlab/GSSFY", "target")
search_del_dir("C:/work/code-hec-gitlab/LYG", "target")
search_del_dir("C:/work/code", "target")
search_del_dir("C:/work/code-hep-gitlab/hydrogen", "target")

