# cmd 服务器
import socket
import subprocess

ip = '127.0.0.1'
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 地址重用
server.bind((ip, port))  # 绑定ip, 端口
server.listen(5) # 设置半连接池
print('服务器启动成功, 等待客户端连接 >>>')
while True:
    conn, addr= server.accept()
    print('连接成功, 客户端信息', addr)
    while True:
        try:
            cmd_size = int(conn.recv(8).decode(encoding='utf-8'))
            res_data = bytes()
            recv_size = 0
            while recv_size < cmd_size:
                data = conn.recv(1024)
                res_data += data
                recv_size += len(res_data)
        except:
            break

        obj = subprocess.Popen(res_data.decode(encoding='utf-8'),
                         shell = True,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.PIPE)
        
        
        out_res = obj.stdout.read()
        print('这是正确结果的长度：',len(out_res),'这是正确结果的内容：',out_res )
        out_error = obj.stderr.read()
        print('这是错误结果的长度：',len(out_error),'这是错误结果的内容：',out_error )
        
        # 定义协议, 把header bytes的长度传给客户端
        data_size = len(out_res) + len(out_error)
        headinfo = bytes(str(data_size), encoding = 'utf-8').zfill(8)
        # 发送 headinfo 
        conn.send(headinfo)

        # 发送内容
        conn.send(out_res)
        conn.send(out_error)


        

    # 接收到的指令作为终端命令来执行

    conn.close()


