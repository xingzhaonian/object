r'''
0. 请问下面变量 d 是一个字典吗？
d = {}
答: 是的, {}是一个空字典, {1, 2, 3, 4, 5}则是合集

1. 字典中，同样一个值是否可以出现两次？
答: 值可以, 但是键不可以, 如果键有相同的, 最新的键对应的值对会覆盖前面的键对应的值

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
        

'''电话簿'''
print('欢迎进入鱼C电话簿')
name = []
phone_number = {}

while True:
    choice_mode = input('I:录入 / C:查询 / D:删除 / P:打印 / E:退出')
    if choice_mode == 'I':
        is_continue_input_phone_number = True
        is_continue_input_phone_number_1 = True
        while is_continue_input_phone_number:
            print('--- 录入模式 ---')
            input_name = input('请输入姓名')
            if input_name in phone_number:
                print(('名字已经存在, 手机号码是{}'.format(phone_number[input_name])))
                is_modify = input('是否修改？(Y / N)')
                if is_modify == 'Y':
                    is_continue_input_phone_number_1 = True
                    while is_continue_input_phone_number_1:
                        input_phone_number = input('请输入新手机号')
                        if not input_phone_number.isdecimal() or len(input_phone_number) != 11:
                            print('请输入正确的电话号码')
                            continue
                        else:
                            phone_number[input_name] = input_phone_number
                            print(phone_number)
                            is_continue_input_phone_number_1 = False
                elif is_modify == 'N':
                    print('不更新电话号码')
                else:
                    print('不更新电话号码')
                continue_input_phone_number = input('是否继续录入 Y / N')
                if continue_input_phone_number == 'Y':
                    is_continue_input_phone_number = True
                    continue
                elif continue_input_phone_number == 'N':
                    is_continue_input_phone_number = False
                    break
                else:
                    while continue_input_phone_number != 'N' or continue_input_phone_number != 'Y':
                        continue_input_phone_number = input('输入错误, 请重新输入( Y / N)')
                        if continue_input_phone_number == 'N':
                            is_continue_input_phone_number = False
                            is_continue_input_phone_number_1 = False
                            break
                        elif continue_input_phone_number == 'Y':
                            is_continue_input_phone_number = True
                            is_continue_input_phone_number_1 = False
                            break
            else:
                is_continue_input_phone_number_1 = True
                while is_continue_input_phone_number_1:
                    input_phone_number = input('请输入手机号')
                    if not input_phone_number.isdecimal() or len(input_phone_number) != 11:
                        print('请输入正确的电话号码')
                        continue
                    else:
                        phone_number[input_name] = input_phone_number
                        print(phone_number)
                        continue_input_phone_number = input('是否继续输入 Y / N')
                        if continue_input_phone_number == 'Y':
                            is_continue_input_phone_number = True
                            break
                        elif continue_input_phone_number == 'N':
                            is_continue_input_phone_number = False
                            break
                        else:
                            while continue_input_phone_number != 'N' or continue_input_phone_number != 'Y':
                                continue_input_phone_number = input('输入错误, 请重新输入( Y / N)')
                                if continue_input_phone_number == 'N':
                                    is_continue_input_phone_number = False
                                    is_continue_input_phone_number_1 = False
                                    break
                                elif continue_input_phone_number == 'Y':
                                    is_continue_input_phone_number = True
                                    is_continue_input_phone_number_1 = False
                                    break
    elif choice_mode == 'C':
        print('---查询模式---')
        is_continue_select = True
        while is_continue_select:
            select_name = input('请输入姓名')
            if select_name in phone_number:
                print(select_name,':', phone_number[select_name])
            else:
                print('没有该联系人')
            is_continue = input('是否继续查询(Y / N)')
            if is_continue == 'Y':
                continue
            elif is_continue == 'N':
                break
            else:
                while is_continue != 'Y' or is_continue != 'N':
                    is_continue = input('输入错误, 请重新输入(Y / N)')
                    if is_continue == 'Y':
                        is_continue_select = True
                        break
                    elif  is_continue == 'N':
                        is_continue_select = False
                        break
    elif choice_mode == 'D':
        print('---删除模式---')
        is_continue_del = True
        while is_continue_del:
            pop_name = input('请输入要删除的姓名')
            print(phone_number.pop(pop_name, '没有该联系人'))
            is_continue = input('是否继续删除(Y / N)')
            if is_continue == 'Y':
                continue
            elif is_continue == 'N':
                break
            else:
                while is_continue != 'Y' or is_continue != 'N':
                    is_continue = input('输入错误, 请重新输入(Y / N)')
                    if is_continue == 'Y':
                        is_continue_select = True
                        break
                    elif  is_continue == 'N':
                        is_continue_select = False
                        break
    elif choice_mode == 'P':
        print('---打印模式---')
        print(f'电话簿{phone_number}')
    elif choice_mode == 'E':
        print('---退出程序---')
        break
    else:
        print('输入错误, 请重新输入')