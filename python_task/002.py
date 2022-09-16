'''
----问答----

0. IDLE 的交互模式和编辑器模式有什么区别？
答: 交互模式直接可以运行写的代码, 而编辑器模式则需要把代码写好再运行

1. 在课堂上敲过的代码中，除了 print() 和 input()，你觉得还有哪一个是 Python 的 BIF 内置函数？
答: int()

2. 请问 print() 和 Print() 的功能一样吗？
答: 不一样; print()是一个内置函数，可以打印输出参数内容, 而Print则是一个变量, 还是一个没有赋值的变量

3. 请统计一下 Python 一共有多少个 BIF 内置函数？
答:
①: len(dir(__builtins__))
②: import builtins
   len(dir(builtins))
   共68个

4. Tab 键除了用于缩进，你还发现它在 IDLE 中有什么特殊的功能吗？
答: tab 键在IDLE中可以当作四个空格使用, 也就是缩进; 还有就是可以自动识别并填充当前已经创建的变量和方法，或已经存在
的变量和方法

5. 请问下面代码为什么不能正常执行？
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)

if guess = 8:
    print("你是小甲鱼心里的蛔虫嘛？！")
    print("哼，猜中了也没奖励！")
else:
    print("猜错啦，小甲鱼现在心里想的是8！")
    
print("游戏结束，不玩啦^_^")
答: 因为   if guess = 8:  判断条件写错了, = 相当于赋值, 而判断是否相等要用 ==


----动动手----
0. 请在 IDLE 的交互模式中，计算一年有多少秒？
答: one_year = 60 * 60 * 24 * 365

1. 按下面要求修改课堂中的 game.py 代码。
a.让用户输入这次数学考试的成绩。
b.如果分数是 100 分，显示：好棒，你离女神又近了一步^_^
c.如果分数不是 100 分，显示：小子，想要幸福，就得努力！

答:'''
result = 100
while True:
    tamp = input('请输入本次考试成绩')
    try:
        tamp = int(tamp)
    except ValueError:
        print('请输入数字哦~~')
    finally:
        if type(tamp) == type(int()):
            break

if tamp >= result:
    print('好棒，你离女神又近了一步^_^')
else:
    print('小子，想要幸福，就得努力！')




