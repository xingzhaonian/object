# === 客户端程序 server.py ===

# 导入 socket模块
import socket
import time 

# 管理客户端连接和相关功能
class Client(object):
    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 50000
        self.reconnectTimes = 10
        self.buflen = 1024
        self.connectObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.connectObject.connect((self.ip, self.port))
            print('连接成功')
        except:
            print('连接失败, 准备进行重连>>>')
            while self.reconnectTimes:
                try:
                    self.connectObject.connect((self.ip, self.port))
                    print('连接成功')
                    break
                except:
                    self.reconnectTimes -= 1
                    print(f'重连剩余{self.reconnectTimes}次')
                    time.sleep(2)

    def sendMessage(self):
        self.message = input('请输入要发送的消息>>>')
        while not self.message:
            self.message = input('输入为空, 重新输入>>>')
        if self.message == 'exit':
            self.connectObject.close()
            return '404'
        self.connectObject.send(self.message.encode(encoding='utf-8'))

    def reviceData(self):
        print('开始接收')
        self.rawData = self.connectObject.recv(self.buflen)
        print('进行转码')
        self.resultData =  self.rawData.decode(encoding='utf-8')
        return self.resultData

    def run(self):
        self.status = None
        while True:
            self.status = self.sendMessage()
            if self.status == '404':
                print('客户端关闭连接 >>>')
                break
            self.data = self.reviceData()
            print(f'接收到服务器返回消息, 内容为{self.data}')
               
c = Client()
c.run()