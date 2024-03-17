# cmd文件 客户端
import socket
import json
import pathlib

ip = '127.0.0.1'
port = 5060

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

# 传给客户端header信息
while True:
    cmd = input('输入指令 >>>')
    while not cmd:
        cmd = input('指令为空, 请重新输入')
    cmd_str_h = len(cmd)

    cmd_bytes_h = bytes(str(cmd_str_h), encoding = 'utf-8').zfill(4)
    print(f"发送指令的大小给服务器==={int(cmd_bytes_h.decode('utf-8'))}")
    client.send(cmd_bytes_h)

    print(f"发送序列化后的指令==={cmd.encode('utf-8')}")
    client.send(cmd.encode('utf-8'))

    # 收取头部信息长度
    header_data_h = int(client.recv(4).decode('utf-8'))
    print(f"获取到头部信息长度:==={header_data_h}")

    # 收取json头部数据
    json_data = client.recv(header_data_h)
    print(f"获取到json头部数据:==={json_data}")
    json_tranform_dict = json.loads(json_data)
    print('文件名===', json_tranform_dict['file_name'])
    print('文件大小===', json_tranform_dict['file_size'])
    print('MD5信息===', json_tranform_dict['md5'])


    # 收取数据大小信息
    data_h = int(client.recv(8).decode('utf-8'))
    print(f"收取到数据内容信息的大小:==={data_h}")

    # 收取数据内容
    data = bytes()
    recv_data_h = 0
    while recv_data_h < data_h:
        res_data = client.recv(1024)
        data += res_data
        recv_data_h += len(res_data)

    path = pathlib.Path('D:/project/object/test_file/download.txt')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data.decode('utf-8'))
        
    #print(f"服务器返回的数据总体内容为{data.decode(encoding='utf-8')}")
    print(f'接收到服务返回总体数据的长度为==={len(data)}')








    


