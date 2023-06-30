'''
函数
1. 可以最大程度的实现代码的重用, 减少大量的冗余代码
2. 可以将不同功能的代码进行封装, 分解, 从而降低结构的复杂度, 增加代码的可读性 

函数的结构
def myfunc():  # 定义函数:  def 函数名字 ():
    pass    # 函数内执行的代码

函数的参数
def myfunc(name):  # 括号内填函数的参数
    for i in range(3):
        print(f'i love {name}')   # 打印函数的参数
myfunc('haha')   # 把'haha' 传入函数的参数, 调用函数会打印3次 'haha'

def myfunc(name, times):   # 函数的参数可以有多个
	for i in range(times):
		print(f'i love {name}')
def myfunc('python', 5)  # 调用函数, 会打印5次 'python'

函数的参数分为实际参数和形式参数两种
形式参数: 是函数定义时写的参数的名字, 比如上面的 name 和 times
实际参数: 是在调用函数的时候实际传递进去的值

函数的返回值
def div(x , y):  # 定义函数, 该函数有两个参数
    z = x / y    # 函数执行的代码, 即 z = x / y
    return z     # return 语句则是在执行完函数后返回一个值
函数 return完之后会立马结束, 不会再走其他代码, 例如:
def div(x, y):
	if y == 0:
		return ('除数不能为0')
	z = x / y
	return z
div(5, 0) 返回 '除数不能为0', 返回之后就不会走	z = x / y; return z
如果该函数没有写 return 语句, 则代码执行完毕后默认会返回None
================================================================================================
参数就是定制的接口
1. 位置参数--- 在定义参数的时候就把参数的名字和位置给确定下来, 我们将python中这类位置固定的参数叫做位置参数
def myfunc(parm1, parm2, parm3):
	return parm1, parm2, parm3
调用myfunc(parm1, parm2, parm3)结果: parm1, parm2, parm3

2. 关键字参数--- 指在调用的时候在调用具有参数默认值的函数时, 使用参数的关键字来指定为哪个参数赋值, 位置参数必须在关键字参数之前 
def myfunc(parm1, parm2, parm3):
	return parm1, parm2, parm3
调用myfunc(parm1 = 1, parm2 = 2, parm3 = 3)结果 1, 2, 3

3. 默认参数--- 如果我们使用默认参数, 那么我们就应该把它放在最后面, 定义函数时, 写上默认参数,调用该方法时,默认参数可以不写, 它会自动用使用定义时写下的默认参数,
如果调用时在默认参数的位置写了参数, 该参数就会覆盖定义时写的默认参数
def myfunc(parm1, parm2, parm3 =  5):
	return parm1, parm2, parm3
调用myfunc(1, 2)结果 1, 2, 5;   myfunc(1, 2, 5)结果 1, 2, 5   myfunc(1, 2, parm3= 10)结果 1, 2, 10
4.打包参数--- 定义函数时在形参的前面加 '*' 来表示收集参数打包为元组, 在形参的前面加 '**' 来表示收集参数打包为字典
5.解包参数--- 调用函数时在传入的参数前加 '*' 来表示将传入的参数进行解包, 刚好能匹配到定义函数时需要的参数个数, 
调用函数时在传入的参数前加 '**' 来表示将传入的参数进行解包, 刚好能匹配到定义函数时需要的参数个数,
(函数内 '/' 左边的只能是位置参数不能是关键字参数, 右侧的随意; '*' 号左边既能是位置参数也可以是关键字参数, 
而 '*' 右侧只能是关键字参数)
def abc(a, /, b, c):                                 def abc(a, *, b, c):
	print(a, b, c)									     print(a, b, c)

========================
作用域: 
局部变量: 如果一个变量定义的位置在一个函数的里面, 该变量的作用域只在函数内, 称为局部变量
全局变量: 如果在任何函数外部定义一个变量, 那么它的作用域就是全局的, 称为全局变量
注意: 在函数中局部变量会覆盖同名的全局变量; 函数内部可以访问全局变量, 但无法修改该变量的值, 因为
一旦如果在函数内出现了和全局变量同名的局部变量, 那么局部变量就会覆盖全局变量

global语句: 在函数内部需要修改全局变量的值时, 那么就在函数内部写上 global + 要修改的变量名, 这样就可修改全局变量了

嵌套函数: 
1. 内部函数无法直接进行调用, 需要通过外部函数去进行调用
2. 内部函数可以访问到外部函数的变量, 但内部函数却无法修改外部函数的变量(同全局变量和局部变量道理)

nonlocal 语句: 在内部函数要修改外部函数的变量时, 使用 nonlocal + 变量名即可在内部函数中修改外部函数变量的值

LEGB规则:
L 是 local (局部作用域)
E 是 enclosed (嵌套函数的外层函数作用域)
G 是 global (全局作用域)
B 是 build-in (内置作用域)

===========================================================================================================
函数内部的变量, 它的作用域只在函数内部生效, 在函数外部是无法进行访问的
在嵌套函数中可以访问到外部函数的变量, 但无法修改, 除非声明nonlocal
外层函数的作用域是会通过某种形式保存下来的, 尽管这个函数已经调用完了, 但是外层作用域里的变量是会保存下来的
(在内层函数修改外层函数变量的情况下, 如果外层函数赋值给某个变量, 通过调用变量加' ()' , 那么每次调用后外层
函数的变量会保存下来, 如果只是通过调用外层函数加 '()()' 的话, 外层变量则不会保存)
闭包--- 
闭包的结构是嵌套函数, 外层函数返回内层函数的函数名, 把外层函数通过变量进行赋值, 这个变量就会记住外层函数内的变量, 每次重复
调用, 把外层函数通过变量进行赋值的变量值都会变(它会记住, 保存下来了)

高阶函数
把一个函数作为参数传递给另一个函数, 或者一个函数的返回值为另一个函数(若返回值为该函数本身，则为递归), 满足其中一种则为高阶函数
例如: 
def functionA():
	print('调用函数A')
def functionB(function):
	print('开始调用函数')
    function()
    print('调用完毕')
functionB(functionA)

或者

def bar():
	print('in bar function')
def foo():
	print('in foo function')
    return bar
result = foo()
result()


装饰器
装饰器的结构是 高阶函数 + 闭包
例如:
def time_master(function):
	def calc_time():
		print('开始运行程序')
        start_time = time.time()
        function()
        end_time = time.time()
        print(f'运行该函数共计{end_time - start_time}秒')
    return calc_time
@time_master
def myfunction():
	time.sleep(2)
    print('hello fishc')

myfunction()

多个装饰器可以同时用在同一个函数上
例如:
def add(function):
	def inner():
		x = function
        return x + 1
    return inner
    
def cube(function):
	def inner():
		x = function
        return x * x * x
    return inner
    
def square(function):
	def inner():
		x = function
        return x * x
    return inner
@add
@cube
@square
def test():
	return 2
test()

如何给装饰器传递参数?
需要用到三层嵌套函数, 第一层函数需要一个参数, 这个参数不能是一个函数, 第二层函数需要一个参数, 这个参数必须是一个函数,
第三层函数看需求, 如果需要就用传参(但参数不能是一个函数), 如果不用就不传
例如:
def logger(msg):
	def time_master(function):
		def calc_run_time():
			start_time = time.time()
            function()
            end_time = time.time()
            print(f'[{msg}]共运行了{end_time - start_time:.3f}秒')
        return calc_run_time
    return time_master

@logger('A')
def functionA():
	print('正在调用函数A')
	time.sleep(1)
functionA()

@logger(msg = 'B')
def functionB():
	print('正在调用函数B')
    time.sleep(2)
functionB()

==================================================================================================
lambda表达式
lambda arg1, arg2, arg3, ... argN : expression   lambda关键字后面跟着函数的参数, 冒号左边为lambda x, 右边为表达式
x = lambda x : x * x
x(3)  返回9
lambda 还可以放进列表中
relust = [lambda x : x * x, 3, 5]
relust[0](relust[1])  解析: relust为一个列表, 该列表中的第一个参数为lambda表达式, 表达式需要一个参数x, 将relust的第二个参数
也就是 3 传入lambda 表达式, 结果为9

mapped = list(map(lambda x : ord(x) + 10, 'fishc')) 解析: map函数需要两个参数第一个参数是函数, 而lambda就是函数, 所以能作为
map的第一个参数使用, 该lambda函数的表达式为将x作为参数传给lambda, 然后将取出x的对应的编码数值
返回[112, 115, 125, 114, 109]

boring = list(filter(lambda x : x % 2, range(10))) 解析: 返回10以内的奇数 filter计算出的结果为假不返回哦~~

lambda 是一个表达式而非语句, 所以它能够出现在python不允许def语句出现的地方, 这是它最大的优势, 但由于所有的功能代码都局限
在一个表达式中去实现, 因此 lambda表达式通常也只能实现一些功能比较简单的需求













'''