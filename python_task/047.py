'''
0. 请将下面 lambda 表达式写成普通函数的形式？
f = lambda x, y, z: x + y + z
def call(x, y, z):
    return x + y + z
f = call(1, 2, 3)

1. 请问下面代码会返回 True 还是 False 呢？
>>> def squareX(x):
...     return x * x
...
>>> squareY = lambda y : y * y
>>> squareX == squareY
# 请问这里返回 True 还是 False
答: 返回False, 因为一个是function, 一个是表达式

>>> squareX(3) == squareY(3)
# 请问这里返回 True 还是 False
答: 返回True, 这里是调用函数, 返回的是结果, 两边都返回9, 所以相等

2. 小甲鱼在视频中说，“由于lambda是一个表达式，因此它可以用在常规函数不可能存在的地方，比如把它放到列表里面……”，那么请问
下面代码是否可以成功访问？
>>> def squareX(x):
...     return x * x
...
>>> y = [squareX, 2, 3]
>>> y[0](y[1])
答: 可以

3.请使用 map() 函数以下代码实现相同的功能？
>>> [x ** 2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
答: list(map(lambda x : x ** 2, range(10)))

4, 请使用 filter() 函数实现相同功能？
>>> [x for x in range(10) if x % 2]
[1, 3, 5, 7, 9]
答: list(filter(lambda x : x % 2, range(10)))

5. 请将下面的闭包函数成 lambda 表达式的实现形式？
>>> def power(exp):
...     def exp_of(base):
...         return base ** exp
...     return exp_of
...
>>> square = power(2)
>>> cube = power(3)
>>> square(2)
4
>>> square(5)
25
>>> cube(2)
8
>>> cube(5)
125
答: f = lambda exp : lambda base : base ** exp

6. 请将下面三个装饰器函数写成 lambda 表达式的实现形式
def add(func):
    def inner():
        x = func()
        return x + 1
    return inner
    
def cube(func):
    def inner():
        x = func()
        return x * x * x
    return inner
    
def square(func):
    def inner():
        x = func()
        return x * x
    return inner
    
@add
@cube
@square
def test():
    return 2
    
print(test())

答:
@lambda func : lambda : func() + 1
@lambda func : lambda : func() * func() * func()
@lambda func : lambda : func() * func()
def test():
    return 2
    
print(test())



动动手：
power = {"吕布":999, "关羽":888, "刘备":666, "张飞":900, "赵云":789, "不二如是":999}
    
# 请 lambda 表达式和 filter() 函数配合，替换下面的代码
greater = []
for k, v in power.items():
    if v > 800:
        greater.append((k,v))
# 请 lambda 表达式和 filter() 函数配合，替换下面的代码
    
print(greater)
[('吕布', 999), ('关羽', 888), ('张飞', 900), ('不二如是', 999)]
'''

power = {"吕布":999, "关羽":888, "刘备":666, "张飞":900, "赵云":789, "不二如是":999}
x = list(filter(lambda x : x[1] > 800, power.items()))
#print(x)
'''
1. 请用一行代码找出猪队友。
假如有一个比赛，团队的最终得分是由每个成员的得分相加而来……
因此，团队成员得分最低的，我们尊称其为 “猪队友”~
问题：
请使用一行代码，找到每个队伍的 “猪队友”（给大家降低一点难度，我们假设同一团队中，每位成员的得分均不相同）
>>> members = {
    "鱼C工作室" : {"小甲鱼":83, "不二如是":89, "二师兄":64, "小师妹":75, "鱼小二":96},
    "复仇者联盟" : {"钢铁侠":85, "绿巨人":39, "黑寡妇":82, "鹰眼":73, "雷神":99},
    "奥特曼家族" : {"迪迦":99, "艾斯":84, "泰罗":63, "佐菲":78, "赛文":78}}
>>> 
>>> # 请在此处添加一行代码，完成题目要求，并将结果保存在变量 x 中
>>> 
>>> print(x)
['鱼C工作室:二师兄', '复仇者联盟:绿巨人', '奥特曼家族:泰罗']
'''
members = {
    "鱼C工作室" : {"小甲鱼":83, "不二如是":89, "二师兄":75, "小师妹":75, "鱼小二":96},
    "复仇者联盟" : {"钢铁侠":85, "绿巨人":39, "黑寡妇":82, "鹰眼":73, "雷神":99},
    "奥特曼家族" : {"迪迦":99, "艾斯":84, "泰罗":63, "佐菲":78, "赛文":63}}
# 请在此处添加一行代码，完成题目要求，并将结果保存在变量 x 中
x = [':'.join((i, min(members[i].items(), key = lambda x:x[1])[0])) for i in members]


def find_pig_teammate():
    relust = []
    for i, k in members.items():
        for x in k.keys():
            if k[x] == min(k.values()):
                relust.append(i + ':' + x)
    return relust
print(find_pig_teammate())
