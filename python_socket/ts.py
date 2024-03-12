# === 服务器程序 server.py ===

# 导入 socket模块
import socket

# 初始化ip, 端口, 每次接收最大字节数
ip = '127.0.0.1'
port = 50000
serverBufLen = 1024

# 指定协议, 创建连接对象
server_sockObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定ip
server_sockObject.bind((ip, port))

# 设置监听, 服务器处理客户端用户数量
server_sockObject.listen(5)
print('服务器启动成功, 等待客户端进行连接...')

while True:
    # 等待客户端进行连接
    try:
        server_ConnectObject, addr = server_sockObject.accept()
    except:
        break
    print(f'客户端连接成功, 客户端信息{server_ConnectObject}, ip:{addr[0]}, 端口:{addr[1]}')

    while True:
        # 服务器接收客户端发来的消息, 接收到的数据为空则视为客户端断开连接, 关闭服务器
        try:
            serverReviceData = server_ConnectObject.recv(serverBufLen)
            print(f'接收到客户端发来的消息, 内容为{serverReviceData}')
        except:
            break

        # 判空处理
        if not serverReviceData:
            break

        # 解码接收到客户端发来的消息, 使用 utf-8 编码格式
        serverReviceData = serverReviceData.decode('utf-8')
        print(f"解码后为{serverReviceData}")

        # 把客户端发来的字符串改为大写
        serverReturnData = serverReviceData.upper()

        # 将要返回的消息数据进行编码, 使用 utf-8 编码格式
        after_serverReturnData = serverReturnData.encode('utf-8')

        # 向客户端返回消息
        server_ConnectObject.send(after_serverReturnData)
        print(f'向客户端返回数据成功, 内容为{serverReturnData}, 等待客户端再次发送数据>>>')

    server_ConnectObject.close()
    
server_sockObject.close()