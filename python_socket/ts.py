# ==== TCP 服务端程序 server.py =====
import socket

IP = '192.168.1.3'
PORT = 50000
BUFLEN = 512
print('我是服务器')
listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listenSocket.bind((IP, PORT))

listenSocket.listen(5)
print(f'服务端启动成功，在{PORT}端口等待客户端连接...')
dataSocket, addr = listenSocket.accept()
print('接受了一个客户端连接, IP为:', addr[0], '端口为:',addr[1])

while True:
    recved = dataSocket.recv(BUFLEN)

    # 如果对方返回空的bytes, 表示对方关闭了连接, 退出循环, 结束消息收发
    if not recved:
        break
    # 读取的字节数据是bytes类型, 需要解码
    info = recved.decode()
    print(f'客户端发来的消息：{recved}, 解析后为{info}')
    send_info = recved + b'LOL'

    # 发送的数据类型必须是bytes, 所以要进行编码
    print(f'向客户端返回消息：{send_info}', '解析后为', send_info.decode())
    
    dataSocket.send(send_info)

# 服务端也调用close() 关闭socket
dataSocket.close()
listenSocket.close()





