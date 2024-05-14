import CG_Message.Serialize


CG_GetPlayerInfoData = {
	# 【int】：消息唯一编号
	'msgId' : 101001,

	# 【int】：与服务器消息配对的消息编号
	'resMsgId' : 101002,

	# 【int】：等待服务器对应的消息返回;1:等待；0：不等待，默认为1
	'sync' : 1,

	# 【String】：消息名
	'name' : "CG_GetPlayerInfo",
	
	# 【byte】消息自增号,当超过127时,自动从1开始继续增长
	'msgIncreaseNum' : 0,
}


def serialize_player_info():
    msgid = CG_GetPlayerInfoData['msgId']
    msgIncreaseNum = CG_GetPlayerInfoData['msgIncreaseNum']
    data = CG_Message.Serialize.Assemble()
    msgid_bytes = data.PutInt(msgid)
    msgIncreaseNum_bytes = data.PutBytes(msgIncreaseNum)
    result = data.Result()
    return result


