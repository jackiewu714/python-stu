import smtplib;
from email.mime.text import MIMEText;
from email.header import Header;
import sys;

# 需要本机启动SMTP服务
sender = "from@runoob.com";
receivers = ["271321421@qq.com"];

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText("Python 邮件发送测试。。。", "plain", "utf-8");
message['From'] = Header("菜鸟教程", "utf-8");
message['To'] = Header("测试", "utf-8");

subject = "Python SMTP 邮件测试";
message['Subject'] = Header(subject, "utf-8");

try:
    smtpObj = smtplib.SMTP("localhost");    #需启动本机的SMTP服务
    smtpObj.sendmail(sender, receivers, message.as_string());
    print("邮件发送成功");
except:
    print("邮件发送失败，原因：", sys.exc_info());