'''
0. 请至少说出使用函数的两个显著优势？
答: 1. 函数可以打包代码, 可以最大程度的进行重复使用; 2. 可以将不同的代码进行封装, 分解, 降低代码结构的复杂程度, 增加代码可读性

1. 如果定义的函数不需要接收任何参数,可以不写小括号吗(像下面代码这样)？
>>> def myfunc:
...     pass
...
答: 不可以, 函数的基本结构为:
def 函数名 ():
    pass

2. 请问下面代码中,实参是什么？形参是什么？
>>> def myfunc(x, y):
...     print(x + y)
...
>>> a = 3
>>> b = 5
>>> myfunc(a, b)
8
答: 实参: 函数调用时实际传递的值a和b; 形参: 定义函数的时候写的参数的名字 x和y

3. 如果在函数的定义中没有出现 return 语句,是否说明该函数没有返回值？
答: 错误, 如果在函数的定义中没有出现 return 语句, 会有默认返回值, None

4. 一个函数能够在同时返回多个值吗？
答: 可以, 一个函数可以返回多个值

5. 请问下面代码,通过调用 funA() 函数,是否能够间接地调用到 funB() 函数,从而打印出 "Hi~" 呢(注意它们定义的顺序,在定义 funA() 函数的时候,funB() 函数仍未定义)？
>>> def funA():
...     funB()
...
>>> def funB():
...     print("Hi~")
...
>>> funA()
# 这里是否会报错呢？
答: 不会报错，可以成功调用
解析：通常情况下，定义需要在调用之前，不然会引发 name 'XXX' is not defined 的异常。
不过有一种例外情况, 那就是这个例子中演示的, 函数之间相互调用……
当我们在定义 funA() 函数的时候，并没有对其进行调用，函数体中的代码并没有被挨个儿执行，所以此时 funB() 是否存在，并不重要，它就是个符号~!
然后在调用 funA() 函数的时候，函数体中的代码才被真正的执行，此时 funB() 函数早就已经被悄悄定义过了，因此代码才不会报错，这就是其中的缘由！

6. 我们说函数是一个相对封闭的个体,那么函数是如何与外部通信的呢？
答: 通过参数和返回值

'''
'''
0. 请编写一个实现【注册】和【登陆】功能的代码,这次要求将不同的功能封装成独立的函数。
程序实现如下：
1.编写 4 个函数分别用于获取用户指令(get_int())、注册(register())、登陆(login())、MD5加密(encrypt())
2.使用一个 Python 的字典作为数据库。
3.注册时需验证用户名是否已存在于数据库
4.登陆时需验证用户名和密码是否匹配
5.密码保存需使用 MD5 加密
'''
import hashlib
database = {}
def encrypt(parameter1):
    md5_code = hashlib.md5(bytes(str(parameter1), encoding = 'utf-8')).hexdigest()
    return md5_code

def register():
    user_name = input('输入要注册的用户名')
    while True:
        if user_name in database:
            user_name = input('用户名已存在, 请重新输入')
        else:
            break
    password = input('输入密码')
    database[user_name] = encrypt(password)
    print(f'{database[user_name]}')
    print('恭喜, 注册成功')
    
def login():
    received_username = input('请输入用户名')
    if received_username not in database:
        while True:
            received_username = input('该用户名不存在, 请重新输入用户名')
            if received_username in database:
                break
    received_password = input('请输入密码')
    print(encrypt(received_password))
    if database[received_username] != encrypt(received_password):
        while True:
            received_password = input('密码错误, 请重新输入密码')
            print(encrypt(received_password))
            if database[received_username] == encrypt(received_password):
                break
    print('恭喜, 登陆成功')
    
def get_int():
    is_continue_with_operation = True
    while is_continue_with_operation:
        print('欢迎来到鱼C论坛')
        print('======================')
        print('1. 注册')
        print('2. 登陆')
        print('3. 退出')
        while True:
            choice = (input('请输入指令'))
            while (choice != '1') and (choice != '2') and (choice != '3'):
                print('指令错误, 请重新输入')
                choice = (input('请输入指令'))
            print('======================')
            if choice == '1':
                register()
                break
            elif choice == '2':
                login()
                break
            elif choice == '3':
                is_continue_with_operation = False
                break 
get_int()