import os;      #操作系统接口
import glob;    #文件通配符
import sys;
import re;      #字符串正则匹配

# 1.操作系统接口
dir = os.getcwd();
print("dir=", dir);

os.chdir("D:/zbase.yy.com/keywords/");
print("dir=", os.getcwd());

# os.system("mkdir python");

# 2.文件通配符函数
files = glob.glob("*.*");
print("files=", files);

# 3.命令行参数
print("sys.argv=", sys.argv);
sys.stderr.write("Warning, log file not found starting a new one\n");

# 4.字符串正则匹配
fRet = re.findall(r"\bf[a-z]*", "which foot or hand fell fastest.")
print("fRet=", fRet);

sRet = re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat");
print("sRet=", sRet);


