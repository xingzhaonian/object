import GC_Message.Deserialize
GC_GetRankInfo = {
	# 【int】：消息唯一编号
	'msgId':108002,
	# 【int】：无服务器配对消息
	'resMsgId':0,
	# 【int】：等待服务器对应的消息返回;1:等待；0：不等待，默认为1
	'sync':1,
	# 【String】：消息名
	'name':"GC_GetRankInfo",
	# 【byte】消息自增号,当超过127时,自动从1开始继续增长
	'msgIncreaseNum':0,
	# 【int】 错误码，0：正确；非0：业务返回的异常结果
	'errorCode':0,
	# 【short】：rankType :排行榜类型
	'rankType':0,
	# 【long】：rankSize :排行榜大小 前端根据自己排名算比例
	'rankSize':0,
	# 【Array<RankInfoBean>】：rankInfoBeanList :排行榜数据
	'rankInfoBeanList':None,
	# 【RankInfoBean】：myRankInfoBean :我的排名
	'myRankInfoBean':None,
}

def deserialize_rank_info(message_data):
    rank_info  = GC_Message.Deserialize.Analysis(message_data)
    encryptionid = rank_info.GetBytes()
    serial = rank_info.GetInt()
    msg_length  = rank_info.GetInt()
    msgId = rank_info.GetInt()
    msgIncreaseNum = rank_info.GetBytes()
    errorCode =rank_info.GetInt()
    rankType = rank_info.GetShort()
    rankSize = rank_info.GetLong()
    rank_info_list = rank_info.RankBeanList()
    my_rank_info= rank_info.RankInfoBean()
    return msgId, msgIncreaseNum, errorCode, rankType, rankSize, rank_info_list, my_rank_info

