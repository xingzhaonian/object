r'''
----问答题----
0. 请问 1 + 2 / 3 跟 1 + 2 // 3 的结果有何不同?
答: 1 + 2 / 3 相当于 2除以3然后加1, 而1 + 2 // 3则是 2除以3的商加1, 至于结果1 + 2 / 3= 1.6666666666666665, 而  1 + 2 // 3 = 1
一个是float, 一个是int; 对于 除法 / 来说, 结果不管是否为整数都将以浮点数的形势存放

1. 无论是真除法(/)还是地板除(//),都需要注意的一个问题是什么?
答: 都需要注意 除数是不能为0的,  被除数 / 除数  =  商.....余数

2. 请问 1 +- 2 - + 3 *-4 /+ 5, 计算结果是?
答: -1.4

3. pow(3, 4, 5) 的含义是？
答: 3 的 4 次方 % 5, 也就是 81 % 5 等于1

4. (x // y) * y + (x % y) 的结果是什么？
答: x; 因为地板除的结果乘以除数 + 余数 = 被除数

5. 如果给 int() 函数传入一个浮点数参数,那么 int() 是简单暴力地将小数部分裁掉
(比如 int(9.99) 的结果等于 9)……可是我们更习惯的是使用“四舍五入”的方式来取整。如果不借助其它函数,你能够单纯使用 int() 函数来实现吗？
答: 可以, int(num + 0.5)就可以实现了


----动动手----
0. 使其功能变为计算 1000000 以内所有偶数的和。
'''
i = 0
num = 0
# 修改为10000
while i <= 10000:
    if i % 2 == 0:
        print(i, "是偶数！", num)
        num += i
    i = i + 1
print("1000000 以内所有偶数的和是", num)

r'''
1. 舍罕王的失算
故事背景:
相传国际象棋是古印度舍罕王的宰相达依尔发明的。
舍罕王十分喜爱国际象棋,便决定让宰相自己选择何种赏赐。这位聪明的宰相指着 8 * 8 共 64 格的象棋棋盘说：陛下,请您赏给我
一些麦子吧。就在棋盘的第 1 格中放 1 粒,第 2 格放 2 粒,第 3 格放 4 粒,以后每一格都比前一格增加一倍,依此放完棋盘上 64 格,我就感激不尽了……
舍罕王听了达依尔这个“小小”的要求,便让人扛来一袋麦子,他要兑现许诺。结果,在给达依尔发放麦子时,舍罕王发现他要给达依尔的麦子比自己想象的要多得
多,一袋麦子是远远不够的……

'''

wheat = 0
count = 0
for i in range(1, 65):
    if i == 1:
        wheat += 1
    else:
        wheat *= 2
    print('第{}个格子放小麦{}个'.format(i, wheat))
    count += wheat
    print('第{}次相加等于{}'.format(i, count))

print("舍罕王应该给达依尔{}粒麦子！".format(count))