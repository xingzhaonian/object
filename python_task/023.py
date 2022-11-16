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
    
row = len(matrix)
col = len(matrix[0])
   
min_row = [1024] * row
max_col = [0] * col
   
# 遍历矩阵中的每一个元素
# 找到每行中最小的元素，并将它们存放到列表min_row中
# 找到每列中最大的元素，并将它们存放到列表max_col中
for i in range(row):
    for j in range(col):
        min_row[i] = min(matrix[i][j], min_row[i])
        max_col[j] = max(matrix[i][j], max_col[j])
   
# 遍历矩阵中的每一个元素
# 判断是否同时满足“同一行的所有元素中最小”和“同一列的所有元素中最大”
for i in range(row):
    for j in range(col):
        if matrix[i][j] == min_row[i] and matrix[i][j] == max_col[j]:
            print(matrix[i][j])