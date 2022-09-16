import requests

'''def down_load_music(url):
    res = requests.get(url)'''

url = 'http://www.baidu.com'

headers_info = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'}

res = requests.get(url, headers = headers_info, timeout = 30)

print('请求结果', type(res), res)
data = res.content
print(data, '类型:', type(data))

#music = open('D:\\Project\\object\\music\\蔚蓝海岸.mp3', 'wb')
#music.write(data)
