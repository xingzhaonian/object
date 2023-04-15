r'''
0. 请问下面变量 d 是一个字典吗？
d = {}
答: 是的, {}是创建字典的关键符号

1. 字典中，同样一个值是否可以出现两次？
答: 不可以, 如果有相同的, 最新的键对应的值对会覆盖前面的值

2. 请问下面代码创建的字典中，键和值分别是什么？
d = {}.fromkeys("吕布", 999)
答: d = {'吕':999, '布':999}

3. 请问下面代码中, del d 这个语句, 是单独删除 d 变量还是将 d 变量和其指定的字典一起干掉呢？
d = dict.fromkeys("Fish", 250)
del d
答: 直接干掉对象 d

4. 请问下面创建字典的 8 种方法中, 哪几种是正确的
>>> a = {99:"吕布", 90:"关羽", 60:"刘备"}
>>> b = dict(99:"吕布", 90:"关羽", 60:"刘备") x
>>> c = dict(99="吕布", 90="关羽", 60="刘备") x
>>> d = dict([(99, "吕布"), (90, "关羽"), (60, "刘备")])
>>> e = dict({99:"吕布", 90:"关羽", 60:"刘备"})
>>> f = dict({99="吕布", 90="关羽", 60="刘备"}) x
>>> h = dict({99:"吕布", 90:"关羽"}, 60="刘备") x
>>> i = dict(zip([99, 90, 60], ["吕布","关羽","刘备"]))
答: a, d, e, i

5. 请问下面代码执行之后，变量 b 中的内容是？
>>> a = {"小甲鱼":"You are my super star."}
>>> b = a
>>> a.clear()
答: b = a, id(a) = id(b); 所以a.clear() 之后 b也变空了

'''
Movie_Name_list = []
dict_Release_Time_List = {}
dict_Direct_Name_List = {}
dict_Leading_Role_List = {}
dict_Movie_Grade_List = {}
while True:
    is_continue_inquire_about = True
    choice = input('请输入想要的功能(1:进行数据录入 / 2:进行数据查询 / 3:退出程序):')
    if choice.isspace():
        print('输入为空, 请再次输入')
        continue
    if choice.isdecimal():
        if int(choice) > 3 or int(choice) == 0:
            print('输入选项无效, 请重新输入')
            continue
        if int(choice) == 1:
            while is_continue_inquire_about:
                print('进行录入选项')
                movie_name = input('请输入电影名称:')
                Movie_Name_list.append(movie_name)
                Release_Time = input('请输入上映日期:')
                dict_Release_Time_List[movie_name] = Release_Time
                direct_name = input('请输入导演名字(多人请用" / "分隔):')
                dict_Direct_Name_List[movie_name] = direct_name
                lading_role_name = input('请输入主演名字(多人请用" / "分隔):')
                dict_Leading_Role_List[movie_name] = lading_role_name
                movie_grade = input('请输入电影评分:')
                dict_Movie_Grade_List[movie_name] = movie_grade
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
            if select_movie_name in Movie_Name_list:
                print('电影名称:', select_movie_name)
                print('上映时间:', dict_Release_Time_List[select_movie_name])
                print('导演名字:', dict_Direct_Name_List[select_movie_name])
                print('主演名字:', dict_Leading_Role_List[select_movie_name])
                print('电影评分:', dict_Movie_Grade_List[select_movie_name])
            else:
                print('查无此片')
        elif int(choice) == 3:
            print('退出程序')
            break
    else:
        print('请输入数字')