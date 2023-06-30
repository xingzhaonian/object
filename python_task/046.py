'''
0. 装饰器的作用是什么？
答: 装饰器的作用是可以不改动函数本身的代码, 让该函数拥有该函数额外的功能

1. 装饰器必须是由嵌套函数实现吗？
答: 对, 装饰器的结构是 高阶函数 + 闭包

2. 如果使用装饰器去装饰一个函数，那么是否需要改动到该函数的内容呢？
答: 使用装饰器去装饰一个函数时, 不需要改动该函数的内容

3. 所以说，装饰器本身也是一个函数，它的功能是将目标函数进行打包，并返回一个加工后的新函数对象，对吗？
答: 对

4. 请问下面代码中，@add、@cube、@square 三个装饰器的执行顺序是？
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
答: 执行顺序是 @square, @cube, @add
基础写法:
init_square = square(test)
init_square_cube = cube(init_square)
init_square_cube_add = add(init_square_cube)
init_square_cube_add()

5. 请将下面装饰器的 @ 语法糖修改为函数调用的形式？
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

答: test = add(cube(square(test)))        print(test())

'''

'''
下面这段代码实现斐波那契数列：
import time
    
def fib():
    back1, back2 = 0, 1
    def func():
        nonlocal back1, back2
        back1, back2 = back2, back1 + back2
        print(back1, end=' ')
    return func
    
def get_fib(n):
    f = fib()
    for i in range(n):
        f()
    
n = int(input("请输入需要获取的斐波那契数："))
get_fib(n)
现在请大家编写一个装饰器，并将其放到适当的位置，目的是让代码 1 秒钟打印一个结果
'''
# 1
import time 
#num = int(input('请输入需要获取的斐波那契数：'))
def delay(function):
    def call_function():
        time.sleep(1)
        function()
    return call_function

def fib():
    a, b = 0, 1
   # @delay
    def inner():
        nonlocal a, b
        a, b = b, a + b
        print(a, end = ', ')
    return inner

def get_fib(n):
    f = fib()
    for i in range(n):
        f()

num = int(input('请输入需要的斐波那契数列：'))
get_fib(num)

#timer_execute()

def type_check(data_type):
    def outer(function):
        def inner(arg):
            if (type(arg)) == type(data_type()):
                return function(arg)
            else:
                return '参数类型错误'
        return inner
    return outer

@type_check(int)
def double(x):
    return x * 2
print(double(2))
print(double('2'))



@type_check(str)
def upper(s):
    return s.upper()
print(upper('i love fishc'))
print(upper(520))



