r'''
----问答题----

0. 请问 Python 是否支持链式比较？
答: 可以, python 支持链式比较, 比如 4 > 5 < 7 < 0

1. 请问下面两段代码有什么区别呢？
A <<<if bool(250):
    print("Yeah, you are right.")
B <<<if 250:
    print("Yeah, you are right.")
答: Python 的真值测试它是会自动进行的，所以不使用 bool() 函数也没有任何问题

2. 在 Python 中, 所有的对象都可以进行真值检测, 对吗？
答: 对, 所有对象都支持真假检测

3. 请问下面表达式的值是什么？
not 3 == 5
答: True, 此处判断 3是否不等于5

4. 在 Python 中, True 和 False 两个关键字是完全等值于 1 和 0 的, 对吗？
答: 对 其实布尔类型其实就是特殊的整数类型，True 和 False 就是 1 和 0 的别称，但作为条件，使用 True 和 False 显然比 1 和 0 要更好理解

5. 请问下面代码打印的内容是什么？
print(5 > 3 and 4)
答: 打印4

6. 请问下面代码打印的内容是什么？
from fractions import Fraction
print(Fraction(1, 2) * 2)
答: 打印1 Fraction(a, b) 表示分子为 a，分母为 b 的分数，Fraction(1, 2) 就是二分之一的意思啦，所以乘以 2 的结果当然是等于 1

----动动手----
0. 请自学 fractions 文档, 并计算 1708227363155544/4636617128565048 约分后的值。
'''
import fractions
num_1 = fractions.Fraction(1708227363155544, 4636617128565048)
print(num_1)

r'''
1. 写一个程序, 判断给定年份是否为闰年。
'''
ordinary_yesrs = [] 
century_years = []
for i in range(1800, 2023):
    if i % 100 == 0 and i % 400 == 0:
        print('{}是世纪闰年'.format(i))
        century_years.append(i)
    else:
        if (i % 4 == 0) and (i % 100 != 0):
            print('{}年是普通闰年'.format(i))
            ordinary_yesrs.append(i)
print(len(ordinary_yesrs),ordinary_yesrs)
print(len(century_years),century_years)