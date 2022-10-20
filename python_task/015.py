r'''
----问答题----
0. Python 是如何区分不同代码块的呢？
答: python通过缩进来区分不同的代码块


1. 请问下面代码执行后, x 变量的值是多少？
x = 520 if "Love" else 404
答: x 等于 520


2. 请将下面代码中的条件分支部分修改为使用条件表达式来实现
age = 18
isMale = True
if age < 18:
    print("抱歉, 未满18岁禁止访问。")
else:
    if isMale:
        print("任君选购！")
    else:
        print("抱歉,本店商品可能不适合小公举哦~")

答: 
age = 18
isMale = True
print("抱歉, 未满18岁禁止访问。") if age < 18 else print("任君选购！") if isMale else print("抱歉,本店商品可能不适合小公举哦~")


3. 其实,大多数 if - else 条件分支还可以使用 and - or 运算符组合的表达式来代替,那么如果将下面代码转变成 and - or 来实现,应该是怎样的呢？
if "Love":
    520
else:
    404

True and "Love" or False and 404

4. 请将下面的条件分支语句,使用条件表达式实现,并尝试理解这段代码的目的是什么？'''
a = 1
b = 2
c = 3
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)
print(a) if a < c else print(c) if a < b else print(b) if b < c else print(c)

r'''
答: 找到最小的数字

----问答题----
0. 请编写一个程序,根据录入的血液酒精含量来判断是否酒驾？
当酒精含量小于 20 毫克时：不构成饮酒行为
当酒精含量大于等于 20 毫克且 小于 80 毫克时：已经达到酒后驾驶的标准
当酒精含量大于等于 80 毫克时：已经达到醉酒驾驶的标准

'''
def Drunkenness_test():
    while True:
        try:
            alcohol_content = input('酒精含量')
            alcohol_content = float(alcohol_content)
            # print(type(alcohol_content))
            if type(alcohol_content) == type(int()) or type(alcohol_content) == type(float()):
                break
        except (ValueError, TypeError):
            print('number')

    if alcohol_content < 20:
        print('未构成饮酒行为')
    elif 20 <= alcohol_content <= 80:
        print('酒后驾驶')
    elif alcohol_content > 80:
        print('醉酒驾驶')

r'''
1. 验证角谷猜想
角谷猜想的内容是：任意给定一个正整数,若它为偶数则除以 2,若它为奇数则乘以 3 再加 1,得到一个新的自然数,按照这样的方法计算下去,最终的结果必将是 1。
比如给定的自然数是 5,则 5 * 3 + 1 = 16 -> 16 / 2 = 8 -> 8 / 2 = 4 -> 4 / 2 = 2 -> 2 / 2 = 1
现在要求大家编写一个验证角谷猜想的程序。

'''
number = int(input('输入数字'))

while True:
    if number <= 0 :
        print('输入的数字为', number, '无效')     
        break
    if number % 2 == 1:
        print('{:.0f}'.format(number),'*', '3', '+', '1', '=' ,'{:.0f}'.format(number * 3 + 1), sep = '')
        number = number * 3 + 1
    if number % 2 == 0:
        print('{:.0f}'.format(number),'/', 2, '=', '{:.0f}'.format(number / 2 ), sep = '')
        number = number / 2
    if number == 1:
        print('最后得到的数字为{0:.0f}'.format(number))
        break