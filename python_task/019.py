r'''
----问答题---
0. Python 的列表可以容纳各种不同类型的对象，对吗？
答: 对, list中可以容纳 int, str, tuple, list 等各种数据类型

1. 请问如何创建一个空列表？
答: s = []  这样就创建了一个空的列表

2. 你知道什么是匿名列表吗？
答: 匿名列表就是只使用一次的列表, 临时使用, 用来存放一些临时数据

3. 如果有一个列表 list1，有两种方法可以获取到该列表的最后一个元素，你知道分别是什么吗？
s = [1,2,3,4,5,6]
答: s[len(s - 1)];  s[-1] 两种

4. 请问下面代码打印的结果是什么？
[1, 2, 3, 4, 5][:3]
答 : 含义是取列表中0---3但不包括3的所有元素   即[1, 2, 3]

5. 请问下面代码打印的结果是什么？
[1, 2, 3, 4, 5][::2]
答: 含义是取列表中全部的元素, 步长为2   即列表的索引值0, 2, 4, 就是[1, 3, 5]

6. 请问下面代码打印的结果是什么？
[5, "上", 4, "山", 3, "打", 2, "老", 1, "虎"][-2::-2]
答: 含义是反向取列表中 倒数第二个至第零个的所有元素, 步长为2, 每隔一个取一个

7. 下面有两列表，请问如何将 list2 列表中的全部元素，添加到 list1 列表中第 2 和第 3 个元素的中间
list1 = [1, 2, 8, 9]
list2 = [3, 4, 5, 6, 7]
答: 
count = 2
for i in list2:
    list1.insert(count, i)
    count += 1

----动动手----
0. 给定一个整数列表 nums 和一个目标值 target, 请在该数组中找出和为目标值的两个元素，并将它们的数组下标值打印出来
比如给定的列表 nums = [2, 7, 11, 15]，目标值 target = 9，那么由于 nums[0] + nums[1] = 2 + 7 = 9，所以打印结果是：[0, 1]

'''
num = []
while True:
    nums = input('请输入一个整数(输入stop结束)')
    if nums == 'stop':
        break
    else:
        nums = int(nums)
        num.append(nums)
target = int(input('请输入目标整数'))
num_1 = num
find = False
for i in num:
    for k in num_1:
        if i == k:
            continue
        if i + k == target:
            find = True
            print([num.index(i), num_1.index(k)])
            break
    if find:
        break
if not find:
    print('未找到')

r'''
2. 最后，回忆前面我们学习过的 random 模块，生成一个由 10000 个整数（范围是 1 ~ 65535）构成的随机列表，目标值 target 由用户输入

'''
import random

