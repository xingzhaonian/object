import lxml
import lxml.etree
import requests


def down_load_music():
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }

    singer_url = 'https://music.163.com/artist?id=2116'
    # 请求歌手歌单页面
    respones = requests.get(url=singer_url, headers=header)

    count = 0
    # 筛选音乐标签数据
    doc = lxml.etree.HTML(respones.text)
    music_list = (doc.xpath('//a[contains(@href,"/song?")]'))
    for i in music_list:
        href = (i.xpath('./@href')[0])
        music_id = href.split('=')[1]
        music_name = i.xpath('./text()')
        
        if music_name:
            if '!' in music_name[0] or '{' in music_name[0] or '$' in music_name[0]:
                continue
            else:
                count += 1
                print(music_name[0] + music_id, count)
                
                music_url = 'http://music.163.com/song/media/outer/url?id=' + music_id
                print(music_url)
                music = requests.get(music_url, header)
                try:
                    with open('D:\\music\\' + music_name[0] + '.mp3', 'wb') as f:
                        f.write(music.content)
                        print(music.content)
                except:
                    continue

down_load_music()





