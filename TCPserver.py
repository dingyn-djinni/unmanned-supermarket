import socket

class sock():
    def __init__(self):
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "10.5.130.251"
        port = 20000
        # 绑定地址
        self.socket_server.bind((host, port))
        # 设置监听
        self.socket_server.listen(5)
        # socket_server.accept()返回一个元组, 元素1为客户端的socket对象, 元素2为客户端的地址(ip地址，端口号)
        self.client_socket, address = self.socket_server.accept()

    # 监听网络，返回通信的
    def listen(self):
        # while循环是为了让对话持续
        while True:
            # 接收客户端的请求
            recvmsg = self.client_socket.recv(1024)
            # 把接收到的数据进行解码
            strData = recvmsg.decode("utf-8")
            # 设置退出条件
            if strData == 'q':
                break
            print("接收: %s" % strData)
            return strData

    def send(self,msg):
        self.client_socket.send(msg.encode("utf-8"))

    def __del__(self):
        self.socket_server.close()
