'''
[异常]
由于语法或者其他原因导致的报错, 我们可以称之为异常

[处理异常]
try-except
语句结构
try:
    # 检测范围
except [expression [as identifier]]:
    # 异常处理代码

例如:
try:
    1 / 0
except:
    print('出错了')
就会输出 出错了

精准定位异常(表示如果异常符合我们的预期则做出对应处理, 否则不处理), 例如:
try:
    1 / 0
except ZeroDivisionError:
    print('出错了')
就会输出  出错了, 因为我们是捕获[ZeroDivisionError], 而报错原因刚好是因为[ZeroDivisionError], 所以能够精准捕获, 假如是下面的代码, 该报错还是报错

try:
    520 + 'fishc'
except ZeroDivisionError:
    print('出错了')
这里不会输出 '出错了', 而是报错, 原因是因为数字不能和字符串相加, 因为我们是判断如果出了异常, 并且异常是 ZeroDivisionError, 他才会执行print的内容


我们也可以在这个指定异常的后面加上一个可选的 as, 将错误的原因提取出来, 例如: 
try:
    1 / 0
exceept ZeroDivisionError as e:   # 把错误原因给到 e
    print(e)                      # 打印e, 就代表打印错误原因


我们也可以做多个异常的处理, 假如我们认为如果出现了两种或多种异常的是时候, 我们需要捕获多个异常, 例如:
try:
    1 / 0
    520 + 'fishc'
except (ZeroDivisionError, TypeError):
    print('出错了')
这里要注意, try 语句后如果有多行代码, 而第一行出了错, python会执行except下的的代码, 就不会执行try语句第一行后面的代码了

也可以单独处理多个不同的异常, 使用多个except 语句就可以 例如:
try:
    1 / 0
    520 + 'fishc'
except ZeroDivisionError:
    print('出错了, 是因为除数不能为0')
except TypeError:
    print('类型错误')
except ValueError:
    print('值不正确')
这里会直接输出'出错了, 是因为除数不能为0', 因为代码走到 1 / 0时直接跳到到了捕获异常的代码处理下,  后面的520 + 'fishc'不会被执行

try-except-else
try:
    被检测的代码块
except:
    检测到异常后执行的代码块
else:
    没有异常发生, 执行的代码块

try-except-else-finally
try:
    被检测的代码块
except:
    检测到异常后执行的代码块
else:
    没有异常发生, 执行的代码块
finally:
    无论有有没有异常, 都会执行的代码块


try-except
try:
    检测范围
except:
    收尾工作执行的代码

[raise]语句
raise 可以生成一个异常, 但不能生成一个不存在的异常
raise ValueError('值不正确')
raise FishcError('出错了')  像这样就不行

[assert]语句
assert 也是引发一个异常, 但是assert只能引发一个叫做AssertionError的异常
a = 'fishc'
assert a == 'fishc'  不会出错
assert a == 'aaaaaa'  这里就会抛出AssertionError

利用异常来实现 goto
try:
    while True:
        while True:
            for i in range(10):
                if i > 3:
                    raise
                print(i)
            print('被跳过')
        print('被跳过')
    print('被跳过')
except:
    print('到这里来了')
这里的原理是, 在try 语句下面的循环中, 达到条件的话引发一个异常, 直接就会执行except下面的语句, 不需要多层循环一层一层跳出了



'''

