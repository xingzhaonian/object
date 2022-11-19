r'''
----问答题：----
0. 有时候我们会看到大牛的代码中使用单独一个下划线(_)来作为变量的名字,它通常有何含义？
答: _ 作为变量名的含义是临时存放数据, 用的比较少, 或者这个数据没有什么意义, 就只是个临时数据
解析：如果是下划线组合,比如 _var、__var、__var__、var_,它们都有约定俗成地特殊含义,不要轻易
使用这些组合名称（具体是啥特殊含义,咱在后面的课程会有详细讲解哈）

1. 请使用列表推导式创建一个 4 * 5 的二维列表,并将每个元素初始化为数字 8 
答: s = [[max(0,8),max(0,8),max(0,8),max(0,8),max(0,8)] for i in range(4)]

2. 请将下面列表推导式还原成循环语句的实现形式。
result = [i / 2 for i in range(10) if i % 2 == 0]
答:
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i / 2)

3. 请将下面的嵌套循环语句使用列表推导式实现。
>>> result = []
>>> for x in range(10):
...     if x % 2 == 0:
...         for y in range(10):
...             if y % 2 != 0:
...                 result.append([x, y])

答:  result = [[x, y] for x in range(10) if x % 2 == 0 for y in range(10) if y % 2 != 0]

4. 请将下面 matrix 矩阵反向展开,即使得最终的结果为 [9, 8, 7, 6, 5, 4, 3, 2, 1]
答 : '''
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

matrix_length = len(matrix)
matrix_two_dimensional_length = len(matrix[0])
result = []
for i in range(matrix_length):
    i += 1
    for k in range(len(matrix[-i])):
        k += 1
        result.append((matrix[-i][-k]))
'''  或者使用列表推导式 '''
flatten = [col for row in matrix for col in row][::-1]

r'''
5. 鱼C-T恤总共提供了有 2 种颜色("BLACK", "WHITE")和 10 个码数("WS", "WM", "WL", "S", "M", "L", "XL", "2XL", "3XL", "4XL")的选择
请使用列表推导式统计所有颜色和尺码的组合(要求将每个组合使用一个内嵌的列表包含起来,如下所示)
>>> colors = ["BLACK", "WHITE"]
>>> sizes = ["WS", "WM", "WL", "S", "M", "L", "XL", "2XL", "3XL", "4XL"]
>>> 
>>> # 请使用列表推导式,统计得出下面的结果
>>> 
>>> result
[['BLACK', 'WS'], ['BLACK', 'WM'], ['BLACK', 'WL'], ['BLACK', 'S'], ['BLACK', 'M'], ['BLACK', 'L'], ['BLACK', 'XL'], ['BLACK', '2XL']
 ['BLACK', '3XL'], ['BLACK', '4XL'], ['WHITE', 'WS'], ['WHITE', 'WM'], ['WHITE', 'WL'], ['WHITE', 'S'], ['WHITE', 'M'], ['WHITE', 'L'],
 ['WHITE', 'XL'], ['WHITE', '2XL'], ['WHITE', '3XL'], ['WHITE', '4XL']]
答:
'''
colors = ["BLACK", "WHITE"]
sizes = ["WS", "WM", "WL", "S", "M", "L", "XL", "2XL", "3XL", "4XL"]
result = [[i, k] for i in colors for k in sizes]


r'''
---动动手---
0. 请使用列表推导式,获得 matrix 矩阵的转置矩阵 Tmatrix(将 matrix 的行列互换之后得到的矩阵,称为 matrix 的转置矩阵)
>>> matrix = [[1, 2, 3, 4],
...           [5, 6, 7, 8],
...           [9, 10, 11, 12]]
什么是转置矩阵？
一个矩阵 matrix,把它的第一行变成第一列,第二行变成第二列,……,最末一行变为最末一列,从而得到一个新的矩阵 Tmatrix。这一过程称为矩阵的转置

''' 
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

row_range = len(matrix)
clo_range = len(matrix[0])
output_result = [[]*row_range  for i in range(clo_range)]
for i in range(row_range + 1):
    for k in range(clo_range - 1):
        output_result[i].append((matrix[k][i]))

print(output_result)
r'''
1. 请按照顺时针螺旋顺序输出矩阵中的所有元素。
比如矩阵 matrix 如下：
>>> matrix = [[1, 2, 3, 4, 5],
...           [6, 7, 8, 9, 10],
...           [11, 12, 13, 14],
              [15, 16, 17, 18]]
那么将输出:
[1, 2, 3, 4, 5, 10, 14, 18, 17, 16, 15, 11, 6, 7, 8, 9, 13, 12]
'''
matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]

rows = len(matrix)
cols = len(matrix[0])
    
left = 0
right = cols - 1
top = 0
bottom = rows - 1
    
result = []
    
while left <= right and top <= bottom:
    # 从左往右遍历
    for col in range(left, right + 1):
        result.append(matrix[top][col])
    
    # 从上往下遍历
    for row in range(top + 1, bottom + 1):
        result.append(matrix[row][right])
    
    if left < right and top < bottom:
        # 从右往左遍历
        for col in range(right - 1, left, -1):
            result.append(matrix[bottom][col])
    
        # 从下往上遍历
        for row in range(bottom, top, -1):
            result.append(matrix[row][left])
    
    left = left + 1
    right = right - 1
    top = top + 1
    bottom = bottom - 1
    
print(result)