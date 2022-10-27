'''
分支结构判断
1, 判断一个条件，如果这个条件成立, 就立即执行其中包含的代码块或语句
if condition:
    statement(s)


2, 判断一个条件, 如果条件成立, 就执行其包含的语句或代码块; 如果条件不成立, 就执行另外的语句或代码块
if condition:
    statement(s)
else:
    statement(s)


3, 判断多个条件, 如果第一个条件不成立, 则继续判断第二个条件, 如果第二个条件还不成立, 则继续判断第三个条件；如果某一个条件成立后, 即执行条件成立后的语句, 后面的不再进行判断和执行
if condition:
    statement1(s)
elif condition:
    statement2(s)
elif condition:
    statement3(s)


4, 第四种是在第三种的情况下加一个else, 即表示上面所有的条件都不成立的情况下执行else下的代码
if condition:
    statement1(s)
elif condition:
    statement2(s)
elif condition:
    statement3(s)
else:
    statement(s)


5, 条件表达式格式
(条件成立所执行的代码) if (条件) else (条件不成立执行的代码) 例如：
age = 18
print('欢迎您来') if age > 17 else print('禁止访问') 

分支结构的嵌套
if condition:
    if condition:
        statement(s)
    else:
        statement(s)
else:
    if condition:
        statement(s)
    else:
        statement(s)




=========================================================我是一条分割线=====================================================================================


while循环 ---  语法结构

while 后面的条件成立的情况下, 会一直重复执行while 下面的代码
while condition:
    statement(s)


while 可以设计一个死循环, 让程序一直执行下去, 通常搭配break、continue语法一块使用
while True:
    statement(s)
    if condition:
        break

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        coutinue
    print(i)

 
while 还可搭配 else使用, 来检测循环退出的情况, 比如:
day = 1
while day <= 7:
    answer = input('你今天有好好学习吗？')
    if answer != '有':
        break
    else:
        day += 1

else:
    print('非常棒， 你已经连续7天了')


while 循环搭配else使用时, 如果条件不满足不走循环体内的代码, 就是走else下的代码, 如果是break循环则不会走else下的代码(for ...else...基本一样)


循环的嵌套结构
双层循环或者多层循环  例如九九乘法表
二双层循环中的break每次只跳出一层循环体, 跳出对应循环的那一层循环



'''
class multiplication_table:                   
    def while_loop_multiplication_table():
        a = 1
        while a <= 9:
            b = 1
            while b <= a:
                print(b, 'x', a, '=', b * a, end = ' ')
                b += 1
            a += 1
            print('\n')

    def for_loop_multiplication_table_1():
        a = 1
        for i in range(9):
            b = 1
            for k in range(a):
                print(b, 'x', a, '=', b * a, end = ' ')
                b += 1
            a += 1
            print('\n')

    def for_loop_multiplication_table_2():
        a = 1
        for i in range(9):
            for k in range(a):
                print(k + 1, 'x', a, '=', (k + 1) * a, end = ' ')
            a += 1
            print('\n')
    
    def for_loop_multiplication_table_3():
        for i in range(9):
            for k in range(i + 1):
                print(k + 1, 'x', i + 1, '=', (k + 1) * (i + 1), end = ' ')
            print('\n')

multiplication_table.for_loop_multiplication_table_1()
multiplication_table.for_loop_multiplication_table_2()
multiplication_table.for_loop_multiplication_table_3()
multiplication_table.while_loop_multiplication_table()


'''
for循环 ---  语法结构
for 变量 in 可迭代对象:
    statement(s)

可迭代对象：指那些元素能被单独提取出来的对象 例如字符串

for 循环一样可以搭配continue和break使用

'''
a = 0
for i in range(1,1000001):
    a += i

print(a)

for i in range(2, 10):
    for n in range(2, i):
        if i % n == 0:
            print(i, '=', n, '*', i // n)
            break
    else:
        print(i, '是素数')

