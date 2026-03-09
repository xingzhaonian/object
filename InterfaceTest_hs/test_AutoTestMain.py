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
recv_data_thread = ClientMain.StoppableThread(clientmain.Recv_data)
recv_data_thread.start()


# Pytest环境下, 默认读取test开头的函数为测试用例

# Pytest环境下, 对于参数化的处理, 用mark装饰器



# 道具使用
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\\InterfaceTest\\message_config\\useItem_1216.yaml'))
def useItem_1216(msg):
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
def test_sfboxopenreward_1(msg):
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
def test_curiosadventure_attack(msg):
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
def test_sadun_visit(msg):
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


# 升级刘禅门客的全资质光环   aura_id :5    1000级
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\InterfaceTest\\message_config\\servant_upaura_2199_5.yaml'))
def servant_upaura_2199_5(msg):
    for i in range(900):
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



# 升级刘禅门客的全资质光环   aura_id :6   100级
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\InterfaceTest\\message_config\\servant_upaura_2199_6.yaml'))
def servant_upaura_2199_6(msg):
    for i in range(80):
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

# 升级孟获门客的资质性光环   aura_id :5   1000级
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\InterfaceTest\\message_config\\servant_upaura_2203_5.yaml'))
def servant_upaura_2203_5(msg):
    for i in range(990):
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


# 升级孟获门客的全资质光环   aura_id :6   100级
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\InterfaceTest\\message_config\\servant_upaura_2203_6.yaml'))
def servant_upaura_2203_6(msg):
    for i in range(90):
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



# 升级孟获门客的全属性光环   aura_id :6   1000级
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\InterfaceTest\\message_config\\servant_upaura_2203_8.yaml'))
def servant_upaura_2203_8(msg):
    for i in range(950):
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




# 升级息夫人红颜的亲密, 魅力, 才艺光环 1   (300级)
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\InterfaceTest\\message_config\\wife_upaura1.yaml'))
def wife_upaura1(msg):
    for i in range(280):
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


# 升级息夫人红颜的亲密, 魅力, 才艺光环 2  (1000级)
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\InterfaceTest\\message_config\\wife_upaura2.yaml'))
def wife_upaura2(msg):
    for i in range(980):
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



# 升级战马戍荒麟(4051)的资质光环5(100级)
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\InterfaceTest\\message_config\\warhorse_upssaura5.yaml'))
def warhorse_upssaura5(msg):
    for i in range(90):
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



# 升级战马戍荒麟(4051)的资质光环6(100级)
@pytest.mark.parametrize('msg', load_data.load_message.load('O:\\皇上快点_测试\InterfaceTest\\message_config\\warhorse_upssaura6.yaml'))
def warhorse_upssaura6(msg):
    for i in range(990):
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