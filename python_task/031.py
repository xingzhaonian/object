r'''
问答题
0. 请问下面代码会打印什么内容？
"{}, {}, {}".format("苹果", "香蕉", "梨")
答: 会打印 "苹果", "香蕉", "梨"

1. 请问下面代码会打印什么内容？
"{1}看到{0}就很激动！".format("小甲鱼", "漂亮的小姐姐")
答: "漂亮的小姐姐看到小甲鱼就很激动！"

2. 请问下面代码会打印什么内容？
"我叫{name}，我爱{0}。喜爱{0}的人，运气都不会太差^o^".format(name="小甲鱼", "python")
答: 会报错, positional argument follows keyword argument(位置参数跟随在关键字参数后面)

3. 请问下面代码会打印什么内容？
"{{0}}".format(1)
答: {0}

4. 请问下面代码会打印什么内容？
"{{{0}}}".format(1)
答: {{1}}

5. 请问下面代码会打印什么内容？
"{{{{{{0}}}}}}".format(1)
答: {{{0}}}

'''

r'''
动动手
0. 请编写一个程序，统计字符串中的单词个数（“单词”以空格进行分隔）
输入：（空字符串）
输出: 0

输入: Python
输出: 1

输入: I love FishC
输出: 3

'''
#text = input('请输入字符')
#text = text.split( )
#nums = len(text)
#print(nums)

r'''1. 请编写一个程序，将用户输入的字符串重新格式化，使得字母和数字相互分隔（即一个字母一个数字相互间隔）
举例：
输入: FishC1314
输出: F1i3s1h4C

输入: FishC520
输出: 字符串中数字和字母的数量不满足重新格式化的条件

输入: Python6543210
输出: 6P5y4t3h2o1n0
'''
text_1 = input('请输入字符')
str_num = 0
Number = 0
str_1 = 'qwertyuiopasdfghjklzxcvbnm'
for i in text_1:
    if i.lower() in str_1 or i.upper() in str_1:
        str_num += 1
    else:
        Number += 1
print('str_num - Number', str_num - Number)
if ((str_num - Number) ==  1) or ((str_num - Number) ==  -1) :
    print('可以进行格式化字符串')
    text_1_list = []
    num_list = []
    for i in text_1:
        text_1_list.append(i)
    print(text_1_list)
    text_1_list_temp = text_1_list[:]
    for i in text_1_list_temp:
        if i.isdecimal():
            num_list.append(i)
            text_1_list.remove(i)
    print(text_1_list, num_list)

    result = []
    if len(text_1_list) > len(num_list):
        for i in range(len(num_list)):
            result.append(text_1_list[i])
            result.append(num_list[i])
        result.append(text_1_list[-1])
    else:
        for i in range(len(text_1_list)):
            result.append(num_list[i])
            result.append(text_1_list[i])
        result.append(num_list[-1])
    result = ''.join(result)
    print(result)
else:
    print('字符串中数字和字母的数量不满足重新格式化的条件')



