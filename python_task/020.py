r'''
0. 列表的 extend() 方法是否支持使用字符串来扩展列表？
答: 可以, 列表的extend()方法可以使用字符串来扩展列表

1. 请问下面代码是否会报错？
答: 
s = [1, 2, 3]
s.append([4, 5, 6])
答: 不会, 这样相当于把列表[4, 5, 6]添加到 列表s中, 结果为 s = [1, 2, 3, [4, 5, 6]]

2. 请将下面代码改为使用列表的 insert() 方法实现。
s = [1, 2, 3, 4, 5]
s.append(6)
答: 
s.insert(len(s), 6)

3. 请问下面代码执行后，列表 s 的内容是什么？
s = [1, 2, 3, 4, 5]
s.extend(["FishC"])
答: [1, 2, 3, 4, 5, "FishC"]

4. 请使用切片的语法，实现与下面代码相同的效果。
s = [1, 2, 3, 4, 5]
s.append("上山打老虎")
s
[1, 2, 3, 4, 5, '上山打老虎']
答:
s[len(s):] = ['上山打老虎']

5. 请使用切片的语法，实现与下面代码相同的效果。
s = [1, 2, 3, 4, 5]
s.extend("上山打老虎")
s
[1, 2, 3, 4, 5, '上', '山', '打', '老', '虎']
答: s[len(s):] = '上山打老虎'

6. 请问下面代码执行后，列表 s 的内容是什么？
s = [1, 2, 3, 4, 5]
s[len(s)-2:] = [2, 1]
答: s = [1, 2, 3, 2, 1]

----动动手----
0. 请编写一个程序，判断给定的字符串 s 中括号的写法是否合法。
条件：
字符串仅包含 '('、')'、'['、']'、'{'、'}' 这三对括号的组合
左右括号必须成对编写，比如 "()" 是合法的，"(" 则是非法的
左右括号必须以正确的顺序闭合，比如 "{()}" 是合法的，"{(})" 则是非法的'''
'''s = input("请输入测试字符串：")

# 创建一个特殊列表
stack = []
   
for c in s:
    # 如果是左括号，那么添加到特殊列表中
    if c == '(' or c == '[' or c == '{':
        stack.append(c)
    # 如果是右括号的情况
    else:
        # 如果碰到右括号，但特殊列表中没有左括号，那么肯定是非法的
        if len(stack) == 0:
            print("非法T_T")
            break
   
        # 逐个给出 c 对应的右括号 d
        if c == ')':
            d = '('
        elif c == ']':
            d = '['
        elif c == '}':
            d = '{'
   
        # 对比 d 和从特殊列表尾部弹出的元素
        if d != stack.pop():
            print("非法T_T")
            break
else:
    # 如果循环走完，特殊列表不为空，那么肯定是左括号比右括号多的情况
    # 那肯定有同学会问：右括号比左括号多的情况在哪里判断？
    # 小甲鱼答：在上面 d != stack.pop() 的判断中已经可以排除了~
    if len(stack) == 0:
        print("合法^o^")
    else:
        print("非法T_T")'''



import copy

string = input('请输入测试字符')
list_1 = []
list_1.extend(string)
list_1_light = len(list_1)
if list_1_light % 2 != 0 or list_1_light == 0:
    print('非法')
    exit()
list_range = list_1_light / 2
list_2 = copy.deepcopy(list_1)
print(list_range)

for i in range(int(list_range)):
    if i ==0 and (list_1[i] == ')' or list_1[i] ==']' or list_1[i] =='}'):
        print('非法')
        break
    if list_1[int(list_range) - 1] == ')' or list_1[int(list_range) - 1] ==']' or list_1[int(list_range) -1 ] == '}':
        print('非法')
        print('这是第',list_range,'个元素', '值为', list_1[int(list_range) - 1])
        break
    if list_1[i] == '{':
        list_1[i] = '}'
    if list_1[i] =='(':
        list_1[i] = ')'
    if list_1[i] == '[':
        list_1[i] =']'
    #print('i', list_1[i],'======','pop',list_2.pop())
    if list_1[i] == list_2.pop():
        continue
    else:
        print('非法')
        break
else:
    print('合法')
    


string = input('请输入测试字符')
str_list = []
_ = ''

for i in string:
    if i == '(' or i == '[' or i == '{':
        str_list.append(i)
    else:
        if len(str_list) == 0:
            print('非法')
            break
        if i == ')':
            d = '('
        if i == ']':
            d = '['
        if i == '}':
            d = '{'
        if d == str_list.pop():
            continue
        else:
            print('非法')
            break
else:
    if len(str_list) == 0:
        print('合法')
    else:
        print('非法')


        