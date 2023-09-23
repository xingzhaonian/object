'''
0. 请问类和对象有什么关系？
答: 类通过实例化可以生成对象, 可以比喻 对象是类的其中一个孩子
类就是对象的模板，我们在类中定义好了属性和方法，那么基于此类创建出来的对象也自 “出生” 起，就自动拥有这些属性和方法

1. 请定义一个最小的类 C
答:
class C:
    pass
pass 是空语句，一般用于占领坑位，以待日后使用。上面这个类没有属性，没有方法，仅有一个 pass 语句，但也是没有问题的（不构成语法错误

2. 请问下面画红框的位置分别是什么呢？
class C:
    X = 520
c1 = C()
c2 = C()
答:
c1 is c2
False

c1 == c2
False

c1.x is c2.x
True

c1.x == c2.x
True

3. 两个来自于同一个类的对象，是否有可能存在不同的属性呢？
答: 当然有可能, 实例化的对象, 可以动态的创建属性, 属于新增

4. 你觉得面向对象的优势是什么？
答: 实现代码的封装和重用
类的定义实现了代码的封装，实例化多个对象实现了代码的重用

5. 定义在类中的函数就叫方法，那么它们有什么直观的区别呢？
答: 方法需要使用对象进行访问调用，而函数则可以直接调用
比如: 
class Lop:
    def lol(self):
        print('lol')
我们就需要先实例化或者类名.方法名进行调用
l = Lop()
l.()
或者 Lop().lol()

6. 请问下面代码中, self 参数的值什么？为什么方法定义的时候有 self 参数，但在调用中却无需传递实参？
>>> class C:
...     def func(self):
...         print("Hi FishC~")
...
>>> c = C()
>>> c.func()
Hi FishC~
答: 在上面代码中, self 参数的值是对象 c 自身；因为 self 参数是对象访问方法的时候自动进行传递的，所以不需要我们进行显式传递。
同一个类可以生成无数多个对象, 那么当我们在调用类里面的一个方法的时候, Python 如何知道到底是哪个对象在调用呢？
没错，就是通过这个 self 参数传递的信息
所以，类中的每一个方法，默认的第一个参数都是 self。

==============================================================================================================================================
大家先观察下面代码：
>>> class C:
...     x = 250
...     def get_x(self):
...         return x
...
>>> c = C()
>>> c.get_x()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    c.get_x()
  File "<pyshell#40>", line 5, in get_x
    return x
NameError: name 'x' is not defined
这里抛出了一个 NameError 异常，表示这个 x 变量未曾定义, 这是为何？
答: 我猜是因为类中的属性是私有的, 无法被类中的方法进行引用


'''
class Person:
    name = None
    age = None
    
    def set_name(self):
        self.name = input('请设置你的名字')
        print(self.name)

    def set_age(self):
        self.age = input('请设置你的年龄')
        print(self.age)        

    def get_name(self):
        if self.name:
            print(self.name)
        else:
            print('名字未设置')
            
    def get_age(self):
        if self.name:
            print(self.name)
        else:
            print('名字未设置')        

p = Person()
print(f'默认的名字{p.name}, 默认的年龄{p.age}')
p.set_name()
p.set_age()
p.get_name()
p.get_age()
print(p.name)
print(p.age)

class Rectangle:
    length  = 5
    width = 3

    def set_length(self):
        self.length = int(input('请设置长度'))
        print(self.length)


    def set_width(self):
        self.width = int(input('请设置宽度'))
        print(self.width)

    def get_perimeter(self):    
        if self.length == Rectangle.length:
            self.set_length()
        if self.width == Rectangle.width:
            self.set_width()
        print(f'周长面积{2 * ((int(self.length)) + (int(self.width)))}')

    def get_area(self):
        if self.length == Rectangle.length:
            self.set_length()
        if self.width == Rectangle.width:
            self.set_width()
        print(f'周长面积{(int(self.length) * int(self.width))}')

r = Rectangle()
print(f'初始长度:{r.length}, 初始宽度:{r.width}')
r.get_perimeter()
r.get_area()
print(f'修改之后的长度:{r.length}, 修改之后的宽度:{r.width}')

