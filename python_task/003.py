'''
----问答----

0. Python3 虽然支持中文作为变量名，但有些大牛却不赞同这么做，你觉得他们的依据是什么？
答: 维护代码成本过高, 而且看起来像菜鸟, 不够国际化 internationalization

1. 以下哪个变量命名不正确？为什么？
(A)MM_520  (B)_MM520_  (C)520_MM  (D)_520_MM  (E)我M爱M你
答: C错误, 因为在python的变量和使用中有明确规定, 变量可以使用下划线打头, 也可以用英文字母打头, 也可以
中文字符打头, 但是不能用数字打头

2. 你觉得下面代码出错的原因是什么？
print(x)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
答: 因为变量 x 未被赋值, 没有存在, 找不到所以报错

3. 你觉得下面代码中, print() 函数会打印什么内容？
x = 520
x = 880
print(X)
答: 会报错, 细心一点 因为变量 X 未被赋值, 没有存在, 找不到所以报错 是print(X) 而不是print(x) 

4. 你觉得下面代码中, print() 函数会打印什么内容？
x, y, z = 3, 4, 5
x, y, z = y, x, z
print(x, y, z)
答: print(x, y, z) 输出 4, 3, 5  因为 x, y, z 又重新赋值了

5. 你觉得下面代码中, print() 函数会打印什么内容？
print("小甲鱼常说："Good good study, day day up!"") 
答: 会报错, 因为字符串都需要成双成对, 像这样的参数扔进去, 无法被python识别, 我们可以这样打印
print('小甲鱼常说："Good good study, day day up!"'), 利用单双引号的特性, 把单双引号区分开,
就可以正常输出双引号了, 反之则用双引号包裹起来输出单引号

6. 请填充下面图片中红色部分的代码，让 print() 函数可以按照要求打印字符串。
print('"Bruce Eckel say:"Life is short, let\'s learn Python."')

----动动手----
0. 请编写代码：使用变量(dpy)存放每年的天数(365)，变量(hpd)存放每天的小时数(24)，变量(mph)存
放每小时的分钟数，变量(spm)存放每分钟的秒数(60)，最后计算一年有多少秒，并将结果存放到变量(spy)中。
答: 
dpy = 365 
hpd = 24 
mph = 60
spm = 60 
spy = dpy * hpd * mph * spm

1. 请编写代码：使用 input() 函数让用户录入姓名，然后将名字保存到变量(name)中，最后使用 print() 函数打印出来

'''
name = input('请输入您的名字')
print('你好，' + name + '!')