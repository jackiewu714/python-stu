
from com.yy.stu.obj.ObjInherit import Child, Child2;

c = Child();    #实例化子类
c.childMethod();    #调用子类的方法
c.parentMethod();   #调用父类的方法
c.setAttr(200);     #再次调用父类的方法
c.getAttr();        #再次调用父类的方法

c.myMethod();

# c2 = Child2();
# c2.myMethod();
