import math;

#1.全局变量，在函数中使用
money = 200;
def addMoney():
    #如果要给全局变量在一个函数里赋值，必须使用global语句
    global money;
    money = money + 1;
    return money;

print("before addMoney, money=", money);
addMoney();
print("after addMoney, money=", money);

#2.dir()函数
content = dir(math);
print("function dir(), content=", content);

#3.reload()函数，貌似python3没有该函数
#reload();
