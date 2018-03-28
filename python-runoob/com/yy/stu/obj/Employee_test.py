
from com.yy.stu.obj.Employee import Employee;

#1. 创建实例对象
#创建 Employee 类的第一个对象
emp1 = Employee("Zara", 2000);
#创建 Employee 类的第二个对象
emp2 = Employee("Manni", 5000);

#2. 访问属性
emp1.displayEmployee();
print("Total Employee %d" % Employee.empCount);

emp2.displayEmployee();
print("Total Employee %d" % Employee.empCount);

#3. 使用函数的方式来访问属性
#hasattr(obj,name) : 检查是否存在一个属性。
hRet = hasattr(emp1, "age");    # 如果存在 'age' 属性返回 True。
print("hRet=", hRet);

#setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
sRet = setattr(emp1, "age", 18);    # 添加属性 'age' 值为 8
print("sRet=", sRet);

#getattr(obj, name[, default]) : 访问对象的属性。
gRet = getattr(emp1, "age");    # 返回 'age' 属性的值
print("gRet=", gRet);

#delattr(obj, name) : 删除属性。
dRet = delattr(emp1, "age");    # 删除属性 'age'
print("dRet=", dRet);

#4. Python内置类属性
print("Employee.__doc__: ", Employee.__doc__);
print("Employee.__name__: ", Employee.__name__);
print("Employee.__module__: ", Employee.__module__);
print("Employee.__bases__: ", Employee.__bases__);
print("Employee.__dict__: ", Employee.__dict__);



