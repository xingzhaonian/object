'''
0. 在函数定义中，带一个星号的形参（如 def func(*x)）和带两个星号的形参（如 def func(**x)）有什么区别？
答: def func(*x) 这种表示收集参数, 将*后的参数打包为一个元组收集多个参数,  def func(**x)这种表示收集
关键字参数, 然后以字典形式的键值对进行输出, 例如: a = 1, b = 2, 收集这两个关键字参数后再函数内就是
{a:1, b:2}

1. 请问下面代码会打印什么呢？
>>> def func(a, b=4, c=5):
...     print(a, b, c)
...        
>>> func(1, 2)
>>> # 请问这里会打印什么内容？
答: 1, 2, 5 因为定义函数时a 是位置参数, b = 4是默认参数, c = 5也是默认参数, 当调用该函数时, 1传给
位置参数a, 2传给默认参数b, 最后一个c 就使用默认参数 5

2. 请问下面代码会打印什么内容呢？
>>> def func(x, *y, z=3):
...     print(x, y, z)
...
>>> func(1, 1, 2, 3, 5)
>>> # 请问这里会打印什么内容？
答: 打印 1, (1, 2, 3, 5) 3; 因为 1 作为位置参数传给x, 1, 2, 3, 5都会打包成元组传给 *y, z 是默认参数

3. 请问下面代码会打印什么呢？
>>> def func(x, **y):
...     print(x, y)
...        
>>> func(x=1, y=2, z=3)
>>> # 请问这里会打印什么内容？
答: 打印 1, {y:2, z:3}, 因为 调用该函数时x = 1作为关键字参数传给x, y=2 z=3作为字典类型的收集参数传给
**y (**y表示收集多个关键字参数, 以字典的键值对来输出), 所以最后打印1 {'y':2, 'z':3}

4. 请问下面代码会打印什么呢？
>>> def func(x, *y, **z):
...     print(x, y, z)
...
>>> func(1, 2, 3, 4, y=5)
>>> # 请问这里会打印什么内容？
答: 打印1 (2, 3, 4) {'y':5}, 因为定义函数时x为位置参数, *y为以元组形式收集多个参数,**z为以关键字
参数收集多个参数,调用函数时 1为位置参数传给x, 2, 3, 4为收集参数传给*y, y = 5以关键字参数形式传给**z 

5. 请问下面代码会打印什么呢？
>>> def func(x, *y, **z):
...     print(x, y, z)
...
>>> func(1, 2, 3, y=4, z=5)
>>> # 请问这里会打印什么内容？
答: 打印 1 (2, 3) {'y':4, 'z':5}

6. 请问下面代码会打印什么呢？
>>> def func(x, *y, **z):
...     print(x, y, z)
...
>>> func(1, 2, x=3, y=4, z=5)
>>> # 请问这里会打印什么内容？
答: 会报错, 因为 定义函数时x为位置参数, 但是在调用时把x当作关键字参数了

7. 请问下面代码会打印什么呢？
>>> def func(x, y, z=3):
...     print(x, y, z)
...
>>> func((1, 2), *(3, 4))
答: (1, 2) 3 4, 定义函数时定义了三个参数, 第一个是x, 第二个是y, 第三个是默认参数 y = 3, 在进行调用的时候
(1, 2)作为一个参数传给x, *(3, 4)解包后传给y 和 z, y对应3 z对应4

'''
romannum_arabnum = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
def romannum_to_arabnum(s):
    result = 0
    str_lenght = len(s)
    for i, k in enumerate(s):
        if k in romannum_arabnum:
            temp_result = romannum_arabnum[k]
            if (i != list(enumerate(s))[-1][0] ) and (temp_result < romannum_arabnum[list(enumerate(s))[i + 1][1]]):
                result -= temp_result
            else:
                result += temp_result 
    return result


s = input('请输入一个罗马数字：')
v = romannum_to_arabnum(s)
print(f"转换后的结果是：{v}")


N2R = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]
    
def num2roman(num):
    r = []
    for v, s in N2R:
        while num >= v:
            num -= v
            r.append(s)
        if num == 0:
            break
    
    return "".join(r)
    
#n = input("请输入一个整数：")
#r = num2roman(int(n))
#print(f"转换后的结果是：{r}")


        
