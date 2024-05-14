import GC_Message.Deserialize

def deserialize_draw_card(message_data):
    drawcard_info = GC_Message.Deserialize.Analysis(message_data)
    encryptionid = drawcard_info.GetBytes()
    serial = drawcard_info.GetInt()
    msg_length  = drawcard_info.GetInt()
    msgId = drawcard_info.GetInt()
    msgIncreaseNum = drawcard_info.GetBytes()
    errorCode = drawcard_info.GetInt()
    draw_Type = drawcard_info.GetInt()
    draw_num = drawcard_info.GetInt()
    reward_list = drawcard_info.ItemBean()
    draw_times = drawcard_info.RewardTimes()
    free_cool_down = drawcard_info.RewardCd()
    safe_times = drawcard_info.SafeTimes()
    return msgId, errorCode, draw_Type, draw_num, reward_list, draw_times, free_cool_down, safe_times


