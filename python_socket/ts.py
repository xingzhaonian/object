# ===== 我是服务器 server.py =====

import socket

ip = '192.168.1.3'
port = 50000
buflen = 1024

socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketObject.bind((ip, port))
socketObject.listen(5)
print(f'服务器启动成功, 在{port}端口等待进行连接...')
connetObject, addr = socketObject.accept()
print(f'连接对象:{connetObject}, ip地址:{addr[0]}, 端口:{addr[1]}')

while True:
    receive_data = connetObject.recv(buflen)
    print(f'客户端发来了消息, 内容是{receive_data}')
    if not receive_data:
        break
    receive_data = receive_data.decode('utf-8')
    print(f'解码后为{receive_data}')


    receive_data = receive_data.upper()
    print(f'向客户端返回消息, 内容为{receive_data}')
    send_data = receive_data.encode('utf-8')
    print(f'需要进行编码, 编码后内容为{send_data}')
    connetObject.send(send_data)
    print('返回消息完成, 等待再次接收消息中>>>')

connetObject.close()
socketObject.close()






