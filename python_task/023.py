r'''
0. 请问你是如何理解 ”在 Python 中，变量不是盒子” 这句话的？
答: 变量不是盒子, 可以说变量是指针或者是标签, 在给变量赋值时，并不是把值丢入盒子中并把之前的值拿出，而是给新的值开辟出另一块内存空间

1. 请问下面代码执行后, y 的值是多少？
>>> x = 1
>>> y = x
>>> x = 2
答: y = 1, 因为 y 变量相当于在内存中重新开辟了一块空间来储存其value, 接下来不管 x 怎么进行变化, y都不会变


2. 请问下面代码执行后, x == y 返回的结果是 True 还是 False ?
>>> x = [1, 2, 3]
>>> y = x
>>> y[1] = 1
>>> x == y
答: 返回True


3. 请问下面代码实现的是浅拷贝还是深拷贝？
>>> x = [[1, 2, 3], [4, 5, 6]]
>>> y = x[:]
答: 浅拷贝

4. 请问下面代码执行后，列表 x 和 y 的内容分别是什么？
>>> x = [[1, 2, 3], [4, 5, 6]]
>>> y = x.copy()
>>> y.append(7)
>>> y[1].append(8)
答: x = [[1, 2, 3], [4, 5, 6, 8]]    y = [[1, 2, 3], [4, 5, 6, 8], 7]
 

5. 请问下面代码执行后，列表 s 的内容是什么？
>>> s = [1]
>>> s.append(s)
答: [1, [...]]   s[1] 中有无限个[1, [...]]


----动动手----
0. 创建一个 88 x 88 的随机整数矩阵（二维列表），然后匹配用户输入的整数是否与其中某元素相等，如果相等则打印其行号和列号。
要求1:随机整数取值范围 0~1024
要求2:需找出所有匹配的元素
'''

import random
matrix_list = []
for i in range(2):
    matrix_list.append([])
    for k in range(2):
       matrix_list[i].append(random.randint(0, 1024))

num = 33
num = int(num)
count = 0
for i in matrix_list:
    for k in i:
        if num == k:
            print(count, matrix_list[count].index(num))
    count += 1

r'''
1. 请编程找出矩阵中的幸运数字。
说明：假设给定一个 m * n 的矩阵（矩阵中数值的取值范围是 0~1024, 且各不相同）
如果某一个元素的值在同一行的所有元素中最小，并且在同一列的所有元素中最大，那么该元素便是幸运数字。
假设给定的矩阵如下：

'''
matrix = [[10, 36, 52],
          [33, 24, 88],
          [66, 76, 99]]


is_find = False

# 获取矩阵长度 (列表总长度和每一行的长度 )
matrix_range = len(matrix)
each_range = len(matrix[0])

# 获取矩阵中每一行中最小的元素, 添加到 min_row
min_row = [min(min(matrix[i]), 1024) for i in range(len(matrix)) ]

# 初始化tamp_list列表, 使得结构变为 matrix 的结构
tamp_list = [ [] for i in range(each_range)]

# 将每一列的元素变为每一行放进 tamp_list 
for i in range(matrix_range):
    for k in range(each_range):
        tamp_list[i].append(matrix[k][i])

# 获取 tamp_list 中每一行最大的元素 添加到 max_clo
max_clo = [max(max(tamp_list[i]), 0) for i in range(len(tamp_list))]

# 找出幸运数字, 判断 min_row 和 max_clo 中是否有相同的元素存在
for i in range(len(min_row)):
    for k in range(len(max_clo)):
        if min_row[i] == max_clo[k]:
            is_find = True
            print('幸运数字为', min_row[i], '位于第', i + 1, '行第', k + 1, '列')
            

'''
# 或者這樣  传统for 循环写法
row_min = []
temp_list = []
clo_max = []
row_range = len(matrix)
clo_range = len(matrix[0])
for i in range(row_range):
    temp_list.append([])

for i in range(row_range):
    for k in range(clo_range):
        if min(min(matrix[i]), 1024) not in row_min:
            row_min.append(min(min(matrix[i]), 1024))
        temp_list[i].append(matrix[k][i])

for i in range(len(temp_list)):
    clo_max.append(max(max(temp_list[i]), 0))
print(row_min, clo_max)

for i in range(row_range):
    for k in range(clo_range):
        if row_min[i] == clo_max[k]:
           print('位于列表中第', i+1, '行', '第', k+1, '个元素为幸运数字', matrix[i][k])'''