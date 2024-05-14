'''
GetBytes    --int (1个字节)
GetBool     --bool (1个字节)
GetShort    --int (2个字节)
GetInt      --int (4个字节)
GetLong     --int (8个字节)
GetString   --str (调用Getint取出长度, 再将str.)
Getfloat    --float (struct.unpack,   4个字节)
GetDouble   --int (8个字节)
'''

import struct
class Analysis(object):

    # 初始化指针, 跟踪当前位置
    def __init__(self, bytes_data):
        #print(f'当前消息长度：{len(bytes_data)}')
        self.index = 0
        self.bytes_data = bytes_data

    # 获取 1 个字节的Int
    def GetBytes(self):
        self.bytes = self.bytes_data[self.index:self.index+1][::-1]
        self.bytes = int.from_bytes(self.bytes, byteorder='little', signed=True)
        self.index += 1
        #print(f'指针位置{self.index}')
        return self.bytes

    # 获取 1 个字节的bool, 0 or 1
    def GetBool(self):
        self.bool_bytes = self.bytes_data[self.index:self.index+1][::-1]
        self.bool_bytes = int.from_bytes(self.bool_bytes, byteorder='little', signed=True)
        self.index += 1
        #print(f'指针位置{self.index}')
        return self.bool_bytes
    
    # 获取 2 个字节的int
    def GetShort(self):
        self.short = self.bytes_data[self.index:self.index + 2][::-1]
        self.short = int.from_bytes(self.short, byteorder='little', signed=True)
        self.index += 2
        #print(f'指针位置{self.index}')
        return self.short

    # 获取 4 个字节的int
    def GetInt(self):
        self.ints = self.bytes_data[self.index:self.index+4][::-1]
        self.ints = int.from_bytes(self.ints, byteorder='little', signed=True)
        self.index += 4
        #print(f'指针位置{self.index}')
        return self.ints

    # 获取 8 个字节的int
    def GetLong(self):
        self.long = self.bytes_data[self.index:self.index+8][::-1]
        self.long = int.from_bytes(self.long, byteorder='little', signed=True)
        self.index += 8
        #print(f'指针位置{self.index}')
        return self.long
    

    # 获取字符串, 先取字符长度, 指针自动定位到字符串对应的bytes起始位置
    def GetString(self):
        self.String_length = self.GetInt()
        if self.String_length <= 0:
            return ''
        self.String = self.bytes_data[self.index:self.index + self.String_length]
        self.index += self.String_length
        #print(f'指针位置{self.index}')
        self.String = self.String.decode(encoding='utf-8')
        return self.String
    
    # 获取 4 个字节的 float
    def Getfloat(self):
        self.floats = self.bytes_data[self.index:self.index+4][::-1]
        self.floats = struct.unpack('f', self.floats)[0]
        self.index += 4
        #print(f'指针位置{self.index}')
        return round(self.floats, 4)
    
    # 获取 8 个字节的int
    def GetDouble(self):
        self.Double = self.bytes_data[self.index:self.index+8][::-1]
        self.Double = struct.unpack('f', self.Double)[0]
        self.index += 8
        #print(f'指针位置{self.index}')
        return round(self.Double, 4)
    
    # 排行榜中玩家的信息
    def GetPlayBeanInfo(self):
        self.playinfo = []
        # [long] 玩家id
        self.GetInt()
        self.playerid = self.GetLong()
        self.playinfo.append(self.playerid)

        # [string] 玩家昵称
        self.nickname = self.GetString()
        self.playinfo.append(self.nickname)


        # [string] 玩家头像编号
        self.icon = self.GetString()
        self.playinfo.append(self.icon)

        # [long] 玩家战力
        self.power = self.GetLong()
        self.playinfo.append(self.power)

        # [int] 玩家服务器id
        self.serverid = self.GetInt()
        self.playinfo.append(self.serverid)

        # [int]  玩家等级
        self.level = self.GetInt()
        self.playinfo.append(self.level)

        # [int]  头像
        self.pic = self.GetInt()
        self.playinfo.append(self.pic)

        # [int] 头像框
        self.picframe = self.GetInt()
        self.playinfo.append(self.picframe)
        return self.playinfo

    # 个人排行榜信息
    def RankInfoBean(self):
        self.rank_bean_info = []

        self.GetInt()
        # [short] 排行榜类型
        self.ranktype = self.GetShort()
        self.rank_bean_info.append(self.ranktype)

        # [int] 当前名次
        self.rank = self.GetInt()
        self.rank_bean_info.append(self.rank)

        # [bytes] 箭头方向, 与上次比较; -1-->上, 0-->不变, 1-->向下
        self.updown = self.GetBytes()
        self.rank_bean_info.append(self.updown)

        # [GetPlayBeanInfo] 玩家信息
        self.playerinfobean = self.GetPlayBeanInfo()
        self.rank_bean_info.append(self.playerinfobean)

        # [long] 玩家分数
        self.score =  self.GetLong()
        self.rank_bean_info.append(self.score)

        return self.rank_bean_info

    # 排行榜列表
    def RankBeanList(self):
        self.ranklist = []

        self.ranklist_length = self.GetInt()
        for i in range(self.ranklist_length):
            self.ranklist.append(self.RankInfoBean())
        return self.ranklist


    def ItemBeanInfo(self):
        self.itemlist = []
        # 资源类型
        self.GetInt()
        self.item_type = self.GetShort()
        self.itemlist.append(self.item_type)

        # 资源id
        self.item_id = self.GetInt()
        self.itemlist.append(self.item_id)

        # 数量
        self.num = self.GetLong()
        self.itemlist.append(self.num)

        # 扩展字段
        self.extra = self.GetString()
        self.itemlist.append(self.extra)
        return self.itemlist
    


    def ItemBeanList(self):
        self.item_bean_list = []
        self.item_bean_length = self.GetInt()

        for i in range(self.item_bean_length):
             self.item_bean_list.append(self.ItemBeanInfo())
        return self.item_bean_list
            



    

    def RewardTimes(self):
        self.reward_list = []
        self.drawcard_times = self.GetInt()
        self.reward_list.append(self.drawcard_times)
        return self.reward_list
    

    def RewardCd(self):
        self.reward_cd_list = []
        self.drawcard_cd = self.GetLong()
        self.reward_cd_list.append(self.drawcard_cd)
        return self.reward_cd_list

    def SafeTimes(self):
        self.GetInt()
        self.safe_times = []

        self.rank_lv_count = self.GetInt()
        self.safe_times.append(self.rank_lv_count)

        self.type_counte = self.GetInt()
        self.safe_times.append(self.type_counte)
        
        return self.safe_times        
    


        












    


    