
def verify_data(respnose):

    # # # 注意: 遇到int转bytes(), 需要将序列化的bytes进行反转

    message_data = bytes()

    # 消息id --int  4个字节
    msgId = 100001 
    message_data += msgId.to_bytes(4, byteorder='little')[::-1]

    # IncreaseNum --bytes 1个字节
    IncreaseNum = 0
    message_data += IncreaseNum.to_bytes(1, byteorder='little')[::-1]


    # accountID  --long 8字节
    accountID = respnose['data']['accountID']
    message_data += accountID.to_bytes(8, byteorder = 'little')[::-1]

    # sessionID -- string    
    sessionID = respnose['data']['sessionID'].encode('utf-8')
    sessionID_h = len(sessionID)
    sessionID_h_bytes = sessionID_h.to_bytes(4, byteorder='little')[::-1]
    message_data += sessionID_h_bytes
    message_data += sessionID

    # targetUid -- long
    targetUid = respnose['data']['serverInfo']['recommendUid']
    targetUid_bytes = targetUid.to_bytes(8, byteorder='little')[::-1]
    message_data += targetUid_bytes

    #  logicalID -- int
    logicalID = respnose['data']['serverInfo']['logicalID']
    logicalID_bytes = logicalID.to_bytes(4, byteorder='little')[::-1]
    message_data += logicalID_bytes

    # clientIP  --str
    clientIP = respnose['data']['clientIP']
    clientIP_bytes = clientIP.encode('utf-8')
    clientIP_h = len(clientIP_bytes)
    clientIP_h_bytes = clientIP_h.to_bytes(4, byteorder='little')[::-1]
    message_data += clientIP_h_bytes
    message_data += clientIP_bytes

    # language --str
    language = ''.encode('utf-8')
    language_h = len(language)
    language_h_bytes = language_h.to_bytes(4, byteorder='little')[::-1]
    message_data += language_h_bytes
    message_data += language

    # unsupported  --str
    unsupported = 'unsupported'.encode('utf-8')
    unsupported_h = len(unsupported)
    unsupported_h_bytes = unsupported_h.to_bytes(4, byteorder='little')[::-1]
    message_data += unsupported_h_bytes
    message_data += unsupported

    #  忘了是啥了
    b = 0
    message_data += b.to_bytes(4, byteorder = 'little', signed = True)[::-1]

    # cn
    cn = 'cn'.encode('utf-8')
    cn_h = len(cn)
    cn_h_bytes = cn_h.to_bytes(4, byteorder='little')[::-1]
    message_data += cn_h_bytes
    message_data += cn

    # app_version
    app_version = '6874'.encode('utf-8')
    app_version_h = len(app_version)
    app_version_h_bytes = app_version_h.to_bytes(4, byteorder='little')[::-1]
    message_data += app_version_h_bytes
    message_data += app_version

    # 加密长度, 占一个字节
    encryption = 0
    encryption_h_bytes = encryption.to_bytes(1, byteorder='little')[::-1]

    # 消息长度
    message_data_length = len(message_data)
    message_data_length_bytes = message_data_length.to_bytes(4, byteorder='little')[::-1]

    # 组装消息 (加密 + 消息长度 + 消息体)
    message_data = encryption_h_bytes + message_data_length_bytes + message_data

    return message_data
















