'''
0. 函数文档必须要放在函数体的开头吗？
答: 对, 函数文档必须在函数的开头顶部

1. 函数文档通常是保存在哪里？
答: 函数文档通常保存在__doc__中

2. 请问下面代码会打印什么呢？
>>> def times(s:str, n:int) -> str:
...     return s * n
...
>>> times(5, "FishC")
# 请问这里会打印什么内容？
答: FishCFishCFishCFishCFishC

3. 请问下面代码会打印什么呢？
>>> def foo(a: 'x', b: 5 + 6, c: list) -> max(2, 9):
>>>     pass
...
>>> foo.__annotations__
# 请问这里会打印什么内容？
答: {'a': 'x', 'b': 11, 'c': <class 'list'>, 'return': 9}

4. 如果我们自己定义一个函数 times，期望用户传入的两个参数分别是 整数型列表 和 整数，那么请问相应的类型注释应该怎么写？
答: def times(l:list[int], n:int) -> list:
    return l * n

5. 如果我们自己定义一个函数 times，期望用户传入的两个参数分别是 字典（其中键为字符串，值为浮点数）和 整数，那么请问相应的类型注释应该怎么写？
答: def times(d:dict[str, float], n) -> list:
    return list(d.values()) * n

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
    print(poker_data)
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
#doudizhu_poker(gamer1, gamer2, gamer3, poker_data)
def play_poker():
    '''
    "对牌" 即两张相同的牌
    "火箭" 即两张王
    "炸弹" 即四张相同的牌
    "三张" 即三张相同的牌
    '''
    while True:
        user_poker = input('请出牌(空格间隔, 退出请输入Q)')
        if user_poker == 'Q':
            break
        elif (len(user_poker) == 5) and (user_poker[1] == user_poker[4]):
            print('符合规则: 对子')
        elif (len(user_poker) == 11) and (user_poker[1] == user_poker[4] == user_poker[7] == user_poker[10]):
            print('符合规则: 炸弹')
        elif (len(user_poker) == 3) and ('☀' in user_poker) and ('🌙' in  user_poker):
            print('符合规则: 火箭')
        elif (len(user_poker) == 8) and (user_poker[1] == user_poker[4] == user_poker[7]):
            print('符合规则: 三张')
        else:
            print('不符合规则')
print(play_poker.__doc__)
    