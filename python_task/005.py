r"""
----问答----
0. 在 Python 中，一个等于号（=）和两个等于号（==）的功能是一样的吗？
答: 不一样, 因为一个等号相当于赋值操作, 二两个等号相当于判断 两个等号两侧的值是否相等

1. 请问下面代码为什么会报错？
3 < = 4
SyntaxError: invalid syntax
答: 因为 小于等于没有贴在一起, python 无法识别到语法内容, 所以语法报错了

2. 请问下面代码返回的 True 还是 False?
3 <= 5 >= 4
答: 返回True , 因为多个比较符连用的时候代表  3 <= 5 and 5 >= 4, 两边结果为True, 所以为True
多个比较符连用时, 比如  3 > 5 <= 6 > 7 < 7 >= 9, 相当于 3 > 5 and 5 <= 6 and 6 > 7 and 7 < 7 and 7 >= 9
3 > 5 and 5 <= 6 and 6 > 7 and 7 < 7 and 7 >= 9, 第一个结果返回True, 第二个结果返回True, 第三个结果返回False
后面的就不用看了, 只要有一个False 就直接返回False, 因为他们的逻辑是相当于 and 而不是 or

3. 请问下面代码返回的值是什么？
1 + 1 >= 2
答: 返回 True, 因为 1 + 1 = 2, 2 >= 2 是成立的, >= 的意思是说小于或者等于都为True

4. 请问下面代码存在什么问题？
if guess == 8:
    print("你是小甲鱼心里的蛔虫嘛？！")
   print("哼，猜中了也没奖励！")
else:
    print("猜错啦, 小甲鱼现在心里想的是8! ")
答: 缩进有问题, 第三行的缩进不对, 代码会报错

5. 请问下面 A、B、C、D 四个表达式中，哪些将返回 True?
A. 'FishC' == '''FishC'''
B. "小甲鱼" == "小乌龟"
C. 520 == int(520.1314)
D. 9 == int(9.99)
答: A 返回True, 因为都是字符串类型的数据, 而且字符串的数据都一模一样; B 返回False, 因为虽然都是字符串, 但是字符串的数据不一样, 不相等, 返回False
C 返回True, 因为int(520.1314) 是转换过数据类型的, 520.1314转换为int数据类型就是等于 520, 浮点数转换为int后会把小数点后面的舍掉, 只保留小数点
前面的数字, 所以int(520.1314) 就等于520  D 返回True, 原理同C 题目

----动动手----
0. 请按下面要求实现程序
要求A: 打开 IDLE 的编辑模式
要求B: 将下面代码输入Powered 
要求C: 将代码保存到桌面，并命名为 test
要求D: 执行程序Powered by
num1 = input("请输入第一个整数：")
num2 = input("请输入第二个整数：")

if num1 < num2:
    print("第一个数比第二个数小！")

if num1 > num2:
    print("第一个数比第二个数大！")

if num1 == num2:
    print("第一个数和第二个数一样大！")


"""
num1 = input('请输入第一个整数：')
num2 = input('请输入第二个整数: ')
num1 = int(num1)
num2 = int(num2)
 
if num1 < num2:
    print('第一个数比第二个小')
if num1 > num2:
    print('第一个数比第二个大')
if num1 == num2:
    print('第一个数和第二个数一样大')



num1 = input('请输入第一个整数：')
num2 = input('请输入第二个整数: ')
 
if int(num1)  < int(num2):
    print('第一个数比第二个小')
if int(num1) > int(num2):
    print('第一个数比第二个大')
if int(num1) == int(num2):
    print('第一个数和第二个数一样大')




num1 = int(input('请输入第一个整数：'))
num2 = int(input('请输入第二个整数: '))
if num1 < num2:
    print('第一个数比第二个小')
if num1 > num2:
    print('第一个数比第二个大')
if num1 == num2:
    print('第一个数和第二个数一样大')
