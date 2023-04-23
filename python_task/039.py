'''
0. 创建一个空集合，我们只需要使用一对不包含任何元素的大括号（{}），对吗？
答: 错误, 不包含任何元素的 {} 是dict类型

1. 可以把集合当做是只有键没有值的字典吗？
答: 可以, Python 中的字典和集合都是通过散列表来实现的，所以，集合其实也是存储着键值对，只不过默认情况下它的键和值是相同的。

2. 请问下面代码的执行结果是？
>>> len({s for s in "fishc.com.cn"})
答: set去重, {'.', 'n', 's', 'h', 'c', 'o', 'i', 'm', 'f'},  有9个元素

3. 使用下标来访问集合，会导致报错，你知道为什么集合不支持下标索引吗？
答: 因为无序

4. 请使用一行代码判断字符串 “FishC.com.cn” 中是否存在重复的字符？
答: len('FishC.com.cn') == len({'FishC.com.cn'}), 返回False, 就说明数量不一致 字符串中有重复的

5. 如果要检测一个字符串是否另一个字符串的子字符串，可以使用 in 运算符，但同样的方式却不适用于集合(如下面代码所示)那么请问应该如何检测一个集合
是否包含另外一个集合呢？
答: 使用issubset()或者issuperset()来检测是否是该集合的子集或超集
>>> "FishC" in "FishC.com.cn"
True
>>> set("FishC") in set("FishC.com.cn")
False
set("FishC").issubset("FishC.com.cn")
set("FishC.com.cn").issuperset('FishC')

6. 如果存在多个列表，需要筛出这些列表中相同的元素，可以使用什么方法？
答: 先把列表转换为set(), 然后使用intersection()交集方法, 得出的结果便是它们之间共同拥有的元素  对应的运算符是 &

7. 请问下面代码的执行结果是？
>>> s1 = set("fishc.com.cn")
>>> s2 = set("ilovefishc.com")
>>> s1 - s2
答: 取 s1和s2 之间的差集, n;  也可以使用 s1.difference(s2)

8. 请使用正确的运算符, 写出与下面代码执行结果相同的操作?
>>> set("FishC").intersection("Php", "Python")
{'h'}
答: 交集 &; set("FishC") & set("Php") & set("Python")

9. 请问下面三个图形中, A 和 B 通过什么操作会变成 C?
答: 对称差集, symmetric_difference(), 运算符为 ^ 

'''

import random
import timeit

haystack = [random.randint(1, 10000000) for i in range(10000000)]
needles = [random.randint(1, 1000) for i in range(1000)]

# 请在此处添加一行代码，使得查找过程的执行效率提高 10000 倍以上。
haystack = set(haystack)

def find():
    found = 0
    for each in needles:
        if each in haystack:
            found += 1

    print(f"一共找到{found}个匹配。")

t = timeit.timeit("find()", setup="from __main__ import find", number=1)
print(f"查找过程一共消耗{t}秒。")



