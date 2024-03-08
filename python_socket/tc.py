# ==== TCP客户端端程序 client.py ====

import socket
# 初始化IP地址
IP = '192.168.1.3'
SERVER_PORT = 50000
BUFLEN = 512
print('我是客户端')
# 实例化 socket对象, 指明协议
dataSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('客户端准备进行连接服务器。。。')
dataSocket.connect((IP, SERVER_PORT))
print('客户端连接服务器成功, 你可以发送消息了')

while True:
    toSend = input('>>')
    if toSend == 'exit':
        break
    # 发送进行编码后的消息
    dataSocket.send(toSend.encode())

    # 等待接收服务端的消息
    recved = dataSocket.recv(BUFLEN)
    # 返回为空bytes, 表示对方关闭了连接
    if not recved:
        break
    print(f'服务器返回的消息为{recved.decode()}')
dataSocket.close()


