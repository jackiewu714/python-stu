import os
import shutil


# 查找根目录下指定名称的目录及其子目录下所有文件
def search_del_dir(rootdir, search_dir_name):
    if os.path.isdir(rootdir):
        dir_list = os.listdir(rootdir)
        for dir in dir_list:
            if dir == search_dir_name:
                path = os.path.join(rootdir, dir)
                print("deleting dir: " + path)
                shutil.rmtree(path)
            else:
                search_del_dir(os.path.join(rootdir, dir), search_dir_name)
    else:
        # print(rootdir + " is not a directory")
        return


# 删除target目录
search_del_dir("C:/work/code-hec-gitlab/TJH-CORE/bms-core", "target")
search_del_dir("C:/work/code-hec-gitlab/TJH-GWT2.8.2", "target")
search_del_dir("C:/work/code-hec-gitlab/ZJYYXM-OLD", "target")
search_del_dir("C:/work/code-hec-gitlab/ZJYYXM", "target")
search_del_dir("C:/work/code-hec-gitlab/ZJYYXM-CORE", "target")
search_del_dir("C:/work/code", "target")
search_del_dir("C:/work/code-hep-gitlab/hydrogen", "target")
