r'''
0. 请问可以使用下面方法来更新字典的值吗？
>>> d = dict.fromkeys("FishC")
>>> d.update([('F',70), ('i',105), ('s',115), ('h',104), ('C',67)])
答: 可以
①, 字典的 update() 方法,可以同时给它传入多个键值对 d.update(F=70, i=105, s=115, h=104, C=67),  使用d.update()方法可以更新字典中的键的值; 
②, 传入一个字典{}  d.update({'F':70, 'i':105, 's':115, 'h':104, 'C':67})
③, 传入一个列表或者元组序列, 序列中包含可以多个键值对  d.update([('F',70), ('i',105), ('s',115), ('h',104), ('C',67)])

1. 请问下面代码执行之后，变量 e 的内容是？
>>> d = {"小甲鱼":"千年王八，万年龟。"}
>>> e = d.copy()
>>> d["小甲鱼"] = "666"
答: 因为字典同列表数据类型, 浅拷贝第一层的修改是不会相互影响的，但是对于嵌套层, 数据就会跟着改变

2. 请问下面代码执行之后，变量 e 的内容是？
>>> d = {"小甲鱼":{"数学":99, "英语":88, "语文":101}}
>>> e = d.copy()
>>> d["小甲鱼"]["语文"] = 100
答: e = {"小甲鱼":{"数学":99, "英语":88, "语文":100}}

3. 请问下面代码执行之后，字典 d 的内容是？
>>> d = {}
>>> d[1] = "千年王八"
>>> d[1.0] = "万年龟"
答: 字典 d 的内容是{'万年龟'}

4. items()、keys() 和 values() 三个方法分别用于获取字典的键值对、键和值三者的视图对象，你如何理解 “视图对象” 的含义？
答: 索引数据, 元数据改变了, 视图对象也会跟着变

5. 请问如何判断某一个值是否在字典中？
答: in 和 not in

6. 请问视频最后演示的代码，为什么字典 d 打印出来的结果是酱紫的？
>>> d = {x:y for x in [1, 3, 5] for y in [2, 4, 6]}
>>> d
{1: 6, 3: 6, 5: 6}
答: 因为字典中的key是唯一的, 后面如果有新的键的值会进行覆盖


动动手:
0. 请按照要求编写一个网站的注册模块
我们知道，通常一个网站的用户名都是唯一的，这就要求注册的时候，系统代码可以识别当前输入的用户名是否已经存在？
如果存在，则不允许注册！
那么现在请大家一起来动手，编写一个网站的注册模块。
要求：
1.用户名不允许重复
2.数据库需要保存用户名及密码
3.初始用户及密码("小甲鱼":"I_love_FishC", "不二如是":"FishC5201314")
'''
import hashlib

dict_name = {"小甲鱼":hashlib.md5(bytes("I_love_FishC", 'utf-8')), "不二如是":hashlib.md5(bytes("FishC5201314", 'utf-8'))}
is_register = True
while is_register:
    user_name = input('请输入用户名')
    while user_name in dict_name:
        user_name = input('用户名已被注册！请重新输入用户名')
    password = input('请输入密码')
    bstr = bytes(password, 'utf-8')
    passwd = hashlib.md5(bstr)
    dict_name[user_name] = passwd
    is_continue_register = input('是否继续注册(Y / N)')
    if is_continue_register == 'Y':
        continue
    elif is_continue_register == 'N':
        break
    else:
        while is_continue_register != 'Y' or is_continue_register != 'N':
            is_continue_register = input('输入错误, 请重新输入(Y / N)')
            if is_continue_register == 'Y':
                is_register = True
                break
            elif is_continue_register == 'N':
                is_register = False
                break
    print('------------------')
print('目前已经被注册的用户有:')
for k, v in dict_name.items():
    print('用户名:', k, '密码:', v.hexdigest(), end = '\n')