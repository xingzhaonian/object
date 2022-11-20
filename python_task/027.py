r'''
问答题
0. 既然元组和字符串都是不可改变的对象,那么两者有何区别？
答: 元组的生成关键字是 ' , ', 字符串则不是; 元组是可容纳可变对象的, 字符串就不行; 

1. 请写出仅有一个元素 5 的元组
答: x = (5,)

2. 请问下面代码得到的结果是？
>>> t = (3, 1, 4, 9, 8)
>>> t.sort()
答: 会报错, 因为t是一个元组, 而元组是不可变的, 不支持sort 排序

3. 请问下面代码得到的结果是？
>>> t = (3, 1, 4, 9, 8)
>>> t[2:4]
答: 输出 (4, 9)

4. 请问我们可以修改的是 “元组中的列表” 还是 “列表中的元组” ?
答: 修改的是元组中的列表, 而不是列表中的元组;  列表中的元组是不可变的

5. 用一个专业的名词描述以下代码的行为？
script, first, second, third = argv
答: 这是解包行为

6. 请问下面代码为什么会出错？如何解决呢？
>>> a, b, c = "FishC"
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a, b, c = "FishC"
ValueError: too many values to unpack (expected 3)
答: 报错误是因为参数 数量不一致导致, 我们可以这样   x, y , z = ('fishc',) * 3; 这样就把a, b, c 三个变量都赋值为 'fishc' 了

7. 如果我们非要修改一个元组,你觉得应该怎么做？
答: 可以进行拼接,  但是进行拼接之后, 该变量已经不是之前那个变量了, 重复进行了赋值, 在内存中开辟了新的空间; 或者改变元组中的列表

8. 有一天,居委会的大妈找上门,让你帮她用 Python 创建一个对象,用于登记接种新冠疫苗的情况。登记内容包含（姓名、生日、接种日期）,你应该怎么做？

答: 使用元组, Vaccination_information = (name, birthday, Inoculation_date),  因为元组不可变, 信息一旦保存则无法进行变更


动动手
0,请编写代码,测试一下到底是创建列表的速度快,还是创建元组的速度快？为了得到更精准的数据,请重复测试100次,并分别计算出平均速度。
'''

import timeit
list_time_consuming = timeit.repeat('init_list = []', number = 1000000, repeat = 100)
list_sum_time = 0
for i in list_time_consuming:
    list_sum_time += i
list_Average_time_consumption = list_sum_time / 100
print('调用了100次创建1000000列表的每次平均耗时, 每创建1000000次列表平均耗时{}'.format(list_Average_time_consumption))


list_time_consuming = timeit.repeat('init_tuple = ()', number = 1000000, repeat = 100)
tuple_sum_time = 0
for i in list_time_consuming:
    tuple_sum_time += i
tuple_Average_time_consumption = tuple_sum_time / 100
print('调用了100次创建1000000元组的每次平均耗时, 每创建1000000次元组平均耗时{}'.format(tuple_Average_time_consumption))




