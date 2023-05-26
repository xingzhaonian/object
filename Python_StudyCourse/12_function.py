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

(函数内 '/' 左边的只能是位置参数不能是关键字参数, 右侧的随意; '*' 号左边既能是位置参数也可以是关键字参数
, 而 '*' 右侧只能是关键字参数)
def abc(a, /, b, c):                                 def abc(a, *, b, c):
	print(a, b, c)									     print(a, b, c)














'''