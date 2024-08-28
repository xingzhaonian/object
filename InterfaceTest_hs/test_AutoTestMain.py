import ClientMain
import pytest
import threading
import load_data.load_message
import json
import easygui


# 初始化玩家相关数据
def user_data():
    msg = "请输入Pid和服务器(服务器为数字):"
    field_names = ["PID", "SERVER"]
    pid, server_id = easygui.multenterbox(msg, "接口测试", field_names)
    while True:
        try:
            server_id = int(server_id)
            break
        except:
            msg = '服务器输入错误, 服务器应该为数字'
            pid, server_id = easygui.multenterbox(msg, "接口测试", field_names)
    return pid, server_id

pid, server_id = user_data()
clientmain = ClientMain.Client(pid, int(server_id))
token, uid, logints = clientmain.GetAccessToken()

# 加载子线程
recv_data_thread = threading.Thread(target=clientmain.Recv_data)
recv_data_thread.start()


# Pytest环境下, 默认读取test开头的函数为测试用例

# Pytest环境下, 对于参数化的处理, 用mark装饰器



# 道具使用
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\\InterfaceTest\\message_config\\useItem_1216.yaml'))
def test_useItem_1216(msg):
    msg['Messagedata']['uid'] = uid
    msg['Messagedata']['ts'] = logints
    msg['Messagedata']['logints'] = logints
    msg['Messagedata']['zoneid'] = server_id
    msg['Messagedata']['access_token'] = token
    msg['Messagedata']['clientts'] = logints
    print('发送的消息===============', msg['Messagedata'],'\n')
    result = json.loads(clientmain.SendMsg(msg['Messagedata']))
    print('返回的消息===============', type(result), result)
    assert result['ret'] == msg['ret']


# 促织升级
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\\InterfaceTest\\message_config\\crickets_uplv.yaml'))
def test_crickets_uplv(msg):
    msg['Messagedata']['uid'] = uid
    msg['Messagedata']['ts'] = logints
    msg['Messagedata']['logints'] = logints
    msg['Messagedata']['zoneid'] = server_id
    msg['Messagedata']['access_token'] = token
    msg['Messagedata']['clientts'] = logints
    print('发送的消息===============', msg['Messagedata'],'\n')
    result = json.loads(clientmain.SendMsg(msg['Messagedata']))
    print('返回的消息===============', type(result), result)
    assert result['ret'] == msg['ret']


# 书院增加时长
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\\InterfaceTest\\message_config\\bookroom_extendpos.yaml'))
def test_bookroom_extendpos(msg):
    msg['Messagedata']['uid'] = uid
    msg['Messagedata']['ts'] = logints
    msg['Messagedata']['logints'] = logints
    msg['Messagedata']['zoneid'] = server_id
    msg['Messagedata']['access_token'] = token
    msg['Messagedata']['clientts'] = logints
    print('发送的消息===============', msg['Messagedata'],'\n')
    result = json.loads(clientmain.SendMsg(msg['Messagedata']))
    print('返回的消息===============', type(result), result)
    assert result['ret'] == msg['ret']


# 大航海获取地图数据
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\\InterfaceTest\\message_config\\navigation_getmap.yaml'))
def test_navigation_getmap(msg):
    msg['Messagedata']['uid'] = uid
    msg['Messagedata']['ts'] = logints
    msg['Messagedata']['logints'] = logints
    msg['Messagedata']['zoneid'] = server_id
    msg['Messagedata']['access_token'] = token
    msg['Messagedata']['clientts'] = logints
    print('发送的消息===============', msg['Messagedata'],'\n')
    result = json.loads(clientmain.SendMsg(msg['Messagedata']))
    print('返回的消息===============', type(result), result)
    assert result['ret'] == msg['ret']


# 大航海移动
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\\InterfaceTest\\message_config\\navigation_move.yaml'))
def test_navigation_move(msg):
    msg['Messagedata']['uid'] = uid
    msg['Messagedata']['ts'] = logints
    msg['Messagedata']['logints'] = logints
    msg['Messagedata']['zoneid'] = server_id
    msg['Messagedata']['access_token'] = token
    msg['Messagedata']['clientts'] = logints
    print('发送的消息===============', msg['Messagedata'],'\n')
    result = json.loads(clientmain.SendMsg(msg['Messagedata']))
    print('返回的消息===============', type(result), result)
    assert result['ret'] == msg['ret']


