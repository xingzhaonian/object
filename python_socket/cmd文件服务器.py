# cmd文件 服务器
import socket
import subprocess
import json
import pathlib
import hashlib

ip = '127.0.0.1'
port = 5060

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(5)
print('服务器启动成功, 等待客户端连接')

while True:
    try:
        connectObject, addres = server.accept()
        print(f'拿到连接对象, 对象信息:==={connectObject}, \n ip:{addres[0]}, \n port:{addres[1]}')
    except:
        connectObject.close()
        break
    while True:
        try:
            res_data_size = int(connectObject.recv(4).decode(encoding='utf-8'))
            print(f'客户端发来的消息长度==={res_data_size}')
        except:
            connectObject.close()
            break
        data = bytes()
        each_size = 0
        while each_size < res_data_size:
            res_data = connectObject.recv(1024)
            data += res_data
            each_size += len(res_data)
        cmd_data = data.decode('utf-8')

        with open(pathlib.Path(cmd_data), 'r', encoding='utf-8')as f:
            data_txt = f.read()
        #obj = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #stdout = obj.stdout.read()
        #3stderr = obj.stderr.read()
        #result_data_h = len(stdout) +len(stderr)
        
        header = {
            'file_name': cmd_data.split('\\')[-1],
            'file_size':pathlib.Path(cmd_data).stat()[6],
            'md5':hashlib.md5(data_txt.encode('utf-8')).hexdigest(),
            'isuse':True
        }

        return_data = data_txt.encode('utf-8')
        data_txt_h = len(data_txt.encode('utf-8'))
        data_h = bytes(str(data_txt_h), encoding='utf-8').zfill(8)

        heard_json = json.dumps(header)
        print(f'已将dict转为json, 内容为==={heard_json}')

        heard_json_info = heard_json.encode(encoding = 'utf-8')        
        print(f'已将json进行序列化, 内容为==={heard_json_info}')

        hearer_h = bytes(str(len(heard_json_info)), encoding = 'utf-8').zfill(4)
        print(f"拿到json序列化后的长度, 也就是头部信息的长度, 长度是==={int(hearer_h.decode(encoding='utf-8'))}")

        # 发送头部信息长度
        connectObject.send(hearer_h)
        print(f"已经将头部信息长度发送给客户端, 长度为==={int(hearer_h.decode('utf-8'))}")

        # 发送头部json数据
        connectObject.send(heard_json_info)
        print(f'已经将头部json数据发给客户端, 内容为==={heard_json_info}')

        # 发送数据内容大小
        connectObject.send(data_h)
        print(f"已经将数据内容大小发给客户端, 长度为==={int(data_h.decode(encoding='utf-8'))}")

        #发送内容
        connectObject.send(return_data)
        print('已经将数据总体内容发给客户端')

    




    

