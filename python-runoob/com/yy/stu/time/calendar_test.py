import calendar;

# 打印某月的月历
cal = calendar.month(2017, 2)
print("以下输出2017年2月份的日历：");
print(cal);

# calendar.firstweekday( )
# 返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一
firstwd = calendar.firstweekday();
print("firstwd=", firstwd);

# calendar.calendar(year,w=2,l=1,c=6)
# 返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
yearCal = calendar.calendar(2017, w=2, l=1, c=6);
print("以下输出2017年年历：");
print(yearCal);