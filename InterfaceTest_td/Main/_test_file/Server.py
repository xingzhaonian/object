# === 服务器程序 server.py ===

import socket

# 获取本机ip, port
def get_host_ip():
    socketObject = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        socketObject.connect(('8.8.8.8', 80))
        ipinfo = socketObject.getsockname()
    finally:
        socketObject.close()
        return ipinfo

ip = get_host_ip()[0]
port = get_host_ip()[1]

def startServer(ip, port):
    buflen = 1024
    # 创建连接对象
    socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketObject.bind((ip, port))
    # 设置连接池
    socketObject.listen(5)
    print('服务器启动成功, 等待客户端进行连接 >>>')
    while True:
        # 等待连接
        serverConnetObject, addr = socketObject.accept()
        print(f'连接成功, 客户端信息{serverConnetObject}, ip:{addr[0]}, port:{addr[1]}')
        while True:
            receiveMessage = serverConnetObject.recv(buflen)
            resultData = receiveMessage.decode(encoding='utf-8')
            print('客户端发来了消息, 内容为{resultData}')

            resultData = resultData.upper()

            # 向客户端返回消息
            serverConnetObject.send(resultData.encode(encoding='utf-8'))
            print('消息返回成功')

startServer(ip, port)

