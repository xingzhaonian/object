import GC_Message.Deserialize
def deserialize_msgid(message_data):
    player_info = GC_Message.Deserialize.Analysis(message_data)
    encryptionid = player_info.GetBytes()
    serial = player_info.GetInt()
    msg_length = player_info.GetInt()
    msgId = player_info.GetInt()
    return msgId
