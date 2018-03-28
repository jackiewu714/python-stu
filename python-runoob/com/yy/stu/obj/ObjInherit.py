
class Parent:
    parentAttr = 100;

    def __init__(self):
        print("调用父类 Parent 构造函数");

    def parentMethod(self):
        print("调用父类 Parent 方法 parentMethod");

    def setAttr(self, attr):
        Parent.parentAttr = attr;

    def getAttr(self):
        print("父类属性, parentAttr：", Parent.parentAttr);

    def myMethod(self):
        print("调用 Parent->myMethod()");

class Child(Parent):
    def __init__(self):
        Parent.__init__(self);
        print("调用子类 Child 的构造方法");

    def childMethod(self):
        print("调用子类方法 childMethod");

    def myMethod(self):
        print("调用 Child->myMethod()");

class Parent2:

    def __init__(self):
        print("调用父类 Parent2 构造函数");

    def parentMethod(self):
        print("调用父类 Parent2 方法 parentMethod");

    def myMethod(self):
        print("调用 Parent2->myMethod()");

class Child2(Parent2, Child):
    def __init__(self):
        print("调用子类 Child2 的构造方法");

    # def myMethod(self):
    #     print("调用 Child2->myMethod()");

