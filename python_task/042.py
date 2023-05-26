'''
0. 如果一个函数要求传递位置参数，那么颠倒实参的顺序，肯定会报错，是吗？
答: 不会报错

1. 默认参数跟关键字参数有啥区别？
答：默认参数: 指在定义函数时写下的某个参数的默认值, 调用时可以不写该参数的值, 如果不写那就用定义函数时写下的默认
值, 如果写了那就会用写的替换掉默认的
关键字参数:指在调用时为哪个参数赋值, 关键字参数必须在位置参数后面

2. 任何支持传递位置参数的函数，都可以使用关键字参数吗？
答: 不是, 函数内 '/' 左侧的参数不可以用关键字参数来传递, '/' 右侧的可以

3. 请问下面代码是否会报错，为什么？
>>> def abc(a, /, b, c):
...     print(a, b, c)
...
>>> abc(a=3, b=2, c=1)
# 请问这里会报错吗？
答: 会报错, 函数内 '/' 左侧的参数不可以用关键字参数来传递, 只能用位置参数传递,  '/' 右侧的可以

4. 请问下面代码是否会报错，为什么？
>>> def abc(a, *, b, c):
...     print(a, b, c)
...
>>> abc(c=3, b=2, a=1)
# 请问这里会报错吗？
答: 不会, 因为 '*' 右侧的参数必须为关键字参数, 左侧随意, 可以是位置参数也可以是关键字参数

5. 请问下面代码会打印什么内容，为什么？
>>> def myfunc(s, vt, o):
...    return "".join((o, vt, s))
...
>>> myfunc(o="我", "清蒸", "小甲鱼")
# 请问这里会打印什么内容？
答: 会报错, 因为关键字参数必须在位置参数后面

动动手:
0. 检测输入的中文字符串是否符合回文的语法，这个前面大家已经做过练习了，不过这一次我们将要放宽，只要该字的拼音一样，字不相同没有关系，比如 “前任只认钱” 可以符合要求。
提示一：放宽要求后，只要文字的发音构成前后回文，即认定为符合要求。
提示二：将汉字转换为对应拼音的方法
提示三：请将各个独立的功能封装为函数
'''
import xpinyin

def input_string():
    s = input('请输入一段话：')
    while len(s) <= 1:
        s = input('字数太少, 重新输入：')
    return s

def characters_to_pinyin(Chinese):
    pinyin = xpinyin.Pinyin().get_pinyin(Chinese)
    return pinyin

def is_palindrome(characters):
    s_pinyin = characters.split('-')
    if s_pinyin == s_pinyin[::-1]:
        return True
    else:
        return False
    
def result():
    if is_palindrome(string_pinyin):
        print(f'{[string]}是回文')
    else:
        print(f'{[string]}不是回文')

string = input_string()
string_pinyin = characters_to_pinyin(string)
result()

    
'''
1. 利用函数模拟创建【栈】的数据结构操作
'''
stack_list = []

def push_value():
    input_push_value = input('请输入将要压入栈中的值：')
    stack_list.append(input_push_value)
    for i in stack_list[::-1]:
        print(i)

def pop_value():
    stack_length = len(stack_list)
    if stack_length > 0:        
        pop_value = stack_list.pop()
        print(pop_value)
        print('栈: ')
        for i in stack_list[::-1]:
            print(i)
    else:
        print('堆栈已经空了~')

def top_value():
    stack_length = len(stack_list)
    if stack_length > 0:        
        print(stack_list[-1])
    else:
        print('堆栈已经空了~')

def choice():
    while True:
        receive_data = input('请输入指令(push/pop/top/exit)')
        while (receive_data != 'push') and (receive_data != 'pop') and (receive_data != 'top') and (receive_data != 'exit'):
            receive_data = input('输入错误, 请重新输入(push/pop/top/exit)')
        if receive_data == 'push':
            push_value()
        elif receive_data == 'pop':
            pop_value()
        elif receive_data == 'top':
            top_value()
        elif receive_data == 'exit':
            break 
    
choice()