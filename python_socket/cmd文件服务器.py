# cmd文件 服务器
import socket
import subprocess
import json
import pathlib
import hashlib

class serverSocket(object):
    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 5060
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(5)
        print('服务器启动成功, 等待客户端连接')
        self.conncet_status = None
        while True:
            try:
                self.connectObject, self.addres = self.server.accept()
                self.conncet_status = 1
                if self.conncet_status == 1:
                    print(f'拿到连接对象, 对象信息:==={self.connectObject}, \n ip:{self.addres[0]}, \n port:{self.addres[1]}')
                    break
            except:
                self.connectObject.close()
                break
    def Upload(self):
        while True:
            try:
                self.res_data_size = int(self.connectObject.recv(4).decode(encoding='utf-8'))
                print(f'客户端发来的消息长度==={self.res_data_size}')
            except:
                self.connectObject.close()
                break
            self.data = bytes()
            self.each_size = 0
            while self.each_size < self.res_data_size:
                res_data = self.connectObject.recv(1024)
                self.data += res_data
                self.each_size += len(res_data)
            self.cmd_data = self.data.decode('utf-8')

            with open(pathlib.Path(self.cmd_data), 'r', encoding='utf-8')as f:
                self.data_txt = f.read()
            #obj = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #stdout = obj.stdout.read()
            #3stderr = obj.stderr.read()
            #result_data_h = len(stdout) +len(stderr)
            
            self.header = {
                'file_name': self.cmd_data.split('\\')[-1],
                'file_size':pathlib.Path(self.cmd_data).stat()[6],
                'md5':hashlib.md5(self.data_txt.encode('utf-8')).hexdigest(),
                'isuse':True
            }

            self.return_data = self.data_txt.encode('utf-8')
            self.data_txt_h = len(self.data_txt.encode('utf-8'))
            self.data_h = bytes(str(self.data_txt_h), encoding='utf-8').zfill(8)

            self.heard_json = json.dumps(self.header)

            self.heard_json_info = self.heard_json.encode(encoding = 'utf-8')        

            hearer_h = bytes(str(len(self.heard_json_info)), encoding = 'utf-8').zfill(4)

            # 发送头部信息长度
            self.connectObject.send(hearer_h)

            # 发送头部json数据
            self.connectObject.send(self.heard_json_info)

            # 发送数据内容大小
            self.connectObject.send(self.data_h)
           
            #发送内容
            self.connectObject.send(self.return_data)


    def download(self):
        pass

if __name__ == '__main__':
    s = serverSocket()
    s.Upload()
    




    

