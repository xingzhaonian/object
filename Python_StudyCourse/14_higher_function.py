'''
===[高阶函数]===
一个函数被当作参数传给另一个函数的时候, 我们称这种函数为高阶函数
模块 functools
[reduce 函数]
functools.reduce(add, [1, 2, 3, 4, 5])
解析: reduce函数需要两个参数, 第一个参数为函数, 第二个参数为可迭代对象, reduce 的作用就是将第二个可迭代对象的参数依次传递到
第一个函数参数中, 最终返回累计的结果, 最终返回 15

===[偏函数]===
偏函数的是指对指定的函数进行二次包装, 通常是将现有的函数部分参数预先给绑定, 从而得到一个新的函数(本质就是闭包)
例如 cube = fcuntools.partial(pow, exp = 3)
cube(3)  返回9
cube(4)  返回64

===[@wraps]===
@wraps装饰器是用来装饰装饰器的
例如
import time

def time_master(function):
    def call_function():
        print('开始运行程序')
        start_time = time.time()
        function()
        end_time = time.time()
        print('程序结束运行')
        print(f'共消耗了{end_time - start_time:.2f}秒')
    return call_function

@time_master
def myfunction():
    time.sleep(2)
    print('i love fishc')
myfunction()
这时候我们使用自省, myfunction.__name__ 返回的是 'call_function', 因为闭包设计, 这里其实最终调用的是call_function
然而我们有了 @wraps 装饰器, 我们就可以这样使用
import time
import functools

def time_master(function):
    @functools.wraps(function)    # 这里使用@wraps装饰器来进行装饰
    def call_function():
        print('开始运行程序')
        start_time = time.time()
        function()
        end_time = time.time()
        print('程序结束运行')
        print(f'共消耗了{end_time - start_time:.2f}秒')
    return call_function

@time_master
def myfunction():
    time.sleep(2)
    print('i love fishc')
myfunction()
这时候我们使用自省, myfunction.__name__ 返回的是 'myfunction'
'''