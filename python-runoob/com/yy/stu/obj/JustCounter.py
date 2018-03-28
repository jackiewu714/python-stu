
class JustCounter:
    __secretCount = 0;  #私有变量
    publicCount = 0;    #公开变量

    def __secretMethod(self):
        self.__secretCount += 1;
        self.publicCount += 1;
        print("调用私有方法 __secretMethod, __secretCount=", self.__secretCount);
        print("调用私有方法 __secretMethod, publicCount=", self.publicCount);

    def publicMethod(self):
        print("调用公有方法 publicMethod");
    
