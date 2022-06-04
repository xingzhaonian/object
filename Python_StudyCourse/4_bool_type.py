'''
bool类型只有两个值, True(真) 和 False(假)

以下是结果为False的所有状态：
被定义为False的所有对象: None和False, None表示为空,一无所有, False为假, 即False
值为0的数字类型: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
空的序列和集合: '', (), [], {}, set(), range(0)

'''

1 == True
0 == False
# True 和 False 是特殊的整数类形
print(True + False)
print(True - False)
print(True * False)
# print(True / False) 除数不能为0
print(False / True)

'''
逻辑运算符
运算符            含义
and              左边和右边同时为True, 结果才为True
or               左边或者右边有一个为True时, 结果就为True
not              如果操作数为False, 结果为True; 如果操作数为True, 结果为False
'''
a = 0
b = 10
c = 100

if a and b:
    print('条件为True,结果为:', a + b)
else:
    print('没进条件，无法相加')

if a or b:
    print('条件为True, 结果为:', a + b)
else:
    print('没进条件，无法想加')

not True
not False

'''
短路逻辑
从左往右,只有当第一个操作数的值无法确定逻辑运算的结果时,才对第二个操作数进行求值， 否则直接抛出结果 
'''

False or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9
False or 0 or 4 or 6 or 9
4

'''
优先级                     运算符                                                               描述
1                         (expressions),[expressions],{key:value},{expressions}                绑定或元组显示, 列表显示, 字典显示, 集合显示
2                         x[index], x[index, index], x(arguments), x.attribute                 下标, 切片, 函数调用, 属性引用
3                         await x                                                              Await表达式
4                         **                                                                   指数
5                         +x, -x, ~x                                                           正号, 负号, 按位翻转
6                         *, @, /, //, %                                                       乘法, 矩阵乘法, 除法, 地板除, 取余数
7                         +, -                                                                 加法, 减法
8                         <<, >>                                                               移位
9                         &                                                                    按位与
10                        ^                                                                    按位异或
11                        |                                                                    按位或
12                        in, not in, is, is not, <, <=, >, >=, !=, ==,                        成员测试, 同一性测试, 比较    
13                        not x                                                                布尔 '非'
14                        and                                                                  布尔 '与'
15                        or                                                                   布尔 '或'
16                        if, else                                                             条件表达式
17                        lambda                                                               Lambdab表达式
'''