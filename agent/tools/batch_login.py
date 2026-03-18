# tools/login_tools.py
import sys
import time
from pathlib import Path
import json
import threading

class LoginTools:
    """批量登录工具"""
    
    def __init__(self):
        # 在这里添加你的模块路径
        self.module_path = r"D:\project\python_InterfaceTest_hs"  # 改成你的实际路径
        if self.module_path not in sys.path:
            sys.path.insert(0, self.module_path)
        

        self.login_msg = [{"cmd":"user.login","params":{"plat":"","enter":True,"packageVersion":"0","idcardinfo":{"switch":0,"normal":0,"usertype":"0","enternormal":0},"bindtype":"Android","language":"cn","serverip":"192.168.8.196","serverport":15011,"nomodel":4,"client_ip":"103.216.43.176","pid":"cxk02_3"},"uid":80000287,"ts":1760393643,"logints":1760393643,"rnum":1,"zoneid":80,"access_token":"zYwMzkzNjQzWVRJMU51c2VyLmxvZ2luYzBaVFF5TWpCaU5ESTV","clientts":1760393643}]
        # 尝试导入你的登录模块
        try:
            global ClientMain, load_data
            import ClientMain
            import load_data.load_message
            self.client_available = True
            print("✅ 登录模块导入成功")
        except ImportError as e:
            print(f"⚠️ 登录模块导入失败: {e}")
            self.client_available = False
    
    def batch_login(self, servers: list, users: list):
        """
        批量登录
        Args:
            servers: 服务器列表，如 [67, 68]
            users: 用户名列表，如 ['cxk04', 'cxk03']
        """
        if not self.client_available:
            return f"[模拟] 登录服务器 {servers}，用户 {users}"
        
        # ===== 在这里填入你的实际登录代码 =====
        # 参考你之前的 batch_login 函数
        
        results = []
        for each_server in servers:
            for each_user in users:
                try:
                    # 你的登录逻辑
                    clientmain = ClientMain.Client(each_user, each_server)
                    # 不进行服务器ip和端口的重复获取了, 在 Client中已经获取过了, 这里消息体内的端口不起作用
                    #server_port = clientmain.ServerInfo(each_server)['port_server']
                    #ip_server = clientmain.ServerInfo(each_server)['ip_server']
                    recv_data_thread = ClientMain.StoppableThread(clientmain.Recv_data)
                    recv_data_thread.start()
                    token, uid, logints = clientmain.GetAccessToken()
                    for each_msg in self.login_msg:
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
                    results.append(f"✅ {each_user}@{each_server} 登录成功")
                    time.sleep(0.1)  # 避免请求太快
                except Exception as e:
                    results.append(f"❌ {each_user}@{each_server} 登录失败: {e}")
        
        return f"批量登录完成:\n" + "\n".join(results)
    
    def login_test_users(self, servers: list):
        """登录测试用户"""
        test_users = [f"test{i}" for i in range(1, 11)]
        return self.batch_login(servers, test_users)