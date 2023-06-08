'''
0. 为什么小甲鱼在视频中说, Python 的阻止局部变量盖全局变量的做法，是一种出于对代码的 “保护” 的表现？
答: 因为在函数中一旦修改了全局的变量, 那么在别的地方这个全局变量很有可能就被改变了, 到时候除了bug不好找

1. 学了这节课，你觉得除了通过参数给函数传递信息之外，还有什么途径可以传递信息到函数内部呢？
答: 在函数内部给全局变量声明 global 关键字后, 就可以在函数内部使用全局变量了

2. 请问下面代码会打印什么呢？
>>> x = 250
>>> def set_x(v):
...     x = v
...     print(x, end=' ')
...        
>>> set_x(520)
>>> print(x)
>>> # 请问这里会打印什么内容？
答: 打印 520, 250, 因为通过参数传给函数的是520, 函数内部给x进行赋值操作, x就等于520, 然后调用函数
输出520, 再打印x, 全局变量 x 没有变, x 为250

3. 请问下面代码会打印什么呢？
>>> x = 123
>>> y = 456
>>> def exchange(x, y):
...     x, y = y, x
...        
>>> exchange(x, y)
>>> print(x, y)
>>> # 请问这里会打印什么内容？
答: 打印 123, 456 函数内的变量无论如何改变, 都不会影响到外部函数的变量, 除非声明 global 关键字

4. 请问下面代码会打印什么呢？
>>> x = [1, 2, 3]
>>> def invert(x):
...     x = x[::-1]
...
>>> invert(x)
>>> print(x)
>>> # 请问这里会打印什么内容？
答: 打印 [1, 2, 3] 因为函数外部的变量 x 和 函数内部的 x 是两个不同的变量, 分别指向的内存地址都不一样


5. 请问下面代码会打印什么呢？
>>> x = [1, 2, 3]
>>> def invert(x):
...     x[:] = x[::-1]
...
>>> invert(x)
>>> print(x)
>>> # 请问这里会打印什么内容？
答: 打印 [3, 2, 1], 根据我自己测试得出的结果, 可变数据类型(列表, 字典, 集合)在全局声明变量后, 在函数的内部
可以直接修改到该全局变量(可变的数据类型), 无需声明 global

6. 请问下面代码会打印什么呢？
>>> x = 100
>>> def funA():
...     global x
...     x = 250
...     def funB():
...         nonlocal x
...         x = 520
...     funB()
...
>>> funA()
>>> print(x)
>>> # 请问这里会打印什么内容？
答: 会报错, 因为 在全局声明了一个变量 x 为100, 在A函数内声明了 global x, 这时候说明函数内引用的 x 是外部
的全部变量(可进行修改), 而嵌套在函数A内的函数B 声明了 nonlocal x, 但是嵌套函数内声明 nonlocal x 是声明上
层函数A内的局部变量, 但是函数A内的变量x已经是全局的了, 也是就说, 函数A作为函数B的上层函数, 是没有局部变量
的, 所以报错
'''
'''
1. 写下从 1 到 N 的数字
2. 获取一个 1 到剩下数字（包括这个数字）的随机数 k
3. 从低位开始，取出第 k 个数字（这个数字还没有被取出），把它写在独立的一个列表的最后一位
4. 重复前两个步骤，直到所有数据都被取出
5. 现在，新的列表中就是打乱了顺序的结果
'''
import random

def fy_shuffle(raw_data, times = 1):
    for i in range(times):
        raw_data_target =  list(raw_data)
        result_data_list = []
        data_list_lenght = len(raw_data_target)
        for k in range(data_list_lenght):
            random_num = random.randint(1, data_list_lenght - k)
            result_data_list.append(raw_data_target.pop(random_num - 1))
            #raw_data_target.remove(raw_data_target[random_num - 1])
            str_result = ''.join(map(str, result_data_list))
        print(f'第{i + 1}次后打乱的结果是{str_result}')
    print(f'最终结果是{str_result}')
    return result_data_list

#raw_data_list = input('请输入需要打乱的序列: ')
#work_times = int(input('请输入需要打乱的次数: '))
#fy_shuffle(raw_data_list, work_times)

poker_data = ['♣1', '♦1', '♥1', '♠1',\
              '♣2', '♦2', '♥2', '♠2',\
              '♣3', '♦3', '♥3', '♠3',\
              '♣4', '♦4', '♥4', '♠4',\
              '♣5', '♦5', '♥5', '♠5',\
              '♣6', '♦6', '♥6', '♠6',\
              '♣7', '♦7', '♥7', '♠7',\
              '♣8', '♦8', '♥8', '♠8',\
              '♣9', '♦9', '♥9', '♠9',\
              '♣10', '♦10', '♥10', '♠10',\
              '♣J', '♦J', '♥J', '♠J',\
              '♣Q', '♦Q', '♥Q', '♠Q',\
              '♣K', '♦K', '♥K', '♠K',\
              '☀', '🌙'
              ]

def doudizhu_poker(a, b, c, poker_data):
    # 初始化数据
    each_gamer_poker_count = 17
    all_gamer_poker = {}
    all_gamer_poker[a] = []
    all_gamer_poker[b] = []
    all_gamer_poker[c] = []
    shuffle_times = int(input('开始洗牌, 请问要洗几次牌? '))
    shuffle_result = fy_shuffle(poker_data, shuffle_times)
    for i in range(each_gamer_poker_count):
        all_gamer_poker[a].append(shuffle_result.pop())
        all_gamer_poker[b].append(shuffle_result.pop())
        all_gamer_poker[c].append(shuffle_result.pop())
    landlord = random.sample((a, b, c), 1)[-1]
    all_gamer_poker[landlord].extend((shuffle_result[-1], shuffle_result[-2], shuffle_result[-3]))
    a_str_poker_date = ' '.join(map(str, all_gamer_poker[a]))
    b_str_poker_date = ' '.join(map(str, all_gamer_poker[b]))
    c_str_poker_date = ' '.join(map(str, all_gamer_poker[c]))
    print(f'玩家{landlord}是地主')
    print(f'玩家{a}的牌是{a_str_poker_date}, 共{len(all_gamer_poker[a])}张牌')
    print(f'玩家{b}的牌是{b_str_poker_date}, 共{len(all_gamer_poker[b])}张牌')
    print(f'玩家{c}的牌是{c_str_poker_date}, 共{len(all_gamer_poker[c])}张牌')

gamer1 = input('请输入第一位玩家的名称: ')
gamer2 = input('请输入第二位玩家的名称: ')
gamer3 = input('请输入第三位玩家的名称: ')
doudizhu_poker(gamer1, gamer2, gamer3, poker_data)