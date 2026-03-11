import GC_Message.Deserialize
GC_PushChangedItems = {
	# 【int】：消息唯一编号
	'msgId':101106,
	# 【int】：无服务器配对消息
	'resMsgId':0,
	# 【int】：等待服务器对应的消息返回;1:等待；0：不等待，默认为1
	'sync':1,
	# 【String】：消息名
	'name':"GC_PushChangedItems",
	# 【byte】消息自增号,当超过127时,自动从1开始继续增长
	'msgIncreaseNum':0,
	# 【int】 错误码，0：正确；非0：业务返回的异常结果
	'errorCode':0,
	# 【Array<ItemBean>】：itemBeanList :当前拥有的数量
	'itemBeanList':None
}


def deserialize_push_changed_itemse(message_data):
    itme_info = GC_Message.Deserialize.Analysis(message_data)
    encryptionid = itme_info.GetBytes()
    serial = itme_info.GetInt()
    msg_length  = itme_info.GetInt()
    msgId = itme_info.GetInt()
    msgIncreaseNum = itme_info.GetBytes()
    errorCodes = itme_info.GetInt()
    itemBeanList = itme_info.ItemBeanList()
    return msgId, msgIncreaseNum, errorCodes, itemBeanList


