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
print('欢迎进入鱼C影评小程序')
print('输入 1 进行数据录入')
print('输入 2 进行数据查询')
print('输入 3 退出程序')
Movie_Name_List = []
Release_Time_List = []
Direct_Name_List = []
Leading_Role_List = []
Movie_Grade_List = []
is_continue_inquire_about = True
while True:
    choice = input('请输入想要的功能(1:进行数据录入 / 2:进行数据查询 / 3:退出程序):')
    if choice.isspace():
        print('输入为空, 请再次输入')
        continue
    if choice.isdecimal():
        if int(choice) == 1:
            while is_continue_inquire_about:
                print('进行录入选项')
                movie_name = input('请输入电影名称:')
                Movie_Name_List.append(movie_name)
                Release_Time = input('请输入上映日期:')
                Release_Time_List.append(Release_Time)
                direct_name = input('请输入导演名字(多人请用" / "分隔):')
                Direct_Name_List.append(direct_name)
                lading_role_name = input('请输入主演名字(多人请用" / "分隔):')
                Leading_Role_List.append(lading_role_name)
                movie_grade = input('请输入电影评分:')
                Movie_Grade_List.append(movie_grade)
                is_continue_inquire_about = input('请问是否继续录入(Y/N):')
                if is_continue_inquire_about == 'Y':
                    is_continue_inquire_about = True
                elif is_continue_inquire_about == 'N':
                    is_continue_inquire_about = False
                else:
                    while True:
                        is_continue_inquire_about = input('请输入(Y/N)来判断是否进行继续录入:')
                        if is_continue_inquire_about == 'Y':
                            is_continue_inquire_about = True
                            break
                        elif is_continue_inquire_about == 'N':
                            is_continue_inquire_about = False
                            break
                        else:
                            continue
        elif int(choice) == 2:
            print('进行查询选项')
            select_movie_name = input('请输入电影名称:')
            if select_movie_name in Movie_Name_List:
                movie_name_index = Movie_Name_List.index(select_movie_name)
                print('电影名称:', select_movie_name)
                print('上映时间:', Release_Time_List[movie_name_index])
                print('导演名字:', Direct_Name_List[movie_name_index])
                print('主演名字:', Leading_Role_List[movie_name_index])
                print('电影评分:', Movie_Grade_List[movie_name_index])
            else:
                print('查无此片')
        elif int(choice) == 3:
            print('退出程序')
            break
    else:
        print('请输入数字')





