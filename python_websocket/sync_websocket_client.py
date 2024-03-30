import websocket
import json
import time

class Client(object):
    def __init__(self):
        
        self.address =  'ws://192.168.1.12:9528/ws'
        self.WebSocket = websocket.create_connection(self.address)
        print(self.WebSocket)

    
    def SendMessage(self):
        while True:
            msg = input('请输入要发送的消息 >>>')
            self.WebSocket.send(msg)
            recv_msg = self.WebSocket.recv()

    def quit(self):
        self.WebSocket.close()


t = str(time.time() *1000).split('.')[0]
msg = {
    'version':9527,
    'msgNo':t,
    'machNo':'u040119110001',
    'cdm':1,
    'time':t
}


c = Client()
c.SendMessage()