'''
0. 为什么将闭包称之为 “工厂函数”？
答: 因为闭包的结构是嵌套结构, 外层的函数返回值是内层函数, 也就是制造函数的函数, 所以叫做工厂函数

1. 实现闭包必须要用到嵌套函数吗？
答: 对, 实现闭包必须要用到嵌套函数, 因为闭包的结构就是嵌套函数, 外层的函数返回值是内层函数

2. 请问下面代码会打印什么呢？
>>> def funA():
...     x = 520
...     def funB():
...         print(x)
...     return funB
...
>>> funny = funA()
>>> del funA
>>> funny()
>>> # 请问这里会打印什么内容？
答: 会打印 520, 虽然已经删除了funA函数, 但是在删除之前funA被赋值给了funny, funny被保存了下来, 所以执行funny() 就相当于调用funB函数

def outter():
    def innerA():
        x = 100
    
    def innerB():
        nonlocal x
        x = 250
    
    def innerC():
        global x
        x = 520
    
    x = 880
    
    innerA()
    print(f"调用完 innerA() 函数之后,x = {x}")
    
    innerB()
    print(f"调用完 innerB() 函数之后,x = {x}")
    
    innerC()
    print(f"调用完 innerC() 函数之后,x = {x}")
    
outter()
print(f"此时此刻,全局变量 x = {x}")
答: 
print(f"调用完 innerA() 函数之后,x = {x}")  打印: 880
print(f"调用完 innerB() 函数之后,x = {x}")  打印: 250
print(f"调用完 innerC() 函数之后,x = {x}")  打印: 250
print(f"此时此刻,全局变量 x = {x}") 打印: 520

4. 如果想要函数 funA() 的调用结果如下,它的函数体应该如何定义？
>>> # 请定义 funA() 函数,使其调用结果如下。
>>> funA(3)(4)(5)
60
答: 
def funA(x):
    def funB(y):
        def funC(z):
            num = x * y * z
            return num
        return funC
    return funB
print(funA(3)(4)(5))

5. 挑战一下自己,请将下面这个闭包函数转换为 lambda 表达式的形式？
>>> def maker(n):
...     def action(x):
...         return x ** n
...     return action
>>> f = maker(2)
>>> f(3)
9
>>> f(5)
25
答:
def maker(n):
    return lambda x: x ** n

'''

'''
0. 请设计一个函数,每次调用传入一个参数,并返回所有参数的平均值。
函数实现如下：
>>> avg = make_avg()
>>> avg(5)    # 第一次调用,只有 1 个参数,平均值是 5
5.0
>>> avg(3)    # 第二次调用,(5 + 3) / 2
4.0
>>> avg(7)    # 第三次调用,(5 + 3 + 7) / 3
5.0
>>> avg(19)   # 第三次调用,(5 + 3 + 7 + 19) / 4
8.5
'''
def make_avg(make_avg_param = 0):
    count = 0
    def inner(inner_param):
        nonlocal count
        nonlocal make_avg_param
        make_avg_param += inner_param
        count += 1
        print(f'{make_avg_param} / {count} = {make_avg_param / count}')
        return count, make_avg_param / count
    return inner
avg = make_avg()
avg(5)
avg(3)
avg(7)
avg(19)
'''
1. 请设计一个闭包函数, 它的功能是每次调用返回一个斐波那契数列。
函数实现如下：
>>> f = fib()
>>> f()
0
>>> f()
1
>>> f()
1
>>> f()
2
>>> f()
3
>>> f()
5
>>> f()
8
>>> f()
13
>>> f()
21
'''
def Fibonacci():
    a = 0
    b = 1
    def calc_Fibonacci():
        nonlocal a, b
        print(a)
        a, b = b, a + b
        return a
    return calc_Fibonacci



f = Fibonacci()
f()
f()
f()
f()
f()
f()
f()
f()
def fibnac():
    init_list_data = [0, 1]
    count = 0
    def calc_fibnac():
        nonlocal init_list_data, count
        if count == 0:
            print(init_list_data[0])
        result = init_list_data[-1] + init_list_data[-2]
        init_list_data.append(result)
        print(result)
        count += 1
        return result
    return calc_fibnac

f = fibnac()
f()
f()
f()
f()