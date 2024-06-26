'''
tuple
逗号是构成元组的基本条件
元组是不可变的


创建一个元组
ryhme = (1, 2, 3, 4, 5, '上山打老虎')

同样 创建元组也可以不带括号
ryhme = 1, 2, 3, 4, 5, '上山打老虎'

元组也可以通过下标来索引对应的value
ryhme[0]
ryhme[2]
ryhme[3]
ryhme[4]

元组跟列表一样, 支持切片操作
ryhme[0:2]
返回一个tuple

因为列表不支持修改, 所以列表内的内容只支持查询 (index, count)

nums = (1,2,3,4,5,6)
nums.index(3)   返回2

nums.count(2)   返回1


多个列表可以使用 '+' 进行拼接
s = (1, 2, 3)
n = (4, 5, 6)
t = s + n
返回 (1, 2, 3, 4, 5, 6)

tuple也可以使用 '*' 号来进行将tuple 重复生成
a = (1,2,3)
c = a * 3
返回 c = (1, 2, 3, 1, 2, 3, 1, 2, 3)


元组也是可以进行嵌套的
a = (1, 2, 3)
b = (4, 5, 6)
c = (a, b)
返回 c = ((1, 2, 3), (4, 5, 6))

元组跟列表一样, 同样支持迭代
a = (1, 2, 3)

for i in a :
    print(i)

元组同样支持列表推导式
a = (1, 2, 3, 4, 5)
s = [i += 1 for i in a ]



元组的打包和解包

解包
t = (1, 2, 3, 4, '哈哈哈', '你是谁', 3.14)
z, x, c, v, b, n, m = t
z = 1, x = 2, c = 3, v = 4, b = '哈哈哈', n = '你是谁', m = 3.14             列表也可如此

重点： 元组中的元素是不可变的, 但是元组中的元素如果是指向一个可变的列表, 那就是可被修改的
a = [1,2,3]
b = [4,5,6]
c = (a, b)

'''