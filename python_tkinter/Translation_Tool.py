import tkinter
import tkinter.ttk
import requests


class Translation(object):

    def __init__(self, window) -> None:
        self.window = window
        self.window.title('翻译工具')
        self.window.geometry('800x600+700+250')
        self.option = ['中文', '英语', '日语', '韩语', '法语', '德语', '西班牙语', '意大利语', '葡萄牙语', '俄语', '阿拉伯语', '泰语', '越南语', '印地语', '土耳其语', '马来语', '荷兰语', '希腊语', '瑞典语', '芬兰语', '丹麦语', '波兰语', '匈牙利语', '捷克语', '罗马尼亚语', '印尼语', '希伯来语', '塞尔维亚语']
        self.combobox = tkinter.ttk.Combobox(self.window, values=self.option)
        self.combobox.current(0)
        self.combobox.pack(pady=10)
        self.combobox.bind("<<ComboboxSelected>>", self.choice_language)
        self.label = 





    def choice_language(self, event):
        self.selected_result = self.combobox.get()
        print(self.selected_result)


    def Translate(self):
        self.post_url = 'https://fanyi.baidu.com/sug'
        # 设置请求头, 模拟浏览器身份访问
        self.request_headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            "Content-Type":"application/json",
            "Content-Type": "application/json"
        }
        self.words = input('输入要翻译的内容>>>')

        #表单数据
        self.form_data = {'kw': self.words}

        #网页请求
        self.resp = requests.post(url=self.post_url, data=self.form_data, headers=self.request_headers)

        # 获取翻译结果
        print(self.resp.json())
        return self.resp.json()

    
    def click_translate(self):
        self.Translate()



def RunTranslationTool() -> None:
    window = tkinter.Tk()
    Translation(window)
    window.mainloop()

RunTranslationTool()