# 炼金工坊
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\\InterfaceTest\\message_config\\alchemy_Opt.yaml'))
def test_alchemy_Opt(msg):
    msg['Messagedata']['uid'] = uid
    msg['Messagedata']['ts'] = logints
    msg['Messagedata']['logints'] = logints
    msg['Messagedata']['zoneid'] = server_id
    msg['Messagedata']['access_token'] = token
    msg['Messagedata']['clientts'] = logints
    print('发送的消息===============', msg['Messagedata'],'\n')
    result = json.loads(clientmain.SendMsg(msg['Messagedata']))
    print('返回的消息===============', type(result), result)
    assert result['ret'] == msg['ret']


# 炼金工坊
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\\InterfaceTest\\message_config\\alchemy_GetProgressReward.yaml'))
def test_alchemy_GetProgressReward(msg):
    msg['Messagedata']['uid'] = uid
    msg['Messagedata']['ts'] = logints
    msg['Messagedata']['logints'] = logints
    msg['Messagedata']['zoneid'] = server_id
    msg['Messagedata']['access_token'] = token
    msg['Messagedata']['clientts'] = logints
    print('发送的消息===============', msg['Messagedata'],'\n')
    result = json.loads(clientmain.SendMsg(msg['Messagedata']))
    print('返回的消息===============', type(result), result)
    assert result['ret'] == msg['ret']
    

# 三国争霸
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\\InterfaceTest\\message_config\\threekingdomsnew_bm.yaml'))
def test_threekingdomsnew_bm(msg):
    msg['Messagedata']['uid'] = uid
    msg['Messagedata']['ts'] = logints
    msg['Messagedata']['logints'] = logints
    msg['Messagedata']['zoneid'] = server_id
    msg['Messagedata']['access_token'] = token
    msg['Messagedata']['clientts'] = logints
    print('发送的消息===============', msg['Messagedata'],'\n')
    result = json.loads(clientmain.SendMsg(msg['Messagedata']))
    print('返回的消息===============', type(result), result)
    assert result['ret'] == msg['ret']


#  咸鱼宝箱抽奖
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\InterfaceTest\\message_config\\saltyFishBox.yaml'))
def sfboxopenreward_1(msg):
    msg['Messagedata']['uid'] = uid
    msg['Messagedata']['ts'] = logints
    msg['Messagedata']['logints'] = logints
    msg['Messagedata']['zoneid'] = server_id
    msg['Messagedata']['access_token'] = token
    msg['Messagedata']['clientts'] = logints
    print('发送的消息===============', msg['Messagedata'],'\n')
    result = json.loads(clientmain.SendMsg(msg['Messagedata']))
    print('返回的消息===============', type(result), result)
    assert result['ret'] == msg['ret']


# 文玩
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\InterfaceTest\\message_config\\curiosadventure_attack.yaml'))
def curiosadventure_attack(msg):
    msg['Messagedata']['uid'] = uid
    msg['Messagedata']['ts'] = logints
    msg['Messagedata']['logints'] = logints
    msg['Messagedata']['zoneid'] = server_id
    msg['Messagedata']['access_token'] = token
    msg['Messagedata']['clientts'] = logints
    for i in range(851):
        print('发送的消息===============', msg['Messagedata'],'\n')
        result = json.loads(clientmain.SendMsg(msg['Messagedata']))
        print('返回的消息===============', type(result), result)
        assert result['ret'] == msg['ret']


# 红颜宠幸
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\InterfaceTest\\message_config\\wife_love.yaml'))
def wife_love(msg):
    msg['Messagedata']['uid'] = uid
    msg['Messagedata']['ts'] = logints
    msg['Messagedata']['logints'] = logints
    msg['Messagedata']['zoneid'] = server_id
    msg['Messagedata']['access_token'] = token
    msg['Messagedata']['clientts'] = logints
    count = input('宠幸次数')
    for i in range(int(count)):
        print('发送的消息===============', msg['Messagedata'],'\n')
        result = json.loads(clientmain.SendMsg(msg['Messagedata']))
        print('返回的消息===============', type(result), result)
        assert result['ret'] == msg['ret']


# 子嗣拜访
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\InterfaceTest\\message_config\\sadun_visit.yaml'))
def sadun_visit(msg):
    msg['Messagedata']['uid'] = uid
    msg['Messagedata']['ts'] = logints
    msg['Messagedata']['logints'] = logints
    msg['Messagedata']['zoneid'] = server_id
    msg['Messagedata']['access_token'] = token
    msg['Messagedata']['clientts'] = logints
    print('发送的消息===============', msg['Messagedata'],'\n')
    result = json.loads(clientmain.SendMsg(msg['Messagedata']))
    print('返回的消息===============', type(result), result)
    assert result['ret'] == msg['ret']

