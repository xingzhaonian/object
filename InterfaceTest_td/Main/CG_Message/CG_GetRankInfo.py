import CG_Message.Serialize

CG_GetRankInfo = {
	# 【int】：消息唯一编号
	'msgId':108001,
	# 【int】：与服务器消息配对的消息编号
	'resMsgId':108002,
	# 【int】：等待服务器对应的消息返回;1:等待；0：不等待，默认为1
	'sync':1,
	# 【String】：消息名
	'name':"CG_GetRankInfo",
	# 【byte】消息自增号,当超过127时,自动从1开始继续增长
	'msgIncreaseNum':0,
	# 【short】：rankType :排行榜类型
	'rankType':0,
}

def serialize_get_rank_info(type):
    msgid = CG_GetRankInfo['msgId']
    msgIncreaseNum = CG_GetRankInfo['msgIncreaseNum']
    ranktype = type
    data = CG_Message.Serialize.Assemble()
    data.PutInt(msgid)
    data.PutBytes(msgIncreaseNum)
    data.PutShort(ranktype)
    result = data.Result()
    return result



