
import sync_websocket_client
import pytest
import threading
import time

# Pytest 接口测试框架管理
# 测试用例 默认使用 test_ 命名

SendMain = sync_websocket_client.ClientMain()
recv_data_thread = threading.Thread(target=SendMain.recv_data)
recv_data_thread.start()


msg1 = {
    'MsgId':10001,
    'Account':'admim',
    'password':123456
}
msg2 = {
    'MsgId':10001,
    'Account':'admin',
    'password':123446
}
msg3 = {
    'MsgId':10001,
    'Account':'admin',
    'password':123456
}



def test_account(msg):
    result = SendMain.AccountVerification(msg)
    return result

masg1 = test_account(msg1)
print(masg1)

masg2 = test_account(msg2)
print(masg2)

masg3 = test_account(msg3)
print(masg3)
