r'''
====问答题=====
0. 请使用列表推导式，创建一个内容为 [1, 4, 9, 16, 25, 36] 的列表？
答 : s = [i * i for i in range(1, 7)]
或者:
s = [i for i in range(37) if i % 2 == 1]
s1 = []
count = 0

for i in range(len(s)):
    if count >= 36:
        break
    count += s[i]
    s1.append(count)
print(s1)


1. 请使用列表推导式，创建一个内容为 [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]] 的列表？
答 : s = [[i - 1, i + 1] for i in range(7) if i > 0]
print(s)

2. 请将下面的列表推导式转换为循环的形式实现？
>>> double = [c * 2 for c in "FishC"]
>>> double
['FF', 'ii', 'ss', 'hh', 'CC']

答: double = []
for i in 'FishC':
    double.append(i * 2)


3. 请将下面的循环转换为列表推导式的形式实现？

>>> matrix = [[1, 2, 3],
...           [4, 5, 6],
...           [7, 8, 9]]
>>> diag = []
>>> for i in range(len(matrix)):
...     i *= matrix[i][i]
...     diag.append(i)
...
>>> diag
[0, 5, 18]

答 : 
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
diag = [ k * matrix[k][k] for k in range(len(matrix))]
print(diag)

4. 请问下面代码执行后，变量 x 和 y 的值分别是什么？
>>> x = "FishC"
>>> y = [x for x in "123"]
答 : y = ['1', '2', '3']   x = "FishC"     因为x 的作用域不一样


5. 解决一下课堂中遗留的问题吧，如何获取矩阵从右上角到左下角这条对角线上的元素？
>>> matrix = [[1, 2, 3],
...           [4, 5, 6],
...           [7, 8, 9]]
答 : s = [matrix[i][-1 - i] for i in range(len(matrix))]

for i in range()


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

diag = []
diag_1 = []
for i in range(len(matrix)):
    diag.append(matrix[i][-1 - i])
print(diag)

count = 0
for i in matrix:
    if 3 in i:
        diag_1.append(3)
        continue
    if 5 in i:
        diag_1.append(5)
        continue 
    if 7 in i:
        diag_1.append(7)
        continue
print(diag_1)

动动手：
0. 打印杨辉三角形
杨辉三角形是中国古代数学的杰出研究成果之一，是我国北宋数学家贾宪于 1050 年首先发现并使用的。而后南宋数学家杨辉在《详解九章算法》一书中记载
并保存了“贾宪三角形“。因此，贾宪三角形又被称为杨辉三角形
简单地说，杨辉三角形的构成如下面动图所示：

'''
# 创建列表
target = []
for i in range(10):
    target.append([])
    for k in range(10):
        target[i].append(k)

#print(target)
# 计算杨辉三角形
# 根据观察，我们知道杨辉三角形左右两边的元素均为1
for i in range(10):
    target[i][0] = 1
    target[i][i] = 1
print(target)


# 第i行j列的值 = 第(i-1)行(j-1)列的值 + 第(i-1)行(j)列的值

for i in range(2, len(target)):
    for k in range(1, i):
        target[i][k] = target[i -1][k - 1] + target[i - 1][k]

print(target)


# 输出杨辉三角形

for i in range(len(target)):
    for k in range(i + 1):
        pass
        print(target[i][k], end = ' ')
    print()