r'''
0. 请改进课堂中的代码,实现双重加密(先执行凯撒加密,再执行莫斯加密)
举个例子,比如明文 I love FishC,执行凯撒加密(正向位移 6 位)后的结果是 O rubk LoynI,接着再执行莫斯加密,结果就是 --- .-. ..- -... -.- .-.. --- -.-- -. ..
'''
plaintext_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
need_cipher_text = input('请输入需要加密的明文')
move_step = int(input('请输入需要移动的位数'))
if move_step >= 26:
    print('数字过大, 无效')
    exit()
result_cipher_text = ''
print(need_cipher_text)
for i in need_cipher_text:
    if i == ' ':
        result_cipher_text += i
    need_cipher_text_position = plaintext_table.find(i)
    for k in range(len(plaintext_table)):
        if need_cipher_text_position + move_step + 1 > 52:
            need_cipher_text_position = need_cipher_text_position - 26
        if int(need_cipher_text_position) == k:
            i = plaintext_table[k + move_step: k + move_step + 1]
            result_cipher_text += i
print(result_cipher_text)

c_table = ['·-', '-···','-·-·', '-··', '·', '··-·', '--·', '····', '··', '·---', '-·-', '·-··',\
           '--', '-·', '---', '·--·', '--·-', '·-·', '···', '-', '··-', '···-', '·--', '-··-',\
            '-·--', '--··', '·----', '··---', '···--', '····-', '·····', '-····', '--···', '---··',\
                '----·', '-----']

d_table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'G', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',\
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

Morse_Code = []
for i in result_cipher_text:
    i = i.upper()
    if i == ' ':
        Morse_Code.append(i)
    else:
        Morse_Code.append(c_table[d_table.index(i)])
for i in Morse_Code:
    if i == ' ':
        continue
    else:        
        print(i, end = ', ')

# 1. 请使用学过的知识，编写一个存储电影数据的小程序
'''
需要存放的数据如下：
电影名称
上映时间
导演（可能有多人）
主演（通常有多人）
电影评分
'''
