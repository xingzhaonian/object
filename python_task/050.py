count = 0
def hannuo(n, a, b, c):
    global count
    count += 1
    if n == 1:
        print(a, '--->',c)
    else:
        hannuo(n-1, a, c, b)
        print(a, '--->', c)
        hannuo(n-1, b, a, c)


hannuo(3, 'x', 'y', 'z')
print(count)
'''
0. 给定一个整数 n，请编写一个递归函数，计算从 1 + 2 + 3 + ... + n 的结果（比如 n = 10，那么结果就是 55）
答:
def get_sum(n):
    if n == 1:
        return n
    else:
        return n + get_sum(n - 1)
print(get_sum(10))

1. 给定一个整数 n，请编写一个递归函数，判断该整数是否为 2 的幂次方。如果是返回 True，否则返回 False。
答:
def isPowerOfTwo(n):
    if n > 0:
        if n == 1:
            return True
        if n % 2 == 1:
            return False
        return isPowerOfTwo(n / 2)
    else:
        return False



2. 请实现一个递归函数，要求只使用加号运算符（+）来实现乘法运算的结果。
答:
def mul(x, y):
    if x == 0 or y == 0:
        return 0
    if x == 1:
        return y
    if y == 1:
        return x
    if x < y:
        return mul(x-1, y) + y
    else:
        return mul(x, y-1) + x

print(3, 5)

3. 给定一个列表 L，请编写一个递归函数，找到该列表中最大的元素
def get_max(L):
    if len(L) == 2:
        return L[0] if L[0] > L[1] else L[1]
    else:
        sub = get_max(L[1:])
        return L[0] if L[0] > sub else sub

4. 假设僧侣每秒钟都能正确地移动一枚金片，请问将 64 枚金片从一根银针移动到另外一根银针上，大概需要使用多少时间？
def g(n):
    if n == 1:
        return 1
    else:
        return 2 * g(n-1) + 1

'''

'''def get_max(l):
    if len(l) == 1:
        return l[0]
    elif len(l) == 2:
        if l[0] > l [1]:
            return l[0]
        else:
            return l[1]
    else:
        sub = get_max(l[1:])
        if l[0] > sub:
            return l[0]
        else:
            return sub

print(get_max([2,20,8,10]))'''


def move(n, x, y, z):
    if n == 1:
        print(x, '--->', z)
    else:
        move(n-1, x, z, y) 
        print(x, '--->',z)
        move(n-1, y, x, z)

move(3, 'a', 'b', 'c')