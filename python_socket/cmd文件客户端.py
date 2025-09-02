# cmd文件 客户端

import socket
import json
import pathlib

class ClientSocket(object):
    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 5060

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.ip, self.port))

    # 下载
    def download(self):
        while True:
            self.cmd = input('输入要下载的文件(包含绝对路径) >>>')
            while not self.cmd:
                self.cmd = input('输入为空, 请重新输入 >>>')
            self.cmd_str_h = len(self.cmd)
            self.cmd_bytes_h = bytes(str(self.cmd_str_h), encoding = 'utf-8').zfill(4)
            
            # 发送请求  文件名+绝对路径的请求大小和序列化后的请求
            self.client.send(self.cmd_bytes_h)
            self.client.send(self.cmd.encode('utf-8'))

            # 收取头部信息长度
            self.header_data_h = int(self.client.recv(4).decode('utf-8'))


            # 收取json头部数据
            self.json_data = self.client.recv(self.header_data_h)
            self.json_tranform_dict = json.loads(self.json_data)

            # 获取数据头的相关信息
            self.header_info_name = self.json_tranform_dict['file_name']
            self.header_info_file_size = self.json_tranform_dict['file_size']
            self.header_info_md5 = self.json_tranform_dict['md5']

            # 收取数据大小信息
            self.data_h = int(self.client.recv(8).decode('utf-8'))


            # 收取数据内容并下载服务器传输的数据
            self.data = bytes()
            self.recv_data_h = 0
            path = pathlib.Path('D:/project/object/test_file/download.txt')
            with open(path, 'w', encoding='utf-8') as f:
                while self.recv_data_h < self.data_h:
                    res_data = self.client.recv(1024)
                    self.data += res_data
                    f.write(self.data.decode('utf-8'))
                    self.recv_data_h += len(res_data)
                        
            #print(f"服务器返回的数据总体内容为{data.decode(encoding='utf-8')}")
                
    # 上传
    def Upload(self):
        pass
                
if __name__ == '__main__':
    c = ClientSocket()
    c.download()








    


