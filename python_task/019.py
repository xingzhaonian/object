r'''
----问答题---
0. Python 的列表可以容纳各种不同类型的对象，对吗？
答: 对, list中可以容纳 int, str, tuple, list 等各种数据类型

1. 请问如何创建一个空列表？
答: s = []  这样就创建了一个空的列表

2. 你知道什么是匿名列表吗？
答: 匿名列表就是创建了一个列表 [], 没有将其进行赋值, 由于没有名字, 也无法进行访问, 比较鸡肋

3. 如果有一个列表 list1，有两种方法可以获取到该列表的最后一个元素，你知道分别是什么吗？
s = [1,2,3,4,5,6]
答: s[len(s) - 1];  s[-1] 两种

4. 请问下面代码打印的结果是什么？
[1, 2, 3, 4, 5][:3]
答 : 含义是取列表中0---3但不包括3的所有元素   即[1, 2, 3]

5. 请问下面代码打印的结果是什么？
[1, 2, 3, 4, 5][::2]
答: 含义是取列表中全部的元素, 步长为2   即列表的索引值0, 2, 4, 就是[1, 3, 5]

6. 请问下面代码打印的结果是什么？
[5, "上", 4, "山", 3, "打", 2, "老", 1, "虎"][-2::-2]
答: 含义是反向取列表中 倒数第二个至第零个的所有元素, 步长为2, 每隔一个取一个  即：1, 2, 3, 4, 5

7. 下面有两列表，请问如何将 list2 列表中的全部元素，添加到 list1 列表中第 2 和第 3 个元素的中间
list1 = [1, 2, 8, 9]
list2 = [3, 4, 5, 6, 7]
答: 
count = 2
for i in list2:
    list1.insert(count, i)
    count += 1

list1 = list1[:2] + list2 + list1[2:]

----动动手----
0. 给定一个整数列表 nums 和一个目标值 target, 请在该数组中找出和为目标值的两个元素，并将它们的数组下标值打印出来
比如给定的列表 nums = [2, 7, 11, 15]，目标值 target = 9，那么由于 nums[0] + nums[1] = 2 + 7 = 9，所以打印结果是：[0, 1]'''


num_list = []

while True:
    _ = input('请录入一个整数(输入stop结束)')
    if _ == ('stop'):
        break
    _ = int(_)
    list_length = len(num_list)
    num_list.insert(list_length, _)

list_length = len(num_list)
print(num_list)

isfind = False
target = int(input('输入目标数字'))
for i in range(list_length):
    for k in range(i + 1, list_length):
        if num_list[i] + num_list[k] == target:
            isfind = True
            print([i, k])
if not isfind:
    print('未找到')




r'''
2. 最后，回忆前面我们学习过的 random 模块，生成一个由 10000 个整数（范围是 1 ~ 65535）构成的随机列表，目标值 target 由用户输入'''


import random
count = 10000
random_list = []
is_find_rand_num = False
random_target = int(input('输入随机目标数字'))
while count:
    random_num = random.randint(1, 65535)
    random_list.append(random_num)
    count -= 1

random_list_light = len(random_list)
for i in range(random_list_light):
    for k in range(i + 1, random_list_light):
        if random_list[i] + random_list[k] == random_target:
            print([i, ':', random_list[i], '====', k, ':', random_list[k]])
            is_find_rand_num = True
if not is_find_rand_num:
    print('未找到随机目标数字')
