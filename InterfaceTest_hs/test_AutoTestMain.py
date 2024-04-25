import ClientMain
import pytest
import threading
import load_data.load_message
import json


# 初始化玩家相关数据
pid = 'cxk01'
server_id = 67

clientmain = ClientMain.Client(pid, server_id)
token, uid, logints = clientmain.GetAccessToken()

# 加载子线程
recv_data_thread = threading.Thread(target=clientmain.Recv_data)
recv_data_thread.start()


# Pytest环境下, 默认读取test开头的函数为测试用例

# Pytest环境下, 对于参数化的处理, 用mark装饰器

@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\\InterfaceTest\\message_config\\useItem_1216.yaml'))
def test_useItem_1216(msg):
    msg['Messagedata']['uid'] = uid
    msg['Messagedata']['ts'] = logints
    msg['Messagedata']['logints'] = logints
    msg['Messagedata']['zoneid'] = server_id
    msg['Messagedata']['access_token'] = token
    msg['Messagedata']['clientts'] = logints
    print('发送的消息===============', msg['Messagedata'])
    result = json.loads(clientmain.SendMsg(msg['Messagedata']))
    print('返回的消息===============', type(result), result)
    assert result['ret'] == msg['ret']





