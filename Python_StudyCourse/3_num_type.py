'''
Python 有三种不同的数字类型
1：整数
2：浮点数
3：复数
'''
a = 0.1
b = 0.2
c = 0.3

if a + b == c:
    print('True')
else:
    print('False')

print(a + b, c)

i = 0
while i < 1:
    i = i + 0.1
    print(i)

'''Python 的浮点数是有误差的'''

'''Python 浮点数之所以是有误差的，是因为Python采用了跟C语言一样的IEEE754的标准来储存浮点数的，所以会产生一定精度上的误差'''

# 如何精确计算浮点数？  使用decimal模块
import decimal

x = decimal.Decimal('0.1')   # 这里接收一个字符串，具体原因是因为浮点数在python认为本身就不精确，所以传进去后，仍然是个不精确的数字，所以需要传字符串                 
y = decimal.Decimal('0.2')
z = decimal.Decimal('0.3')
print(type(x), type(y), type(z), x, y, x + y, z)
if x + y == z:
    print(True)
else:
    print(False)

# 复数
print(1 + 2j)  # 1代表实部， 2j代表虚部
x = 1 + 2j
print(x.real)  # 获取复数对象实部的数值
print(x.imag)  # 获取复数对象虚部的数值

'''

数字之间的运算
操作                           结果
x + y                          x加y的结果
x - y                          x减y的结果
x * y                          x乘以y的结果
x / y                          x除以y的结果
x // y                         x除以y的结果(地板除, 去除小数点后面的余数, 向下取整, 即取比目标结果小的最大整数)
x % y                          x除以y的余数
-x                             x的相反数
+x                             x的本身
abs(x)                         x的绝对值
int(x)                         将x转换为整数
float(x)                       将x转换为浮点数
complex(re, im)                返回一个复数, re是实部, im是虚部
c.conjugate()                  返回c的共轭复数
divmod(x, y)                   返回(x//y, x%y)
pow(x ,y)                      计算x的y次方
x ** y                         计算x的y次方

'''