'''
0. 代码出错，必然会抛出异常，对吗？
答: 是的, Python 通过提供异常机制来识别及响应错误

1. 请问出现异常，就说明是代码出错了，对吗？
答: 不一定, 比如迭代器，它就会在最后一个元素被获取之后，抛出 StopIteration 异常（它只是表示读取完毕，但并不是代码出错）

2. Python 通过 try-except 语句来执行异常机制，请问该语法结构的优点是什么？
try:
    检测范围
except [expression [as identifier]]:
    异常处理代码
答: 代码报错后会终止执行, 而使用try-except捕获异常, 可以做异常处理, 不至于程序终止执行, 该语法结构有效地分离出程序中的异常
处理代码和正常业务代码，使得程序代码更为优雅，并提高了程序的健壮性。

3. 请问下面的代码中，这个 error 是字符串类型吗？
>>> try:
...     520 + 'FishC'
... except TypeError as error:
...     print(f"出错啦，错误原因是：{error}")
...        
出错啦, 错误原因是: unsupported operand type(s) for +: 'int' and 'str'
答: 不是, error 是 <class 'TypeError'>

4. 如果试图引用一个未曾定义过的变量, Python 会抛出什么异常？
答: 会引发 NameError 异常

5. 如果试图访问一个对象中不存在的属性, Python 会抛出什么异常？
答: 如果访问一个对象中不存在的属性的话, 会引发 AttributeError异常

===========
0. 利用异常捕获机制，使用 while 循环语句来实现 for 循环语句的功能。
>>> x = "FishC"
>>> for each in x:
...     print(each)
...        
F
i
s
h
C
'''
x = 'fishc'
_ = iter(x)
while True:
    try:
        print(next(_))
    except:
        break


'1. 利用 Python 异常机制，编写一个检查用户输入语句是否有错误的程序。'
'要求'
'A. 程序能够识别出 “语法错误”、“索引错误”、“变量未定义”、“除数为0” 和 “传入参数类型不恰当” 这几个错误类型。'
'B. 只有通过 Ctrl + C 快捷键才能正常退出程序'
'C. 程序实现请参考以下截图'

def check_except(statement):
    try:
        eval(statement)
    except (SyntaxError, IndexError, NameError, ZeroDivisionError, ValueError, TypeError, KeyboardInterrupt) as Error:
        if type(Error) == SyntaxError:
            print(f'错误: 语法错误')
        elif type(Error) == IndexError:
            print(f'错误: 索引错误')
        elif type(Error) == NameError:
            print(f'错误: 未定义变量')
        elif type(Error) == ZeroDivisionError:
            print(f'错误: 除数不可以为0')
        elif type(Error) == ValueError:
            print(f'错误: 传入的值类型不恰当')
        elif type(Error) == TypeError:
            print(f'错误: 类型错误')
    else:
        print(eval(statement))
try:
    expression = input('请输入一行语句')
except KeyboardInterrupt:
    print('\n退出程序')
    exit()
check_except(expression)
