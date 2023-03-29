r'''
0. 请问下面代码会打印什么呢？
>>> x = [1, 2, 5, 8, 0]
>>> y = reversed(s)
>>> for each in y:
...     print(each)
... 
0
8
5
2
1
>>> list(y)
答: 返回空 '[]' , 因为迭代器已经被for循环用过了, 迭代器的元素为空, 这个时候再取就没了

1. 请使用 map() 函数，实现与下面代码相同的效果？
>>> [ord(x) for x in "FishC"]
[70, 105, 115, 104, 67]
答: list(map(ord, 'FishC'))

2. 请使用 map() 函数，对下面的二维列表进行排序？
>>> matrix = [[1, 3, 2],
...            [5, 4, 6],
...            [8, 7, 9]]
>>> # 这里利用好 map() 函数，一句代码的事情，就可以解决问题啦~
>>> # 排序后的结果如下
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
答: result = list(map(sorted, matrix))

3. 请问下面代码会打印什么呢？
>>> seasons = ["Spring", "Summer", "Fall", "Winter"]
>>> e = enumerate(seasons, start=11)
>>> print(e[2])
答 : enumerate对象是一个枚举对象, 该对象不可下标, 会报错

4. 请使用列表推导式，实现与下面代码相同的结果。
>>> list(filter(str.islower, "FishC"))
['i', 's', 'h']
答: l = [i for i in 'FishC' if i.islower()]

5. 下面代码试图同时对多个可迭代对象进行迭代操作，但是失败了……学了这一节课，你有没有办法解决这个问题？
>>> x = [1, 2, 3, 4, 5]
>>> y = "FishC"
>>> for i, j in x, y:
...     print(i, j)
... 
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    for i, j in x, y:
ValueError: too many values to unpack (expected 2)
答: zipped = list(zip(x, y))
for i in zipped:
    print(i[0],i[1])
for x, y in zip(x, y):
    print(x , y)


6. 迭代器和可迭代对象最大的不同是？
迭代器是一次性的, 可迭代对象则可以重复使用

7. 所有可迭代对象都可以转换成迭代器吗？
是的, 可以; 遵循所有迭代器都是可迭代的对象的原则, 所有可迭代对象都可以转换成迭代器吗


'''
'''
0. 请使用学过的知识，自己动手编写代码，利用 for 循环语句，模拟 all()、any()、enumerate()、zip() 这4个函数的实现
'''
# all() all用来判断序列中的元素是否都为真, 如果是返回True, 否则返回False
def all_1(param_1):
    for i in param_1:
        if not i:
            return False
    else:
        return True

list_1 = [1, 2, 3, 4, 5, None]
# print(all_1(list_1))

# any() any用来判断序列中的元素是否有真值, 如果是返回True, 否则返回False
def any_1(param_1):
    for i in param_1:
        if i:
            return True
    else:
        return False

list_2 = [0, '', 0, 1, None]
print(any_1(list_2))


# enumerate() enumerate用来返回一个枚举对象, 它的功能就是将可迭代对象中的每个元素及从0开始的序号共同构成一个二元组的列表
def enumerate_1(param_1, start = 0):
    param_num = len(param_1)
    result_list = []
    for i in range(param_num):
        if start == 0:
            result_list.append((i, param_1[i]))
        else:
            start += 1
            result_list.append((start - 1, param_1[i]))
    return (result_list)

test_list = ['Spring', 'Summer', 'Fall', 'Winter']             
enumerate_1(test_list, start = 1)



# zip() zip函数用于创建一个聚合多个可迭代对象的迭代器, 它会将作为参数传入的每个可迭代对象的每个元素一次组合成元组, 即第i个元组包含来自每个参数的第i个元素
def zipped(param_1, param_2):
    result = []
    param_1_num = len(param_1)
    param_2_num = len(param_2)
    if param_1_num >= param_2_num:
        for i in range(param_2_num):
            result.append((param_1[i], param_2[i]))
        return iter(result)
    else:
        for i in range(param_1_num):
            result.append((param_1[i], param_2[i]))
        return iter(result)

'''
1. 假设有一个密室，每次只能放一个人进去，在进去之前和出来之后都要求摁一下门口的打卡机按钮，打卡机会依次将名字和进出时间戳记录为以下的格式：
times = [1, 3, 3.5, 6.5, 9.5, 10, 10.8]
names = ["A", "B", "C", "D", "E", "F", "G"]
这里表示：
A 君是从时间戳为 0 的时候进入，从时间戳为 1 的时候出来，总共耗时为 1
B 君是从时间戳为 1 的时候进入，从时间戳为 3 的时候出来，总共耗时为 2
C 君是从时间戳为 3 的时候进入，从时间戳为 3.5 的时候出来，总共耗时为 0.5
```
G 君是从时间戳为 10 的时候进入，从时间戳为 10.8 的时候出来，总共耗时为 0.8
OK, 现在要求大家编写代码, 统计给定的数据, 打印耗时最长和最短的人员名称。
'''
import random
times = []
names = ["A", "B", "C", "D", "E", "F", "G"]
for i in range(len(names)):
    times.append(random.randint(0,20))
max_name = names[0]
min_name = names[0]
max_time = times[0]
min_time = times[0]
max_time_list = []
max_name_list = []
min_time_list = []
min_name_list = []
max_time_list.append(max_time)
max_name_list.append(max_name)
min_time_list.append(min_time)
min_name_list.append(min_name)

for i in range(len(names)):
    each_name = names[i]
    if i == 0:
        each_time = times[i] - 0
    else:
        each_time = times[i] - times[i - 1]
    if each_time > max_time:
        max_time_list.clear()
        max_name_list.clear()
        max_time = each_time
        max_name = each_name
        max_time_list.append(max_time)
        max_name_list.append(max_name)
    elif each_time == max_time:
        if each_name in max_name_list:
            continue
        else:
            max_time = each_time
            max_name = each_name
            max_time_list.append(each_time)
            max_name_list.append(max_name)
    elif each_time < min_time:
        min_time_list.clear()
        min_name_list.clear()
        min_time = each_time
        min_name = each_name
        min_time_list.append(min_time)
        min_name_list.append(min_name)
    elif each_time == min_time:
        min_time = each_time
        min_name = each_name
        min_time_list.append(min_time)
        min_name_list.append(min_name)

zipped_max_result = list(zip(max_name_list, max_time_list))
zipped_min_result = list(zip(min_name_list, min_time_list))
print(zipped_max_result, zipped_min_result)
for x, y in zipped_max_result:
    print('用时最长的是{}, 花了{}秒'.format(x, y))
for x, y in zipped_min_result:
    print('用时最短的是{}, 花了{}秒'.format(x, y))