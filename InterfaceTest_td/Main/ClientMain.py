import requests 
import json
import socket
import CG_Message
import GC_Message
import threading
import time


class Client(object):

    def __init__(self):
        # 初始化登陆地址和访问url的参数
        self.url = 'http://192.168.8.32:10069/login'
        self.data = '{"channel":"develop","token":"","sign":"","pushToken":"","baseId":"develop_baseid","subId":"develop_subid",\
            "packageVersion":"1.0.6874","platform":"rgoogle_22003001","isVerify":false,"createRole":false,"isUiLogin":true,\
            "pidPrefix":"GG_","userType":1,"rsdkLoginTime":"1699444916","extraParams":{"sessionId":"cbcf9881afb757d9dde51056a853fb76",\
            "deviceId":"","osId":"","ram":"32709 MB","appId":"com.MoonJoy.TD","os":"unsupported"},"uid":0,"mode":0,"buildVer":"6874",\
            "pid":"qs80","s":259}'
        
        self.total_data = bytes()
        self.targetMsgId = 0
        self.action = None

        # 发送登陆地址请求
        self.response = requests.post(self.url, self.data)

        # 取出登陆地址请求返回的相关数据
        self.response = json.loads(self.response.text)
        print(self.response)


        # 初始化socket ip和端口
        self.td_ip = '192.168.8.32'
        self.td_port = 16098

        #qs_ip = '192.168.7.133'
        #qs_port = 7777

        # 创建socket连接对象
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((self.td_ip, self.td_port))

        # 接收序列化后的消息数据
        self.data = CG_Message.CG_verify.verify_data(self.response)
        #print(f'消息长度{len(self.data)}, 消息内容{self.data}')
        self.targetMsgId = 100002
        # 发送 CG_Verify验证
        self.clientSocket.send(self.data)
        print('已发送CG_Verify, 等待验证 >>>')


    def recv_data(self):
        each_msg_length = 1024
        each_recv_msg = bytes()
        while True:
            self.total_data = self.clientSocket.recv(1024)
            msgId = GC_Message.GC_GetMessageId.deserialize_msgid(self.total_data)
            msg_length = GC_Message.GC_GetMessageLength.deserialize_msg_length(self.total_data)
            while msg_length >= each_msg_length:
                each_recv_msg = self.clientSocket.recv(1024)
                self.total_data += each_recv_msg
                each_msg_length +=len(each_recv_msg)

            #print(f"消息id: {msgId}")
            if msgId == self.targetMsgId:
                if self.action != None:
                    self.action()
                self.targetMsgId = 0

    def CG_GetPlayerInfo(self):
        #发送CG_GetPlayerInfo
        sendMessage_data = CG_Message.CG_GetPlayerInfo.serialize_player_info()
        self.targetMsgId = 101002
        self.action = self.GC_GetPlayerInfo
        self.clientSocket.send(sendMessage_data)
        while self.targetMsgId != 0:
            time.sleep(0.1)
            continue


    def GC_GetPlayerInfo(self):
        self.player_info = GC_Message.GC_GetPlayerInfo.deserialize_player_info(self.total_data)
        self.msgIncreaseNum = self.player_info[1]
        self.error_code = self.player_info[2]
        self.player_lv = self.player_info[3]
        self.player_exp = self.player_info[4]
        self.player_nickName = self.player_info[5]
        self.player_pic = self.player_info[6]
        self.player_picFrame = self.player_info[7]
        self.player_power = self.player_info[8]
        self.player_language = self.player_info[9]
        print(f"消息自增号:{self.msgIncreaseNum}, 错误码{self.error_code}, 玩家等级:{self.player_lv}, 玩家经验:{self.player_exp}, 玩家昵称:{self.player_nickName}, 玩家头像:{self.player_pic}, 玩家头像框:{self.player_picFrame}, 玩家战力:{self.player_power}, 语言设置:{self.player_language}")

    def CG_GetRankInfo(self, type = 102):
        # 获取排行榜数据    101:关卡排行      102：战力排行
        rank_type = type
        sendMessage_data = CG_Message.CG_GetRankInfo.serialize_get_rank_info(rank_type)
        self.targetMsgId = 108002
        self.action = self.GC_GetRankInfo
        self.clientSocket.send(sendMessage_data)
        while self.targetMsgId != 0:
            time.sleep(0.1)
            continue


    def GC_GetRankInfo(self):
        rank_data = GC_Message.GC_GetRankInfo.deserialize_rank_info(self.total_data)
        error_code = rank_data[2]
        self.rankType = rank_data[3]
        self.rankSize = rank_data[4]
        self.rank_info_list = rank_data[5]
        self.my_rank_info = rank_data[6]
        print(f'错误码: {error_code },  排行榜类型:{self.rankType}, 排行榜大小:{self.rankSize}, 排行榜列表: {self.rank_info_list}, 我的排名信息:{self.my_rank_info}')

    def CG_DrwaCard(self, draw_type, times):
        send_message_data = CG_Message.CG_DrawCard.serialize_draw_card(draw_type, times)
        self.targetMsgId = 101106
        self.action = self.GC_DrwaCard
        self.clientSocket.send(send_message_data)
        while self.targetMsgId != 0:
            time.sleep(0.1)
            continue
        
    def GC_DrwaCard(self):
        item_info = GC_Message.GC_GetPushChangeItems.deserialize_push_changed_itemse(self.total_data)
        msgId = item_info[0]
        msgIncreaseNum = item_info[1]
        errorCodes = item_info[2]
        itemBean = item_info[3]
        print(f'消息id:{msgId}, 错误码:{errorCodes}, 物品信息:{itemBean}')



c = Client()
recv_data_thread = threading.Thread(target=c.recv_data)
recv_data_thread.start()

#等GC_Verify返回
while c.targetMsgId != 0:
    time.sleep(0.1)
    continue

c.CG_GetPlayerInfo()
c.CG_GetRankInfo()
c.CG_DrwaCard(5, 1)
