import requests
url = 'https://dl.stream.qqmusic.qq.com/C400000y39oA2VspA4.m4a?guid=5703167320&vkey=2B8A3DEC13E7006E8B1DD032D480F38DA3B155B6B4939E9D70B8613C0EF0C3AD4C01FD4442D37199BC75A06760CA14D06FF3D6A0BDF5AE4A&uin=&fromtag=120032'
def down_load_music(url):
    headers_info = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'}
    res = requests.get(url, headers = headers_info, timeout = 30)
    print('请求结果', type(res), res)
    data = res.content
    print(data, '类型:', type(data))
    music = open('D:\\Project\\music\\蔚蓝海岸.mp3', 'wb')
    music.write(data)
down_load_music(url)