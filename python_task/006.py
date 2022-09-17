r'''
----问答题---

0. 请问下面代码是打印 "YES" 还是 "NO"?
if 'FishC' == "fishc":
    print("YES")
else:
    print("NO")
答: 打印NO, 因为 'FishC' 不等于 'fishc', 所以走else 条件分支

1. 请问下面代码会打印多少个 "Yo~"?
yoo = 222
while yoo < 233:
    print("Yo~")
答: 会一直打印, 因为yoo = 222, 而while 循环是有判断条件的, while yoo < 233 的时候, 打印 'yo', 这个while循环没有出口, yoo 的值也不会发生变化
所以, 会一直打印

2. 请问下面代码会打印多少个 "Man"?
while 1 + 1 == 2:
    print("Man")
答: 会一直打印, 原理同上一题, 

3. 请问下面代码存在什么问题？
age = input("请输入你的年龄：")
if age <= 18:
    print("你已经成年^o^")
else:
    print("对不起, 你还未成年T_T")
答: input()函数接收后返回的是一个字符串, 需要把它进行转换, 转换为int才能进行比较 age = int(age), 还有一个问题是 判断条件为年龄是否小于等于18,
如果小于等于18就打印你已经成年了, 所以必然是判断条件写错了, 可以改为  if age >= 18:

4. 下面代码是一个死循环（永远不会结束）,请添加一个语句,使其打印一遍 "iloveFishC.com" 后退出循环。
while True:
    print("iloveFishC.com")
答: 添加一个 break 语句在print()的下方就行了, 进循环后, 走到break 就直接退出循环了

5. 请阅读下面代码,根据你的理解,代码中问号（？？？）处应该填写什么内容？
x = input("请输入一个数字：")
x = int(x)

if x > 20:
    print("大于20")
else:
    if x < 10:
        print("小于10")
    else:
        print("？？？")
答: 此数字处于大于等于10 小于 等于20 之间

----动动手----
0. 编写一个成绩评级程序,要求用户输入分数,程序返回对应的评级。
分数 < 60,D
60 <= 分数 < 80,C
80 <= 分数 < 90,B
90 <= 分数 < 100,A
分数 == 100,S
'''
score = int(input('请输入你的分数, 输入数字哟~~'))

if score < 60:
    print('你的成绩为D')
elif 60 <= score < 80:
    print('你的成绩为C')
elif 80 <= score < 90:
    print('你的成绩为B')
elif 90 <= score < 100:
    print('你的成绩为A')
elif score >= 100:
     print('你的成绩为S')

r'''
1. 修改上一题的代码, 让程序可以不断接收输入, 直至用户输入小写字母 e 结束程序。
'''
while True:
    score = input('请输入你的分数, 若要退出输入 e ')
    if score == 'e':
        break
    else:
        score = int(score)
        if score < 60:
            print('你的成绩为D')
        elif 60 <= score < 80:
            print('你的成绩为C')
        elif 80 <= score < 90:
            print('你的成绩为B')
        elif 90 <= score < 100:
            print('你的成绩为A')
        elif score >= 100:
            print('你的成绩为S')