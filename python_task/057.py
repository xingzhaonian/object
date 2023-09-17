'''
0. 异常处理的两个常见组合是什么？
答: 1,
try:
    被检测是否会有异常的代码块
except:
    出现异常执行的代码块
else:
    不出现异常执行的代码块
finally:
    无论是否有异常, 都会执行的代码块
2,
try:
    检测范围
finally:
    收尾工作执行的代码

1. 我们知道，利用 try-except-else 的语法，可以让代码段在没有发生异常的时候去执行 else 语句的内容。那如果不使用 else，有没有办法做到相同的效果呢？
>>> try:
...     1 / 1
... except:
...     print("逮到异常~")
... else:
...     print("没有异常~")
没有异常~
答: 
try:
    1 / 1
    print('没有异常')
except:
    print("逮到异常~")


2. 在学习文件操作的时候，小甲鱼推荐大家使用 with 语句管理文件操作的上下文，原因是 with 语句可以确保文件被正常关闭（不会导致写入数据的丢失）
那么学完异常这一节课，我们又有另外的办法可以做到确保文件的正确关闭，请问如何做呢？
答:
try:
    with open('D:\\python_file\\testtry.txt', 'w') as f:
        f.write('测试一下')
finally:
    f.close()

3. 请问下面代码返回的 True 还是 False？
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
答: False

4. raise 语句可以不添加具体异常直接使用吗？
答: 可以, 会引发一个RuntimeError 错误

5. 执行下面代码，会打印 “内部异常~”，但 “外部异常~” 并不会打印！
在不修改代码的情况下，请问有什么办法可以让它只打印 “外部异常~”，而不打印 “内部异常~”？
import time
    
try:
    for i in reversed(range(1, 4)):
        print(i)
        time.sleep(1)
    try:
        520 + "FishC"
    except:
        print("内部异常~")
except:
    print("外部异常~")
答: 加个 raise 就行了
import time
try:
    for i in reversed(range(1, 4)):
        print(i)
        time.sleep(1)
    raise
    try:
        520 + "FishC"
    except:
        print("内部异常~")
except:
    print("外部异常~")

6. 请将下面 assert 修改为异常的实现方式
def myfunc(x):
    assert x < 0
    return x ** 2
答:
def myfunc(x):
    try:
        assert x < 0
    except AssertionError:
        pass
    else:
        return x ** 2

7. 大家还记得我们在学习分支与循环的时候，说 break 语句只能跳出一层循环体，所以当我们希望在达成条件之后跳出多层循环
就需要借助一个标识变量，然后经过多次跳跃来实现，如下：
>>> out = False
>>> for i in range(1000):
...     for j in range(1000):
...         for k in range(1000):
...             if i * j * k == 12321:
...                 print(f"{i} * {j} * {k} = 12321")
...                 out = True
...             if out:
...                 break
...         if out:
...             break
...     if out:
...         break
...
1 * 37 * 333 = 12321
答:
out = False
try:
    for i in range(1000):
        for j in range(1000):
            for k in range(1000):
                if i * j * k == 12321:
                    raise
                    print(f"{i} * {j} * {k} = 12321")
                    out = True
                if out:
                    break
            if out:
                break
        if out:
            break
except:
    print(f"{i} * {j} * {k} = 12321")


8. 动手试一下, raise 如果不带任何参数，抛出的异常叫啥名字？
答: RuntimeError

9. 请问 raise、raise exception 以及 raise exception(info)，这三者在使用上有什么区别？
答: raise: 单纯抛一个异常出来, 名字为 RuntimeError
raise exception: 给错误一个命名, 名字为 Exception, except 可以去检测这个异常的命名
raise exception(info): 给错误一个命名, 名字为 Exception, info可以写具体报错内容, 更能一眼看出来是哪里出了问题

10. 请编写代码，实现在捕获异常之后，打印一句 “出错啦”，再重新抛出相对应的异常（注意，这里我们说的异常并不特指具体的哪一类，而是泛指所有的异常）。
'''
try:
        1 / 0
except:
    print("出错啦~")
    raise
