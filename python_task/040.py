'''
问答题
0. 请问下面代码会打印 True 还是 False 呢？
>>> s1 = set([1, 1, 2, 3, 5])
>>> s2 = frozenset([1, 1, 2, 3, 5])
>>> s1 == s2
答: True, 虽然frozenset()可不变, 但依然拥有set()去重特性, 两个集合中包含的元素是一样的, 但是如果拿一个list和set比较就是False

1. 既然有了 set() 集合,为什么还要创造 frozenset() 来冻结集合(换句话说,frozenset() 的优势是什么)?
答: 因为set() 集合是可变的特性, 但是set()中的元素要求是不可变(可哈希的), 所以有时候会出现一个集合中的元素是另一个集合的情况, 
这时候frozenset()的作用就体现出来了, 而且frozenset()是可哈希的

2. 集合中, difference(*others) 和 difference_update(*others) 这两个方法都是用于计算差集,那么它们有什么区别呢？
答: difference(*others) 只计算差集的结果, 并不会更新原集合对象的内容, 而difference_update(*other)则是计算差集结果后覆盖更新到集合中

3. 由于 frozenset 对象是不可修改的,所以我们说它也是可哈希的,对吗？
答: 对, frozenset() 对象是可哈希的

4. 请问集合对象的 update(*others) 方法和 add(item) 方法有什么不同？
答: set().update(*thoers) 支持多个参数, 且将other中的每个参数迭代添加到set中, 而set().add(item)只支持单个参数且将这个参数作为一个整体添加到set中 
假设将字符串 "FishC" 作为参数，使用 update() 方法它是拆分成 5 个字符分别添加进去，而使用 add() 方法则是将整个字符串作为一个元素添加进去。

5. 请问集合对象的 remove(elem) 方法和 discard(elem) 方法有什么不同？
答: set.remove(elem) 删除集合对象中的某个元素, 如果这个元素不存在则会抛出异常, set.discard(elem) 删除集合对象中的某个元素, 如果这个元素不存在则啥也不干

6. 请问下面代码输出的内容是什么？
>>> {x for x in 'FishCChsiF' if x not in 'ish'}
答: {'F', 'C'}
分解:
p = set()
for x in 'FishCChsiF':
    if x not in 'ish':
        p.update(x)

        


动动手
0. 最开始的时候, Python 是没有 set() 的,那么当时伟大的程序猿是如何实现 “集合” 这个的概念呢？
现在我们将时间回拨到那个 “一穷二白” 年代,现在大家没有 set() 可用了,只能利用 dict() 来实现交集和并集。
题目要求:
1. 生成一个随机数列表,一共有 100 个元素,每个元素取 1~100 的随机值,赋值给变量 x
2. 生成另一个随机数列表,一共有 100 个元素,每个元素取 50~150 的随机值,赋值给变量 y
3. 利用字典的 “键” 不会重复的特点,计算 x 和 y 的交集(就是两者共有的元素)

'''
import random
x = [random.randint(1, 100) for i in range(100)]
y = [random.randint(50, 150)for i in range(100)]
d = {}
result_dict = d.fromkeys(i for i in x if i in y)
print(result_dict)


'''
1. 破解 MD5 哈希加密！！
在前面的课后作业中(传送门),我们提到过通常服务器是不会保存用户的明文密码的(那样就太不安全了),取而代之的是存储单向哈希加密后的密文
不过尽管如此,也并非绝对的安全！
虽然说单向哈希加密是无法逆向,但聪明的黑客们想出了彩虹表破解法：
彩虹表是一个用于加密散列函数逆运算的预先计算好的表,常用于破解加密过的密码散列。彩虹表常常用于破解长度固定且包含的字符范围固定的
密码(如信用卡、数字等)。这是以空间换时间的典型实践, 比暴力破解(Brute-force attack)使用的时间更少,空间更多；但与储存密码空间中的
每一个密码及其对应的哈希值(Hash)实现的查找表相比,其花费的时间更多, 空间更少。
密码及其对应的哈希值(Hash)实现的查找表相比,其花费的时间更多,空间更少。
说人话就是：所谓的彩虹表,其实就是将所有可能的字符串组合都给预先哈希一遍,然后将映射结果保存起来,当黑客拿到一个哈希值时,通过查表的方式获取密码明文。
虽然密码安全宣传多年来都有在开展,但还是难以阻止使用出生日期等 6 位数字的人们,这一次,我们就用实际行动告诉大家,6 位数字的哈希密码有多容易被破解……
题目要求：
1. 生成 0~999999 所有整数组成密码的哈希值
2. 将上面生成的哈希值保存为映射类型
3. 通过查表的方式,计算下面 3 个哈希值对应的明文密码
021bbc7ee20b71134d53e20206bd6feb
e10adc3949ba59abbe56e057f20f883e
655d03ed12927aada3d5bd1f90f06eb7

hashlib.md5() 的参数是需要一个 b 字符串(即 bytes 类型的对象), 这里可以使用 bytes("123", "utf-8") 的方式将 "123" 转换为 b"123"。
'''
import hashlib
hash_table = {}
for i in range(0, 999999):
    hash_md5 = hashlib.md5(bytes(str(i), encoding = 'utf-8')).hexdigest()
    hash_table[hash_md5] = i
ciphertext = ['021bbc7ee20b71134d53e20206bd6feb', 'e10adc3949ba59abbe56e057f20f883e', '655d03ed12927aada3d5bd1f90f06eb7']
for i in ciphertext:
    if i in hash_table:
        print(f'{i}的明文是{hash_table[i]}')
    else:
        print(f'无法查询, {i}不存在于密码表中')
