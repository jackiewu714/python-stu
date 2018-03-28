
# 导入方式1(导入模块的所有内容)，调用函数不需要带前面的包名
#from com.yy.xianlu.module.support import *;
#add_func(1, 2);

# 导入方式2，调用函数需要带前面的包名
#import com.yy.xianlu.module.support;
#com.yy.xianlu.module.support.add_func(3, 4);

# 导入方式3(部分导入，指定导入的区块)，调用函数不需要带前面的包名
from com.yy.stu.module import add_func;
add_func(5, 6);
