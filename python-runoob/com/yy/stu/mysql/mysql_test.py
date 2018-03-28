import pymysql;
import sys;
from com.yy.stu.mysql.DbConstant import DbConstant;

# 1. 数据库连接
# 打开数据库连接
db = pymysql.connect(host=DbConstant.host, port=DbConstant.port, user=DbConstant.user, passwd=DbConstant.passwd, db=DbConstant.db);
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor();
# 使用 execute() 方法执行sql查询
cursor.execute("select version()");
# 使用 fetchone() 方法获取单条数据
data = cursor.fetchone();
print("Database version is: %s" % data);
# 关闭数据库
db.close();

# 2. 创建数据库表
db = pymysql.connect(host=DbConstant.host, port=DbConstant.port, user=DbConstant.user, passwd=DbConstant.passwd, db=DbConstant.db);
# cursor = db.cursor();
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE");
# creSql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )""";
# cursor.execute(creSql);
db.close();

# 3. 数据库插入操作
db = pymysql.connect(host=DbConstant.host, port=DbConstant.port, user=DbConstant.user, passwd=DbConstant.passwd, db=DbConstant.db);
cursor = db.cursor();
iSql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)""";

try:
    #执行sql语句
    iRet = cursor.execute(iSql);
    #提交到数据库执行
    db.commit();
    print("iRet=", iRet);
except:
    #如果发生错误则回滚
    db.rollback();
    print("Error: unable to insert data, the reason:", sys.exc_info());  # 打印异常消息

db.close();

# 4. 数据库查询操作
db = pymysql.connect(host=DbConstant.host, port=DbConstant.port, user=DbConstant.user, passwd=DbConstant.passwd, db=DbConstant.db);
cursor = db.cursor();
qSql = "SELECT * FROM EMPLOYEE WHERE income > '%d'" % (1000);

try:
    #执行sql语句
    cursor.execute(qSql);
    #获取所有记录列表
    results = cursor.fetchall();
    for row in results:
        fname = row[0];
        lname = row[1];
        age = row[2];
        sex = row[3];
        income = row[4];
        print("fname=%s, lname=%s, age=%d, sex=%s, income=%d" % (fname, lname, age, sex, income));
except:
    print("Error: unable to fetch data, the reason:", sys.exc_info());  #打印异常消息
    raise;

db.close();

# 5. 数据库更新操作
db = pymysql.connect(host=DbConstant.host, port=DbConstant.port, user=DbConstant.user, passwd=DbConstant.passwd, db=DbConstant.db);
cursor = db.cursor();
uSql = "UPDATE EMPLOYEE SET AGE = AGE+1 WHERE SEX='%c'" % ('M');

try:
    # 执行sql语句
    uRet = cursor.execute(uSql);
    #提交到数据库执行
    db.commit();
    print("uRet=", uRet);
except:
    #发生错误时回滚
    db.rollback();
    print("Error: unable to update data, the reason:", sys.exc_info());  # 打印异常消息

db.close();

# 6. 删除操作
db = pymysql.connect(host=DbConstant.host, port=DbConstant.port, user=DbConstant.user, passwd=DbConstant.passwd, db=DbConstant.db);
cursor = db.cursor();
dSql = "DELETE FROM EMPLOYEE WHERE INCOME > %d" % (20);

try:
    #执行sql语句
    dRet = cursor.execute(dSql);
    #提交到数据库执行
    db.commit();
    print("dRet=%d" % dRet);
except:
    #发生错误时回滚
    db.rollback();
    print("Error: unable to delete data, the reason:", sys.exc_info());

db.close();

