import requests

#def down_load_music(url):
 #   res = requests.get(url)

url = 'https://dl.stream.qqmusic.qq.com/C40000314al43aw2Yj.m4a?guid=921602479&vkey=B7BA376C17F5AAC1893C133058E8AF1A8F0 \
    42C9B2685E83F4DE33B125E0ABC24B336FD8C8A138E989E40E0B6C94A9880E040A9BBDAB8C125&uin=&fromtag=120002'

headers_info = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'}



res = requests.get(url, headers = headers_info, timeout = 30)
print('请求结果', res)
data = res.content
print(data)
music = open('D:\\Project_Flie\\object\\music\\蔚蓝海岸.mp3', 'wb')
music.write(data)
