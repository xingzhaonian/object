import GC_Message.Deserialize
def deserialize_msg_length(message_data):
    message_info = GC_Message.Deserialize.Analysis(message_data)
    encryptionid = message_info.GetBytes()
    serial = message_info.GetInt()
    msg_length = message_info.GetInt()
    msgId = message_info.GetInt()
    return msg_length