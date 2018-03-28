import smtplib;
import sys;
from email.mime.text import MIMEText;
from email.header import Header;

# 使用第三方smtp服务
mail_host = "mail.yy.com";
mail_user = "yy-zbase@yy.com";
mail_pass = "bESi3P3d8yHudGgyoZ3o";

sender = "from@runoob.com";
sender = "yy-zbase@yy.com";
receivers = ["271321421@qq.com"];

message = MIMEText("Python 邮件发送测试。。。", "plain", "utf-8");
message['From'] = Header("菜鸟教程", "utf-8");
message['To'] = Header("测试", "utf-8");

subject = "Python SMTP 邮件测试";
message['Subject'] = Header(subject, "utf-8");

try:
    smtpObj = smtplib.SMTP();
    smtpObj.connect(mail_host, 25);
    smtpObj.login(mail_user, mail_pass);
    smtpObj.sendmail(sender, receivers, message.as_string());
    print("邮件发送成功");
except:
    print("邮件发送失败，原因：", sys.exc_info());