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