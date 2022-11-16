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




'''
