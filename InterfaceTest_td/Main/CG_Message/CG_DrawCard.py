import CG_Message.Serialize

CG_DrawCard = {
	# 【int】：消息唯一编号
	'msgId':104003,
	# 【int】：与服务器消息配对的消息编号
	'resMsgId':104004,
	# 【int】：等待服务器对应的消息返回;1:等待；0：不等待，默认为1
	'sync':1,
	# 【String】：消息名
	'name':"CG_DrawCard",
	# 【byte】消息自增号,当超过127时,自动从1开始继续增长
	'msgIncreaseNum':0,
	# 【int】：drawType :抽卡方式 1道具1免费抽 2道具2免费抽 3道具1普通抽 4道具2普通抽 5钻石抽
	'drawType':0,
	# 【int】：drawNum :抽卡数 1 or 10
	'drawNum':0,
}

def serialize_draw_card(types, times):
    msgid = CG_DrawCard['msgId']
    msgIncreaseNum = CG_DrawCard['msgIncreaseNum']
    draw_type = types
    draw_num = times
    data = CG_Message.Serialize.Assemble()
    data.PutInt(msgid)
    data.PutBytes(msgIncreaseNum)
    data.PutInt(draw_type)
    data.PutInt(draw_num)
    result = data.Result()
    return result



