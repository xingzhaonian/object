# === 客户端程序 server.py ===

# 导入 socket模块
import socket

# 初始化ip, 端口, 每次传输最大字节数
ip = '127.0.0.1'
port = 50000
ClientBufLen = 1024

# 指定协议, 创建连接对象
client_ConnectObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 向服务器发起连接请求
client_ConnectObject.connect((ip, port))
print('连接成功')

while True:
    # 向服务器发送消息
    client_SendData = input('请发送消息>>>')

    # 判空处理
    if not client_SendData:
        continue

    # 输入 'exit' 退出连接
    if client_SendData == 'exit':
        break

    # 将要发送的数据进行编码
    after_TranscodeClientSendData = client_SendData.encode('utf-8')

    # 发送转码后的数据
    client_ConnectObject.send(after_TranscodeClientSendData)
    print('发送成功, 等待服务器返回消息')
    
    # 接收服务器返回的消息
    client_ReceiveData = client_ConnectObject.recv(ClientBufLen)
    print(f"接收服务器返回消息成功, 内容为:{client_ReceiveData},  编码后内容为:{client_ReceiveData.decode('utf-8')}")
