import socket;
import sys;

# 创建socke对象
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
# 获取本地主机名
host = socket.gethostname();
port = 9999;
print("host=%s, port=%d" % (host, port));

# 绑定端口
serverSocket.bind((host, port));

# 设置最大连接数，超过后排队
serverSocket.listen(5);

while True:
    clientSocket, addr = serverSocket.accept();
    print("clientSocket=", clientSocket);
    print("连接地址，addr=", str(addr));

    msg = "欢迎访问菜鸟教程！\r\n";
    clientSocket.send(msg.encode("utf-8"));
    clientSocket.close();




