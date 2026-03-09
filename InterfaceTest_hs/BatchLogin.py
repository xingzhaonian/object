import ClientMain
import pytest
import threading
import load_data.load_message
import json
import easygui
import time



login_msg = [{"cmd":"user.login","params":{"plat":"","enter":True,"packageVersion":"0","idcardinfo":{"switch":0,"normal":0,"usertype":"0","enternormal":0},"bindtype":"Android","language":"cn","serverip":"192.168.8.196","serverport":15011,"nomodel":4,"client_ip":"103.216.43.176","pid":"cxk02_3"},"uid":80000287,"ts":1760393643,"logints":1760393643,"rnum":1,"zoneid":80,"access_token":"zYwMzkzNjQzWVRJMU51c2VyLmxvZ2luYzBaVFF5TWpCaU5ESTV","clientts":1760393643}]


user_pid_list = ['cxk01', 'cxk01_1', 'cxk01_2', 'cxk01_3', 'cxk01_4', 'cxk01_5', \
                 'cxk02', 'cxk02_1', 'cxk02_2', 'cxk02_3', 'cxk02_4', 'cxk02_5', \
                 'cxk03', 'cxk03_1', 'cxk03_2', 'cxk03_3', 'cxk03_4', 'cxk03_5', \
                 'cxk04', 'cxk04_1', 'cxk04_2', 'cxk04_3', 'cxk04_4', 'cxk04_5', \
                 'test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9', 'test10',\
                 'topatk01', 'atk01']


user_pid_list_1 = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9', 'test10']


server_list = [91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111]

def batch_login(user_list, server_list, msg_list):
    for each_server in server_list:
        for each_user in user_list:
            clientmain = ClientMain.Client(each_user, each_server)

            # 不进行服务器ip和端口的重复获取了, 在 Client中已经获取过了, 这里消息体内的端口不起作用
            #server_port = clientmain.ServerInfo(each_server)['port_server']
            #ip_server = clientmain.ServerInfo(each_server)['ip_server']
            recv_data_thread = ClientMain.StoppableThread(clientmain.Recv_data)
            recv_data_thread.start()
            token, uid, logints = clientmain.GetAccessToken()
            for each_msg in msg_list:
                each_msg['uid'] = uid
                each_msg['zoneid'] = each_server
                each_msg['params']['pid'] = each_user
                #each_msg['params']['serverport'] = server_port
                #each_msg['params']['serverip'] = ip_server
                return_msg = clientmain.SendMsg(each_msg)
                return_msg = json.loads(return_msg)
                ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(return_msg['ts']))
                print(f'uid:{return_msg["uid"]}, zoneid:{return_msg["zoneid"]}, ts:{ts}, msg:{return_msg}')
            recv_data_thread.stop()
            print(f'当前线程id--->{threading.get_ident()},线程总数量--->{threading.active_count()},所有线程--->{threading.enumerate()}', '\n')
    print('======================登录完毕=============================')
    recv_data_thread.stop()
    return token, uid, logints


batch_login(user_pid_list_1, server_list, login_msg)