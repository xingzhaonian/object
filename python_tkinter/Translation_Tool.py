import tkinter
import tkinter.ttk
import requests
import time
import random

class Translation(object):

    def __init__(self, window) -> None:
        self.window = window
        self.window.title('翻译工具')
        self.window.geometry('800x600+700+250')
        self.option_list = [
            '中文',
            '英语',
            '日语',
            '韩语',
            '法语',
            '德语',
            '西班牙语',
            '意大利语',
            '葡萄牙语',
            '俄语',
            '阿拉伯语',
            '泰语',
            '越南语',
            '印地语',
            '土耳其语',
            '马来语',
            '荷兰语',
            '希腊语',
            '瑞典语',
            '芬兰语',
            '丹麦语',
            '波兰语',
            '匈牙利语',
            '捷克语',
            '罗马尼亚语',
            '印尼语',
            '希伯来语',
            '塞尔维亚语'
        ]
        self.option = {
    '中文': 'ZH',
    '英语': 'EN',
    '日语': 'JA',
    '韩语': 'KO',
    '法语': 'FR',
    '德语': 'DE',
    '西班牙语': 'ES',
    '意大利语': 'IT',
    '葡萄牙语': 'PT',
    '俄语': 'RU',
    '阿拉伯语': 'AR',
    '泰语': 'TH',
    '越南语': 'VI',
    '印地语': 'HI',
    '土耳其语': 'TR',
    '马来语': 'MS',
    '荷兰语': 'NL',
    '希腊语': 'EL',
    '瑞典语': 'SV',
    '芬兰语': 'FI',
    '丹麦语': 'DA',
    '波兰语': 'PL',
    '匈牙利语': 'HU',
    '捷克语': 'CS',
    '罗马尼亚语': 'RO',
    '印尼语': 'ID',
    '希伯来语': 'HE',
    '塞尔维亚语': 'SR'
        }
        self.combobox = tkinter.ttk.Combobox(self.window, values=self.option_list)
        self.combobox.pack(pady=10)
        self.combobox.bind("<<ComboboxSelected>>", self.choice_language)
        self.start_btn = tkinter.Button(self.window, command=self.click_translate, width=6, height=1, text='开始翻译')
        self.start_btn.pack()
        self.source_language = tkinter.Text(self.window, wrap=tkinter.WORD, width=30, height=20, font=('SimHei', 15))
        self.source_language.place(x=10, y=100)
        self.combobox.current(0)
        self.selected_result = self.option_list[0]



    def choice_language(self, event):
        
        self.selected_result = self.combobox.get()

    
    def Generateid(self, n):
        return int(random.randint(10**(n-1), 10**n - 1))


    def Translate(self):
        self.post_url = 'https://www2.deepl.com/jsonrpc?method=LMT_handle_jobs'
        self.post_headers ={
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            "Content-Type":"application/json",
            "Content-Type": "application/json",
        }

    
        self.tamptime = int(time.time() * 1000)
        self.words = ''


        self.payload = {
            "jsonrpc": "2.0",
            "method": "LMT_handle_jobs",
            "params": {
                "jobs": [
                    {
                        "kind": "default",
                        "sentences": [
                            {
                                "text": "你好",  # 要翻译的文本
                                "id": 1,
                                "prefix": ""
                            }
                        ],
                        "raw_en_context_before": [],
                        "raw_en_context_after": [],
                        "preferred_num_beams": 4
                    }
                ],
                "lang": {
                    "target_lang": 'CN',  # 目标语言：英语
                    "preference": {
                        "weight": {},
                        "default": "default"
                    },
                    "source_lang_computed": 'ZH'# 源语言：中文
                },
                "priority": -1,
                "commonJobParams": {
                    "quality": "fast",
                    "regionalVariant": "en-US",
                    "mode": "translate",
                    "browserType": 1,
                    "textType": "plaintext"
                },
                "timestamp": self.tamptime  # 使用当前时间戳
            },
            "id": self.Generateid(8)
        }

        self.response = requests.post(url=self.post_url, headers=self.post_headers, json=self.payload)


    def click_translate(self):
        print(self.selected_result, self.source_language)



def RunTranslationTool() -> None:
    window = tkinter.Tk()
    Translation(window)
    window.mainloop()

RunTranslationTool()
