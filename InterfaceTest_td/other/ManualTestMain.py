
import ClientMain
import pytest
import threading
import time
import json
import requests
import wx
import wx.lib.scrolledpanel as scrolled

# Pytest 接口测试框架管理
# 测试用例 默认使用 test_ 命名

def get_serverlist():
    server_num_list = []
    get_serverlist_url = 'http://gd-local-83.leishenhuyu.com/tank-global/index.php/?t=getserverlist&pid=cxk01&version=0'
    LastServerListResponse = requests.get(get_serverlist_url)
    LastServerListResponse = json.loads(LastServerListResponse.text)
    serverdict = LastServerListResponse['serverlist']
    for i in serverdict:
        server_num_list.append(str(i['zid']) + '//' + i['sname'])
    return  server_num_list


def UserLogin():
    pid = ''
    selected_item = ''
    def on_button_click(event):
        nonlocal pid, selected_item
        pid = text_ctrl.GetValue()
        selected_item = list_box.GetStringSelection().split('//')[0]
        print(selected_item)
        frame.Close()
    app = wx.App()
    frame = wx.Frame(None, title="登陆", size=(600, 400))
    panel = wx.Panel(frame)
    static_text = wx.StaticText(panel, label="PID  >>>:", pos=(22, 22))  # 设置静态文本的位置
    text_ctrl = wx.TextCtrl(panel, size=(300, -1), pos=(150, 20))  # 设置输入框的位置和大小
    sample_list = get_serverlist()
    list_box = wx.ListBox(panel, choices=sample_list, pos=(150, 60), size=(300, 230))
    list_box.SetSelection(0)
    button = wx.Button(panel, label="OK", pos=(250, 300))  # 设置按钮的位置
    button.Bind(wx.EVT_BUTTON, on_button_click)  # 绑定按钮事件
    frame.Show()
    app.MainLoop()
    return pid, selected_item

pid, server = UserLogin()


SendMain = ClientMain.Client(pid, server)
# 开启多线程
recv_data_thread = threading.Thread(target=SendMain.Recv_data)
recv_data_thread.start()

msg = ' {"cmd":"item.use","params":{"itemId":1633,"itemNum":1,"servantId":3001},"uid":67000351,"ts":2040503829,"logints":1416604224,"rnum":13,"zoneid":67,"access_token":"DQwNTAzODI5WVROaFppdGVtLnVzZUl5TkdJellqa3hZemRqWXp","clientts":2040503829}'

msg1 = '{"cmd":"item.getmodel","params":{"modelnames":[]},"uid":67000351,"ts":2040504835,"logints":1416604224,"rnum":28,"zoneid":67,"access_token":"DQwNTA0ODM1WVROaFppdGVtLmdldG1vZGVsSXlOR0l6WWpreFl","clientts":2040504835}'

def manual_useItem(msg):
    result = SendMain.SendMsg(msg)
    print(f'调用了test_useItem')
    return result


def manual_getItem(msg1):
    result = SendMain.SendMsg(msg1)
    print(f'调用了test_getItem')
    return result   




def on_search(event):
    search_text = search_ctrl.GetValue().lower()  # 获取搜索框中的文本，并转换为小写
    for button in buttons:
        if search_text in button.GetLabel().lower():  # 检查按钮的标签是否包含搜索文本
            button.Show()  # 如果匹配成功，显示按钮
        else:
            button.Hide()  # 如果不匹配，隐藏按钮

def button_click_test_useItem(event):
    button = event.GetEventObject()  # 获取触发事件的按钮 
    manual_useItem(msg)


def button_click_test_getItem(event):
    button = event.GetEventObject()
    manual_getItem(msg1)


app = wx.App()
frame = wx.Frame(None, title="接口测试", size=(400, 300))
outer_panel = wx.Panel(frame)  # 创建一个外部面板
outer_sizer = wx.BoxSizer(wx.VERTICAL)  # 外部垂直BoxSizer
outer_panel.SetSizer(outer_sizer)  # 将外部sizer设置为外部面板的sizer
# 创建顶部搜索栏
search_sizer = wx.BoxSizer(wx.HORIZONTAL)  # 水平BoxSizer
outer_sizer.Add(search_sizer, 0, wx.EXPAND)  # 添加搜索栏到外部sizer中
search_ctrl = wx.SearchCtrl(outer_panel)
search_ctrl.Bind(wx.EVT_TEXT, on_search)  # 绑定搜索框文本变化事件
search_sizer.Add(search_ctrl, 1, wx.EXPAND | wx.ALL, 5)  # 将搜索栏添加到水平sizer中
# 创建滚动面板并添加到外部面板中
scroll_panel = scrolled.ScrolledPanel(outer_panel, style=wx.VSCROLL)
scroll_panel.SetupScrolling()
scroll_sizer = wx.BoxSizer(wx.VERTICAL)  # 滚动面板的垂直BoxSizer
scroll_panel.SetSizer(scroll_sizer)  # 将滚动面板的sizer设置为scroll_sizer
outer_sizer.Add(scroll_panel, 1, wx.EXPAND | wx.ALL, 5)  # 将滚动面板添加到外部sizer中

# 按钮搜索列表
buttons = []

test_useItem_button = wx.Button(scroll_panel, label='test_useItem')
test_useItem_button.Bind(wx.EVT_BUTTON, button_click_test_useItem)  
scroll_sizer.Add(test_useItem_button, 0, wx.EXPAND | wx.ALL, 5)  
buttons.append(test_useItem_button)

test_getItem_button = wx.Button(scroll_panel, label='test_getItem')
test_useItem_button.Bind(wx.EVT_BUTTON, button_click_test_getItem)  
scroll_sizer.Add(test_getItem_button, 0, wx.EXPAND | wx.ALL, 5)
buttons.append(test_getItem_button)  


frame.Show()
app.MainLoop()
