r'''
----问答题----
0. continue 语句和 break 语句都能够跳出循环体，那么它们的区别是什么呢？
答: continue 是跳过本次continue 后面的代码, 重新回到循环的最上面; 而break 则是跳出循环体, 结束循环

1. 在不上机的情况下，你能看出下面代码会打印多少次 "FishC" 吗？
i = 0
j = 9
while i < j:
    i += 1     
    j -= 1     
    print("FishC")
答: 打印 5 次 FishC


2. 你觉得 while-else 语法存在的意义是什么？
答 : 存在即合理


3. 你能看出下面代码存在什么问题吗？
i = 0
while i < 10:
    if i % 2 == 0:
        continue
    i += 1
    print(i)
答: 代码永远走不到 i += 1, 会死循环 i < 10, 条件成立, 进入循环 此时判断 i % 2 是否等于0, 此时条件成立, 直接continue, 回到循环最上面, 去判断 i < 10


4. 请看下面代码，当 break 语句执行之后，程序是跳转到位置 1 还是位置 2 呢？
day = 1
while day <= 7:
    while hour <= 8:
        print("今天, 我一定要坚持学习8个小时!")
        hour += 1
        if hour > 1:
            break
    # 位置1
    day += 1
# 位置2
答: break后会跳出循环体, 代码会走到位置1

5. 下面代码存在两个问题，细心的你发现了吗？
while True:
    command = input("请输入命令(exit/pow):")
    if command == "pow":
        base = input("请输入底数：")
        exp = input("请输入指数：")
        pow(base, exp)
    elif command == "exit":
        continue

答:第一个问题是pow计算的时候需要输入int, 而上面代码中base, 和exp接收的时候是字符串, 没有进行int转换; 第二个问题是 elif command == "exit": 的时候, 应该是用braek


---动动手----
0. 将九九乘法表倒过来打印
'''
x = 1
while x <= 9:
    y = 9 
    while y >= x:
        print(y,'x', x, '=', x * y, end = '  ')
        y -= 1
    x += 1
    print('')

r'''
1. 找出 10 以内的所有素数，如果不是素数，请打印出该合数对应的乘积公式，要求代码实现效果如下图

'''
'''for i in range(2, 10):
    for k in range(2, i):
        if i % k == 0:
            print(i, '=', k, '*',  i // k)
            break 
    else:
        print(i, '是素数')'''
            

'''for i in range(2, 10):
    if i == 2:
        print(i,'是素数')
    for k in range(2, i):
        if i % k == 0:
            print(i, '=', k ,'*', i // k)
            break
        else:
            print(i,'是素数')
            break'''


s = 2
while s < 10:
    d = 2
    while d < s:
        if s % d == 0:
            print(s, '=', d, 'x', s // d)
            break
        d += 1
    else:
        print(s,'是素數')

    s += 1



