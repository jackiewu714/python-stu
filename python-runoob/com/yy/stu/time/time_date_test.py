import time;

# 1. 时间戳
ticks = time.time();
print("当前时间戳为：", ticks);

# 2. struct_time元组
localTime = time.localtime(ticks);
print("本地时间为：", localTime);

# 3. asctime()函数 和 ctime() 函数
# 最简单的获取可读的时间模式的函数是asctime()
localTime = time.asctime(time.localtime(time.time()));
print("本地时间为11：", localTime);

localTime = time.ctime(time.time());
print("本地时间为22：", localTime);

# 4. 格式化日期（使用 time 模块的 strftime 方法来格式化日期）
# 4.1 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()));

# 4.2 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()));

# 4.3 将格式字符串转换为时间戳
a = "Fri Feb 10 15:23:14 2017";
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")));
