r'''
----问答题----

0. 请问 6 / 2 的结果是一个整数还是浮点数呢？
答: 是一个浮点数, 因为python中默认是整数除法运算后得到浮点数, 小数是以浮点数的形式进行存放的

1. 请问为什么会出现下面的计算结果:
0.1 + 0.2 - 0.2
0.10000000000000003
答: python 的浮点数之所以是有误差的, 是因为python 采用IEEE754的标准来存储浮点数的, 所以会产生一定精度上的误差
如果需要做到 100% 精确计算浮点数，请使用 decimal 模块

2. 凭借自己的聪明才智，你觉得为什么浮点数的存储会存在“误差”？
答: 浮点数本身就不是百分百精确的; 而且浮点数的位数可以是无限的，但计算机的内存和硬盘确是有限的，用有限的资源来描述无限的内容，本身就是一个悖论

3. 请问下面代码存在什么问题？
age = 18
message = "祝小甲鱼" + age + "岁生日快乐^o^"
答: age 是整数, 整数无法跟字符串的数据类型进行加减运算, 会报错

4. 请问在 Python 中，浮点数 1.0 + 2.0 是否等值于整数 3?
答: 如果判断类型的话, 那么是不相等的; 如果是判断值是否相等的话, 那么是相等的, 另外，当浮点数相加的结果等于整数时，偏差则不会出现，比如 0.1 + 0.2 
会出现偏差，这个我们在视频中已经演示过了，但 0.1 + 0.2 + 0.7 却能得到整数答案 1.0

5. 请写出科学计数法 3.14e5 等值的浮点数。
答: 3.14e5相当于3.14 乘以 10的 5次方  就等于3.14 * (10 ** 5) = 314000.0 


----动动手----
0. 表达式 0.1 + 0.1 + 0.1 - 0.3 看似乎很傻，小学生都会，但 Python 可能搞不定，如下图所示，结果是一个非常奇葩的
数值……请使用恰当的方式计算出正确的结果。
'''
import decimal
a = decimal.Decimal('0.1')
b = decimal.Decimal('0.1')
c = decimal.Decimal('0.1')
d = decimal.Decimal('0.3')
print(a + b + c - d)

r'''
1. 模拟抛硬币的实验
'''
from itertools import count
import random
i = 0
counts = input('请输入抛硬币的次数')
counts = int(counts)
print("开始抛硬币实验：")
while i < counts:
    num = random.randint(1, 10)
    if num % 2:
        print('正面', end = '')
    else:
        print('反面', end = '')
    i += 1