# ===== 我是客户端 client.py =====

import socket

ip = '192.168.1.3'
port = 50000
buflen = 1024

socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketObject.connect((ip, port))

while True:
    send_data = input('请发送消息>>>')

    if not send_data:
        print('发送消息为空, 请重新输入')
        continue

    if send_data == 'exit':
        print('客户端中断连接')
        break

    print(f'向服务器发送消息, 内容为{send_data}')
    send_data = send_data.encode('utf-8')
    print(f'编码后为{send_data}')
    socketObject.send(send_data)
    print('向服务器发送成功, 等待服务器返回消息>>>')
    print('===================*********************=====================')
    receive_data  = socketObject.recv(buflen)
    print(f'接收到服务器返回消息, 内容为{receive_data}')
    print(f"进行解码, 解码后的内容为{receive_data.decode('utf-8')}")

socketObject.close()

