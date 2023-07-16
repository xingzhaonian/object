'''
0. 请问如何定义一个高阶函数？
答: 高阶函数是对其他函数进行操作的函数，操作可以是将它们作为参数，或者是返回它们
一个函数作为参数传给另一个函数, 我们称这种函数为高阶函数

1. 请将下面的 add() 函数修改为 lambda 表达式的表现形式？
>>> def add(x, y):
...     return x + y
...
>>> functools.reduce(add, range(1, 101))
5050
答: 导入functools 模块, 使用functools.reduce; functools.reduce(lambda x, y : x + y, range(1,101))

2. 偏函数的实现原理是？
答: 偏函数的本质就是闭包

3. 请将下面闭包代码改用偏函数来实现？
>>> def power(exp):
...     def exp_of(base):
...         return base ** exp
...     return exp_of
...
>>> square = power(2)
>>> cube = power(3)
>>> square
<function power.<locals>.exp_of at 0x000001CF6A1FAF70>
>>> square(2)
4
>>> square(5)
25
>>> cube(2)
8
>>> cube(5)
125
答: 导入functools模块, 使用partial方法
square = functools.partial(pow, exp = 2)
square(3)
cube = functools.partial(pow, exp = 3)
cube(3)

4. 请使用偏函数，基于 print() 函数打造一个新的 pr() 函数，使其实现效果如下：
>>> pr("I", "love", "FishC.")
I@love@FishC.#
答: pr = functools.partial(print, sep='@', end='#')

5. 请修改下面代码，使得执行 test.__name__ 语句后，得到的结果是 'test'，而非 'call_func'。
>>> def myfunc(func):
...     def call_func():
...         func()
...     return call_func
...
>>> @myfunc
... def test():
...     print("test~")
...
>>> test()
test~
>>> test.__name__
'call_func'
答: 这里要使用到@wraps装饰器
import time
import functools

def myfunc(func):
    @functools.wraps(func)
    def call_func():
        func()
    return call_func

@myfunc
def test():
    print("test~")
test()




'''