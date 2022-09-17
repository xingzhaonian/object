r'''
----问答题----

0. “所有使用算法生成的随机数,都是伪随机数！”,这种说法对吗？
答: 对, 没有什么真正的随机数; 真正意义上的随机数（或者随机事件）表现的分布概率随机产生的,其结
果是不可预测的,是不可重现的。而计算机中的随机函数是按照一定算法模拟产生的,其结果是确定的,是可
重现的。所以,用计算机随机函数所产生的“随机数”并不随机,而是伪随机数

1. 如果要使用 random 模块,第一步应该怎么做？
答: import random


2. 调用 random.randint(1, 10) 函数生成了一个随机数,是否有可能会出现 10 这个数？
答: 是有可能的,  random.randint(a, b) 返回一个随机整数, 范围在 a <= n <= b

3. 请自学 random 文档（传送门）,然后告诉小甲鱼下面这句代码的作用是什么？
random.choice("ilovefishc")
答: 随机返回ilovefishc中的任意一个字符串

4. 请问下面两个 print() 语句打印的结果是否相同,为什么？
import random

random.seed(1)
print(random.randint(1, 10), random.randint(1, 100), random.randint(1, 1000))

random.seed(1)
print(random.randint(1, 10), random.randint(1, 100), random.randint(1, 1000))
答: 答：完全相同,因为它们拥有相同的种子 , 解析：默认的情况下,random 使用当前操作系统的时间
作为随机数种子,所以产生的随机数看起来总是不会再现。但 random 同时允许我们通过技术手段“再现”伪随机数,那就
是提供相同的种子。注意,这是一种设计,并不是什么bug。



----动动手----
0. 请自学 random 文档（传送门）,并选择一个合适的函数,在 0~99 之间随机抽取一个偶数。





'''
import random
num = (random.randrange(0, 100, 2))

'''
1. 请自学 random 文档（传送门）,编写一个双色球的开奖模拟程序, 不知道双色球怎么玩的鱼油可以看下科普：
“双色球”每注投注号码由 6 个红色球号码和 1 个蓝色球号码组成。红色球号码从 1~33 中选择（由于每次抽取后
不放回,所以不会出现重复数字）；蓝色球号码从 1~16 中选择。
'''

import random
red_ball = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32] , k = 6)
blue_ball = random.randint(1, 16)

#print('开奖结果是:', red_ball[0], red_ball[1], red_ball[2], red_ball[3], red_ball[4], red_ball[5] )
#print('特别号码是', blue_ball)


red_ball_1 = random.sample(range(1, 34), 6)
blue_ball_1 = random.randint(1,16)
print('开奖结果是:', *red_ball_1)
print('特别号码是', blue_ball_1)