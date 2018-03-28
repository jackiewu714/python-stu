
from com.yy.stu.obj.JustCounter import JustCounter;

counter = JustCounter();
counter.publicMethod();
print("publicCount=", counter.publicCount);

# counter.__secretMethod();   #报错，实例不能访问私有方法
#Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性，将如下代码替换上面一行代码：
counter._JustCounter__secretMethod();

# print("__secretCount=", counter.__secretCount);     #报错，实例不能访问私有变量
#Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性，将如下代码替换上面一行代码：
print("__secretCount=", counter._JustCounter__secretCount);