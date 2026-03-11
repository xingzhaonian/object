# === 客户端程序 client.py ===

import json
import socket
import time 

# 管理客户端连接和相关方法

class Client(object):
    def __init__(self):
        # 初始化服务器参数, 向服务器建立连接
        self.ip = "192.168.8.146"
        self.port = 15002
        self.reconnectTimes = 10
        print('开始建立连接')
        self.clientConnectObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print('连接中 >>>')
            self.clientConnectObject.connect((self.ip, self.port))
            print('连接成功 >>>')
        except:
            while self.reconnectTimes:
                try:
                    self.clientConnectObject.connect((self.ip, self.port))
                    print('连接成功>>>')
                    break
                except:
                    print(f'连接失败, 开始重连, 剩余重连次数{self.reconnectTimes}')
                    self.reconnectTimes -= 1
                    time.sleep(1)
    
    def sendMessage(self):
        self.message = input('请输入要发送的内容 >>>')
        while not self.message:
            self.message = input('输入为空, 请重新输入 >>>')
        if self.message == 'exit':
            self.clientConnectObject.close()
            return '404'
        self.message = self.message.encode(encoding='utf-8')
        try:
            self.clientConnectObject.send(self.message)
        except:
            print('连接失败, 无法发送')
            return 
        print('发送成功')

    def receviceData(self):
        self.value = self.clientConnectObject.recv(2048)
        self.data = self.value.decode('utf-8')
        return self.data 
    
    def run(self):
        self.status = None
        while True:
            self.status = self.sendMessage()
            if self.status == '404':
                print('客户端关闭连接 >>>')
                break
            self.data = self.receviceData()
            print(f'接收到服务器返回消息, 内容为{self.data}')




c = Client()
c.run()


    



    
