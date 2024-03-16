# cmd 客户端
import socket 
import time 
import json
ip = '127.0.0.1'
port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

while True:
    cmd = input('输入终端指令 >>>')
    heheadinfo = len(bytes(cmd, encoding = 'utf-8'))
    header_size = bytes(str(heheadinfo), encoding = 'utf-8').zfill(8)
    if not cmd:
        continue
    client.send(header_size)
    client.send(cmd.encode(encoding = 'utf-8'))

# 解决粘包问题
    
#服务器返回的数据量大, 每次收取1024个字节, 一次可能收取不完整, 分多次收取。
#但也不能每次收取过大的数据量, 有可能单次收取量大于缓存中的数据, 但由于网络原因
#数据还没发到缓存池里, 我们就直接收取了, 所以我们要保证的是每次收取数据的量不能
#太大, 保证总数据量大于1024的时候, 我们能收取到1024个字节,剩余数据小于1024的时候
#我们能收取到缓存中的全部剩余数据

    data_size = int(client.recv(8).decode('utf-8'))
    recv_size = 0
    data = bytes()
    while recv_size < data_size:
        res_data = client.recv(1024)

        # 如果这里数据量巨大, 那就需要边读边存文件
        data += res_data
        recv_size += len(res_data)
    
    print(data.decode('gbk'))
    print(len(data))



    
        

    