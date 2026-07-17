import ClientMain
import pytest
import threading
import load_data.load_message
import json
import easygui
import time
import GmTools

log_file_Path = 'D:\\' + 'BatchLoginLog.txt'
open(log_file_Path,'w').close()

login_msg = [{"cmd":"acterrioty.yyattack","params":{"activeId":"teYanyun-1","cityId":"411"},"uid":78000011,"ts":1974263721,"logints":1953130204,"rnum":28,"zoneid":78,"access_token":"Tc0MjYzNzIxTW1aaFlhY3RlcnJpb3R5Lnl5YXR0YWNrWTFZVGx","clientts":1974263721}]


user_pid_list = ['cxk01', 'cxk01_1', 'cxk01_2', 'cxk01_3', 'cxk01_4', 'cxk01_5', \
                 'cxk02', 'cxk02_1', 'cxk02_2', 'cxk02_3', 'cxk02_4', 'cxk02_5', \
                 'cxk03', 'cxk03_1', 'cxk03_2', 'cxk03_3', 'cxk03_4', 'cxk03_5', \
                 'cxk04', 'cxk04_1', 'cxk04_2', 'cxk04_3', 'cxk04_4', 'cxk04_5', \
                 'test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9', 'test10',\
                 'topatk01', 'atk01']


user_pid_list_1 = ['test8', 'test18', 'test28', 'test38', 'test48', 'test10', 'test20', 'test30', 'test40', 'test50']


# 获取test1-test100的pid列表
g = GmTools.GmTools()
user_pid_list_2 = g.creat_pid_list('test1')
#user_pid_list_2.extend(user_pid_list)


server_list = [ 81]
def batch_login(user_list, server_list, msg_list):
    for each_server in server_list:
        if each_server == 81:
            user_list = ['test2', 'test12', 'test22', 'test32'] 
        #if each_server == 78:
        #    user_list = ['test7', 'test17', 'test27', 'test37']
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
                print(return_msg)
                #print('\n')
                #with open(log_file_Path , 'a+', encoding='utf-8') as f:
                #    f.write(str(ts) + str(return_msg['data']['userinfo']))
                #    f.write('\n')
            recv_data_thread.stop()
            print(f'当前线程id--->{threading.get_ident()},线程总数量--->{threading.active_count()},所有线程--->{threading.enumerate()}', '\n')
    #print('======================登录完毕=============================')
    recv_data_thread.stop()
    return token, uid, logints

 
batch_login(user_pid_list_1, server_list, login_msg)