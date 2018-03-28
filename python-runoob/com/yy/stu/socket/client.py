import socket;
import sys;

# 创建 socket 对象
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# 获取本地主机名
host = socket.gethostname();
port = 9999;
print("host=%s, port=%d" % (host, port));

# 连接服务，指定主机和端口
clientSocket.connect((host, port));

# 接收小于1024字节的数据
resp = clientSocket.recv(1024);

clientSocket.close();

print("server resp:%s" % resp.decode("utf-8"));