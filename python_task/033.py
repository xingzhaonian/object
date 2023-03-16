r'''
0. 在 Python 中，每一个对象都有三个基本属性，你知道是什么吗？
答: 在Python中每一个对象都有三个基本的属性, 它们分别为 id, type, value

1. 通过下面代码，是否可以证明字符串其实是属于可变序列？
>>> x = "Fish"
>>> x += "C"
>>> print(x)
FishC
答: 不可以, 使用id(object) 可以查看此对象的value变化后id是否为同一id, 如果是同一id, 说明其对象是可变的, 否则不可变

2. 如果两个对象 a 和 b 的 id 值相同，那么 a is b 的运算结果就一定是 True, 对吗?
答: 对, 两个对象都指向同一id; (is)和不是(is not)被称之为同一性运算符，用于检测两个对象之间的 id 值是否相等。

3. 请使用切片的语法实现相同与下面代码的结果。
>>> x = [1, 2, 3, 4, 5]
>>> del x[1:4]
>>> x
[1, 5]
答: y[1:4] = []

4. 请使用 del 语句实现相同与下面代码的结果。
>>> x = [1, 2, 3, 4, 5]
>>> x.clear()
答: del x[:]


动动手:
0. 判断子序列
给定字符串 s 和 t ，请编程判断 s 是否为 t 的子序列。
字符串的子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串（例如，"ace" 是 "abcde" 的子序列，而 "aec" 则不是）。
程序实现如下:
'''

parent_character = 'FiiisjjhkkCBA'
sub_character = 'FishC'
result_list = []
for i in range(len(parent_character)):
    for k in range(len(sub_character)):
        if parent_character[i] == sub_character[k]:
            if parent_character[i] in result_list:
                continue
            result_list.append(parent_character[i])
print(result_list)
if sub_character == ''.join(result_list):
    print('{}是{}的子序列'.format(sub_character, parent_character))
else:
    print(f'{sub_character}不是{parent_character}的子序列')

'''
1. 给定一个字符串 s, 请编程求出该字符串中的最大奇数。
举例:
输入: 43383
输出: 43383

输入:5926
输出:59

输入:966
输出:9

输入:64062
输出:0
'''
s = input('输入数字')
while int(s) % 2 == 0:
    s = s[:-1]
    if s == '':
        print(0)
        break
else:
    print(s)