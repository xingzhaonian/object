'''
===[函数文档]===
创建函数文档非常简单, 只需要在函数内部的开头使用三引号字符串即可
例如
'''
def exchange(dollar, rate = 6.32):
    '''
    功能：汇率转换，美元--->人民币
    参数：
    -dollar 美元数量
    -rate 汇率， 默认值是6.32 (2023-07-15)
    '''
    return dollar * rate
'''
以上就是一个标准的函数文档写法(注意: 函数文档一定是在函数开头)

===[类型注释]===
def times(s:str, n:int) -> str:
    return s * n
以上就是python函数的类型注释了, 括号内参数s:str表示一个s接收一个str类型的数据, 参数n:int表示n接收一个int类型
的数据, -> 表示返回一个str类型的数据(但仅仅是注释, 使开发者希望使用者这样使用该函数, 但不代表必须要按照注释的数据类型传参)
默认参数注释: 如果需要使用默认参数注释可以这么写
def times(s:str = 'hello', n:int = 5) -> str:
    return s * n
列表参数注释: 如果我们期待的参数类型是列表可以这么写
def times(s:list, n:int = 5) -> list:
    return s * n
列表参数注释: 如果我们期待的参数类型是列表, 且期望列表中的数据都是int, 如下
def times(s:list[int], n:int = 5) -> list:
    return s * n
字典参数注释: 如下
def times(d:dict[str, int], n:int = 5) -> list:
    return list(s.keys()) * n

===[内省]===
我们在程序运行的时候想知道一个函数的名字, 我们可以使用__name__来获取
比如:
def times(d:dict[str, int], n:int = 5) -> list:
    return list(s.keys()) * n
times.__name__ 返回的就是'times'
使用annotations查看函数的类型注释, times.__annotations__ 返回的就是{'d': dict[str, int], 'n': <class 'int'>, 'return': <class 'list'>}
查看函数文档使用doc, 比如 exchange.__doc__ 返回 '\n功能：汇率转换，美元--->人民币\n参数：\n-dollar 美元数量\n-rate 汇率， 默认值是6.32 (2023-07-15)\n'





'''