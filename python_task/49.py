'''
0. 递归算法的实现原理什么？
答: 递归实现的原理是在函数内部调用自身

1. 实现同样的任务，说使用递归的执行效率通常要比迭代低，请问依据是什么？
答: 因为每次调用递归函数它并不会立即返回, 而是要等到最底层的那个返回值返回之后, 它才会逐级向外返回

2. 请问下面代码中，recsum() 函数被调用了多少次？
>>> def recsum(x):
...     if x < 0:
...         return x
...     else:
...         return recsum(x-1) + recsum(x-2)
...        
>>> recsum(3)
-11
答: 15 次

3. 下面代码利用递归实现将列表的各个元素进行相加，请补全红色方框中的代码，使其能够成功执行并获取结果。
答:
def recsum(x):
    if not x:
        return 0
    else:
        print(x[0], x[1:])
        return x[0] + recsum(x[1:])
print(recsum([1,2,3,4,5]))

4. 下面代码利用递归实现将嵌套列表的各个元素进行相加，请补全红色方框中的代码，使其能够成功执行并获取结果。
答:
def sumtree(x):
    total = 0
    for i in x:
        if type(i) is not list:
            total += i
        else:
            total += sumtree(i)
    return total

    

动动手
0. 题目：请动手优化课堂中递归实现斐波那契的代码。
'''

def fibRecur(n):
   if n == 1 or n == 2:
       return 1
   else:
      return fibRecur(n-1) + fibRecur(n-2)

print(fibRecur(12))

import timeit

def fibRecur(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibRecur(n-1) + fibRecur(n-2)

def tailFibRecur(n, x, y):
    if n == 1 or n == 2:
        return y
    else:
        return tailFibRecur(n-1, y, x+y)

def fibIter(n):
    a, b, c = 1, 1, 1
    while n > 2:
        c = a + b
        a = b
        b = c
        n -= 1
    return c

# 这个耗时会比较久（因为默认是重复测试 5 次），请大家耐心等待
FR = timeit.timeit("fibRecur(12)", setup="from __main__ import fibRecur")
print(f"普通递归耗时：{FR:.2f}秒。")

TFR = timeit.timeit("tailFibRecur(12, 1, 1)", setup="from __main__ import tailFibRecur")
print(f"优化尾递归耗时：{TFR:.2f}秒。")

FI = timeit.timeit("fibIter(12)", setup="from __main__ import fibIter")
print(f"普通迭代耗时：{FI:.2f}秒。")