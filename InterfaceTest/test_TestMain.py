
import sync_websocket_client
import pytest
import threading
import time
import load_data.yaml_load

# Pytest 接口测试框架管理
# 测试用例 默认使用 test_ 命名

SendMain = sync_websocket_client.ClientMain()

# 开线程接收数据
recv_data_thread = threading.Thread(target=SendMain.recv_data)
recv_data_thread.start()


# Pytest环境下, 默认读取test开头的函数为测试用例

# Pytest环境下, 对于参数化的处理, 用mark装饰器

@pytest.mark.parametrize('data', load_data.yaml_load.load('D:\\PythonProject\\InterfaceTest\\message_config\\user.yaml'))
def test_account01(data):
    result = SendMain.SendMessage(data['user'])
    msg = result[:5]
    assert msg == data['msg']


@pytest.mark.parametrize('data', load_data.yaml_load.load('D:\\PythonProject\\InterfaceTest\\message_config\\user.yaml'))
def test_account02(data):
    result = SendMain.SendMessage(data['user'])
    msg = result[:5]
    assert msg == data['msg']

