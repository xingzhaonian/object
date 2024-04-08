import websocket
import json
import time
import threading
import requests
import hashlib
import base64


class Client(object):
    def __init__(self, pid, server):
        self.pid = pid
        self.server = server
        self.recv_message = ''

        # 访问GameServer
        self.address =  'ws://192.168.8.196:15002/'
        self.WebSocket = websocket.create_connection(self.address)


    def GetLastServer(self):
        # 获取最后一次登录的服务器
        self.login_before_url = 'http://gd-local-83.leishenhuyu.com/tank-global/index.php/?t=getlastserver&pid=' + str(self.pid) + '&version=0&isnew=true'
        self.LastServerResponse = requests.get(self.login_before_url)
        self.LastServerResponse = json.loads(self.LastServerResponse.text)
        self.LiastZid =self.LastServerResponse['server']['zid']
        return self.LiastZid
    

    def GetServerList(self):
        # 获取服务器列表
        self.get_serverlist_url = 'http://gd-local-83.leishenhuyu.com/tank-global/index.php/?t=getserverlist&pid=' +str(self.pid) + '&version=0'
        self.LastServerListResponse = requests.get(self.get_serverlist_url)
        self.LastServerListResponse = json.loads(self.LastServerListResponse.text)
        return self.LastServerListResponse

    def ServerInfo(self, server):
        # 获取登陆后当前服务器信息
        self.login_after_url = 'http://gd-local-83.leishenhuyu.com/tank-global/index.php/?t=getserverinfobyzid&zid=' + str(self.server)
        self.GetServerInfo = requests.get(self.login_after_url)
        self.GetServerInfo = json.loads(self.GetServerInfo.text)

    
    def GetAccessToken(self):
        # 组装获取Token的参数
        self.urlStr = 'http://gd-local-83.leishenhuyu.com/gucenter/getaccess_token.php?pm='
        self.apkey = '8619EBC7EB8B87F34D1DD8EB563F0F64'
        self.tmpTsStr = str(int(round(time.time() * 1000)))
        self.uname = str(self.pid)
        #self.sign = hashlib.md5(self.apkey.encode('utf-8') + self.tmpTsStr.encode('utf-8' ))
        self.urlparm = 'username=' + self.uname + '&zoneid=' + str(self.server) + '&newzoneid=' + str(self.server) + '&password=' + '&ts=' + self.tmpTsStr
        self.platform = '0'
        self.device = 'Android'
        self.area = 'cn'
        self.urlparm += '&platform=' + self.platform + '&device=' + self.device + '&area=' +  self.area + '&rayparms=1'
        self.urlparm = base64.b64encode(self.urlparm.encode('utf-8'))
        self.urlparm = str(self.urlparm)
        self.urlparm = self.urlparm[2:-1]
        self.qStr = self.urlparm[0:2]
        self.hStr = self.urlparm[2:]
        self.timeStr = base64.b64encode(str(self.tmpTsStr).encode('utf-8'))
        self.timeStr = str(self.timeStr)
        self.timeStr = self.timeStr[2:]
        self.timeStr = self.timeStr[:-1]
        self.urlparm = self.qStr + self.timeStr[:5] +  self.hStr
        self.urlStr +=  self.urlparm
        self.access_token_info = requests.get(self.urlStr)
        self.access_token_dict = json.loads(self.access_token_info.text)
        self.access_token = self.access_token_dict['access_token']
        self.player_id = self.access_token_dict['uid']
        self.login_ts = self.access_token_dict['logints']
        return self.access_token, self.player_id, self.login_ts


    def Recv_data(self):
        while True:
            self.recv_message = self.WebSocket.recv()
            time.sleep(0.1)

    def SendMsg(self, msg):
        msg = json.dumps(msg)
        print(type(msg), msg)
        self.WebSocket.send(msg)
        while self.recv_message == '':
            time.sleep(0.1)
            continue
        recv_msg = self.recv_message
        self.recv_message = ''
        return recv_msg

