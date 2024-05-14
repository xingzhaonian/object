import GC_Message.Deserialize

GC_GetPlayerInfo = {
    # 【int】：消息唯一编号
    'msgId' : 101002,
	# 【int】：无服务器配对消息
	'resMsgId' : 0,
	# 【int】：等待服务器对应的消息返回;1:等待；0：不等待，默认为1
	'sync' : 1,
	# 【String】：消息名
	'name' : "GC_GetPlayerInfo",
	# 【byte】消息自增号,当超过127时,自动从1开始继续增长
	'msgIncreaseNum' : 0,
	# 【int】 错误码，0：正确；非0：业务返回的异常结果
	'errorCode' : 0,
	# 【int】：lv :玩家等级
	'lv' : 0,
	# 【long】：exp :经验
	'exp' : 0,
	# 【String】：nickName :玩家昵称
	'nickName' : "",
	# 【String】：pic :玩家头像
	'pic' : "",
	# 【String】：picFrame :玩家头像框
	'picFrame' : "",
	# 【long】：power :战力
	'power' : 0,
	# 【String】：language :设置语言
	'language' : "",
	# 【int】：rankLv :已经突破的阶级
	'rankLv' : 0,
	# 【Object<String, Map>】：guides :key引导类型， value引导步骤的状态
	'guides' : None,
	# 【Object<Integer, Map>】：picList :头像列表
	'picList' : None,
	# 【Object<Integer, Map>】：picFrameList :头像框列表
	'picFrameList' : None,
	# 【int】：changeNameNum :改名次数
	'changeNameNum' : 0,
	# 【int】：battleStyle :战斗风格 0初始自动战斗 1初始手动战斗
	'battleStyle' : 0,
	# 【Array<List>】：evoGuide :进化指南已领取档位id
	'evoGuide' : None,
	# 【int】：unlockAutoBattle :强制解锁自动战斗 -1表示未初始化该字段
	'unlockAutoBattle' : 0
}


def deserialize_player_info(message_data):
    player_info = GC_Message.Deserialize.Analysis(message_data)
    encryptionid = player_info.GetBytes()
    serial = player_info.GetInt()
    msg_length = player_info.GetInt()
    msgId = player_info.GetInt()
    msgIncreaseNum = player_info.GetBytes()
    error_code = player_info.GetInt()
    lv = player_info.GetInt()
    exp = player_info.GetLong()
    nickName = player_info.GetString()
    pic = player_info.GetString()
    picFrame = player_info.GetString()
    power = player_info.GetLong()
    language = player_info.GetString()
    return msgId, msgIncreaseNum, error_code, lv, exp, nickName, pic, picFrame, power, language




