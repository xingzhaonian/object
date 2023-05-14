'''
集合最大的特性: 唯一, 无序
创建集合
1. s = {'fishc', 'python'} # {}
2. s = {i for i in 'fishc'}  # 推导式
3. s = set(1, 3, 4, 'f', 'p') # 构造器

集合是无序的, 无法使用下标去访问
in 和 not in 可以判断某个元素是否在集合中
可以使用for 循环迭代

copy() 用来对集合进行浅拷贝 s1 = s.copy()
isdisjoint() 方法用来检测两个集合是否毫不相干, 如果有交集返回False, 否则返回True  s.isdisjoint('java') 返回True
issubset() 方法用来检测一个集合是否是另一个集合的子集, 如果是返回True, 否则返回False
子集: 对于A, B两个集合, 如果集合A中任意一个元素都是集合B中的元素, 就说明这两个集合有包含关系, 称A集合为B的子集合
issuperset() 方法检测该集合是另一个集合的超集, 如果是返回True, 否则返回False
超集: 对于A, B两个集合, 如果集合B中任意一个元素都是集合A中的元素, 就说明这两个集合有包含关系, 称A集合为B集合的超集
并集: union() s.union('12567') 并集就是将集合与其他集合的元素并在一起, 组成一个新的集合, 支持多参数
交集: intersection() 找到多个集合中共同的那些元素 s.intersection('fish') 返回{'f', 'i', 's', 'h'}, 这些都是两个集合之前的交集, 支持多参数
差集: difference() 找出存在于该集合但不存在于其他集合中的元素 s.difference('fish'), 支持多参数
对称差集: symmetric_difference() 对于A, B两个集合, 先排除A集合与B集合的所有共同元素, 由剩下的元素组成的集合就是A, B的对称差集 s.symmetric_difference('python')

运算符:
使用集合的运算符的话, 必须保证它们都是集合类型, 使用集合的方法只需要是可迭代类型就行了
s <= set('fishc') 检测子集
s < set('fishc') 检测真子集
s >=  set('fishc') 检测超集
s > set('fishc') 检测真超集
s | {1, 2, 3} | set('python')  并集
s & {1, 2, 3} & set('php') 交集
s - set('python') - set('php')  差集
s ^ set('python') 对称差集

(*other)表示支持多个参数, (other)表示支持一个参数
可变集合 set()
不可变集合 frozenset()
s = set('fishc')
s.update(*others) 更新对象s中的数据, 相当于s.union(), 只不过union不会更新对象s中的数据
s.difference_update(*others) 运算s.difference()后的值覆盖更新到对象s中
s.intersection_update(*others) 运算s.intersection后的值覆盖更新到对象s中
s.symeetric_difference_update(others) 运算s.symeetric_difference后的值覆盖更新到对象s中
s.add('45') 表示将'45' 作为参数添加到集合s中
s.remove('lk') 表示从集合s中删除 'lk', 如果'lk'不存在则抛出异常
s.discard('lk') 表示从集合s中删除 'lk', 如果'lk'不存在就啥也不干
s.pop() 表示从集合s中随机弹出(删除)一个元素, 如果集合s中没有数据, 则 KeyError: 'pop from an empty set' 异常
s.clear() 表示清空集合s


可哈希
大多数不可变对象是可哈希的, 否则不可
'''