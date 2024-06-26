r'''
====问答题====
0. 请问 == 运算符和 is 运算符有什么区别呢？
答: == 用于判断两个对象的 value 是否为一样, 而 is 的运算符则是用于判断两个对象所指向的内存地址是否一样

1. 请问下面代码的执行结果是？
>>> [[1, 2, 3], [4, 5, 6]] + [7, 8, 9]
答 : [[1, 2, 3], [4, 5, 6], 7, 8, 9]

2. 请问下面代码的执行结果是？
>>> len([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
答: 3, 因为这是一个二维列表, 列表中只有三个元素, 分别为[1, 2, 3], [4, 5, 6], [7, 8, 9]

3. 请问下面代码的结果是返回 True 还是 False 呢？
>>> a = 250
>>> b = 250
>>> a is b
答 : 返回True 如果在解释器中a和b为同一个值且a < 257, b < 257的话, 返回True, 如果 a >= 257, 则返回False
如果在脚本中不管大小都是返回True
在解释器中如果是小数:
a = 10.0
b = 10.0
print(a is b)   则返回False
在解释器中如果是小数:
a = 10.0; b = 10.0
print(a is b)   则返回True

4. 请问下面代码的结果是返回 True 还是 False 呢？
>>> a = 1000
>>> b = 1000
>>> a is b
答: 返回 False; 若是
a = 256
b = 256
a is b
则返回True


5. 既然有二维列表，那么三维列表应该也是“同理可得”的东西，请大家尝试创建一个简单的三维列表吧？
s = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]

a = [[0] * 3] * 3     这样只是对其引用进行拷贝, 内存地址都是同一个


b = [0] * 3
for i in range(len(b)):
    b[i] = [0] * 3    这样就是给列表中的每一个元素在内存中开辟了一个空间, 用来存储其元素, 内存地址是不同的

three = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
         [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
         [[2, 2, 2], [2, 2, 2], [2, 2, 2]]]



----动动手----

0. 请根据下面的内存关系图，分别创建出 x、y 和 z 三个不同的列表。

x = [[0] * 3] * 3

y = [0] * 3
for i in range(3):
    y[i] = [0] * 3

z = [0] * 3
for i in range(3):
    z[i] = [0] * 3
    for k in range(3):
        z[i][k] = [0] * 3
print(z)


1. 上一节的课后作业我们提到了“摩尔投票法”，这种方法尤其适用于在任意多的选项中找到数量占比最多的那一个。
那么这一次我们修改一下要求，编写代码，利用“摩尔投票法”来找出占比数量最多的两个元素（注意：这两个元素的数量都需要超过总数的三分之一）。

'''
# 找出候选值
nums = [5, 4, 5]
list_lenfgt = len(nums)
one_third_list_lenght = list_lenfgt // 3
major_1 = None
major_2 = None
count_1 = 0
count_2 = 0
# 对抗阶段
for i in nums:     #  循环中找候选值 用 if---elif---else的结构, 找出两个候选值
    if i == major_1:
        count_1 += 1
    elif i == major_2:
        count_2 += 1
    elif count_1 == 0:
        major_1 = i
        count_1 = 1
    elif count_2 == 0:
        major_2 = i
        count_2 = 1
    else:
        count_1 -= 1
        count_2 -= 1

# 统计阶段
count_1 = 0
count_2 = 0
for i in nums:
    if i == major_1:
        count_1 += 1
    elif i == major_2:
        count_2 += 1

if count_1 > one_third_list_lenght and count_2 > one_third_list_lenght:
    print('占比数量最多的两个元素为{0}和{1}'.format(major_1, major_2), '数量分别为{0}和{1}'.format(count_1, count_2))
else:
    print('没有超过总数的三分之一的两个元素')
    if count_1 > one_third_list_lenght:
        print('元素{0}超过了元素总数量的三分之一'.format(major_1), '{0}个'.format(count_1))
    elif count_2 > one_third_list_lenght:
        print('元素{0}超过了元素总数量的三分之一'.format(major_2), '{0}个'.format(count_2))