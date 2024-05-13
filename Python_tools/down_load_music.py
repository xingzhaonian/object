import requests
url = 'https://dl.stream.qqmusic.qq.com/C400000y39oA2VspA4.m4a?guid=8158688256&vkey=8616A5F3E5201A5554FB1DE1E8ABCA782FCF62E5FFA13B598A302BB30D83BFC939D6FCB882EE7CCB31857024654EF8230E3EE5E1EAC8A9F5&uin=&fromtag=120032'
def down_load_music(url):
    headers_info = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'}
    res = requests.get(url, headers = headers_info, timeout = 30)
    print('请求结果', type(res), res)
    data = res.content
    print(data, '类型:', type(data))
    music = open('D:\\Project\\music\\可能-程响.mp3', 'wb')
    music.write(data)
down_load_music(url)