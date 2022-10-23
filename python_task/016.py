r'''
----问答----
0. 我们知道在游戏运行后，通常是玩家中断游戏或者主角被打败了，才会退出游戏。
那么现在让你来开发一个游戏，你觉得应该如何实现这个机制（可以画流程图，也可以简单概述）？
答:

                玩家主角血量 = 100
                      ↓
                      ↓
                      ↓
                      ↓
                 玩家血量为0
                      ↓
                      ↓
                      ↓
                      ↓
                触发退出游戏机制      
'''
HP = 100
for i in range(HP):
    HP -= 1
    if HP == 0:
        print('玩家血量为', HP,'游戏退出')
        break

r'''
1. 请问下面代码存在什么问题？
love = 'yes'
while love = 'yes':
    love = input("今天你还爱我吗：")
答: 判断条件错误, while love = 'yes', 这里应该双 ==, while love == 'yes'

2. 如果不上机，你能算出下面循环执行完毕之后，打印的值应该是多少吗？
i = 1
sum = 0
while i < 10:
    sum = sum + i
    i = i + 1
print(sum)
答: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45

3. 请问下面代码是否会构成一个死循环？
x = 9
while x:
    print(x)
    x -= 3
    x += 1
答: 会, 因为 x 每次自减3, 每次自加1, 所以, 判断条件进行时 x 没有等于0的时候, 循环不会退出


4. 当程序跑起来之后，如果发现是死循环，如何强制退出呢？
答: 可以使用 ctrl + c 来终止进程

5. 以下两段代码实现相同的功能，你觉得哪一段代码的实现更优雅？
password = ''
while password != "FishC":
    password = input("请输入密码：")
   
print("欢迎您来！")

while True:
    password = input("请输入密码：")
    if password == "FishC":
        break
   
print("欢迎您来！")

答: 感觉第二种是更加优雅点的, 比较符合正常人的思维逻辑


----动动手：----


0. 请编写一个程序，实现如下图所示的效果

'''
while True:
    slogan = input('请输入一个口号(输入stop 结束)')
    if slogan == 'stop':
        break
    else:
        print(slogan)

r'''
1. 抛硬币实验
a. 如果抛硬币的次数小于 100，则打印每次的结果，否则不打印
统计最终正面和反面的次数
'''
import random

count = int(input('请输入抛硬币的次数'))
print('开始抛硬币实验...')
i = count
positive = 0     # 正面次数
the_other_side = 0     # 反面次数
Front_consecutive_times = 0    # 正面连续次数
Number_of_consecutive_negative_sides = 0        # 反面连续次数
max_Front_consecutive_times = 0        # 正面最大连续次数
max_Number_of_consecutive_negative_sides = 0   # 反面最大连续次数
last_status = 0   # 上次状态, 初始为0,  1为正面,   2为反面



while count:
    random_number = random.randint(1,100)
    if random_number % 2 == 0:
        if i < 100:
            print('正面',' ', end = '', sep = ' ')
        positive += 1
        if last_status == 2:
            Front_consecutive_times = 0
        Front_consecutive_times += 1
        if max_Front_consecutive_times < Front_consecutive_times:
            max_Front_consecutive_times = Front_consecutive_times
        last_status = 1
    else:
        if i < 100:
            print('反面',' ',  end = '', sep = ' ')
        the_other_side += 1
        if last_status == 1:
            Number_of_consecutive_negative_sides = 0
        Number_of_consecutive_negative_sides += 1
        if max_Number_of_consecutive_negative_sides < Number_of_consecutive_negative_sides:
            max_Number_of_consecutive_negative_sides = Number_of_consecutive_negative_sides
        last_status = 2
    count -= 1


print('一共模拟了', i, '次抛硬币实验, 结果如下: ')
print('正面:', positive)
print('反面:', the_other_side)
print('最大正面连续次数:', max_Front_consecutive_times)
print('最大反面连续次数:', max_Number_of_consecutive_negative_sides)





