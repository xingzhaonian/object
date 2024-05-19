'''
[对象]
面向对象也是一种代码封装的方法
对象 = 属性 + 方法
一个对象的静态特征我们称之为属性
一个对象的动态特征我们称之为方法
创建对象需要先创建一个类(class), 类名开头字母要大写
class Turtle:
    head = 1
    eyes = 2
    legs = 4
    shell = True

    def crawl(self):
        print('人们总是抱怨我慢吞吞的, 殊不知如不积跬步, 无以至千里的道理')
    
    def run(self):
        print('虽然我行动很慢, 但如果遇到危险, 我会拼命狂奔')
    
    def bite(self):
        print('人善被人欺, 龟善被人骑')
    
    def eat(self):
        print('谁知盘中餐, 粒粒皆辛苦')
    
    def sleep(self):
        print('zzzz')

所谓的属性就是类里面的变量, 所谓的方法就是写在类里面的函数
t1 = Turtle()   t1就是一个Turtle类的对象, 也叫做实例对象, 他就拥有了这个类定义的属性和方法
t2 = Turtle()   t2就是一个Turtle类的对象, 也叫做实例对象, 他也拥有了这个类定义的属性和方法

当一个对象被生成出来之后, 我们就可以修改类对象中的属性值了, t1.legs = 3  那么, Turtle类中的legs属性就变成了3
此时, 实例化对象t2, 拥有的Turtle类中的属性不会发生变化, 因为同一个类创建的不同对象, 他们之间的数据不会共享

实例化的对象, 也可以动态的创建属性, 属于新增
t1.mouth = 10, 那么t1对象就拥有了mouth属性, value为10

[封装]
封装是面向对象编程的三个基本特性之一, 两外两个是继承和多态

[self]
class C:
    def get_self(self):
        print(self)

c = C()
c.get_self()

这里会打印 <__main__.C object at 0x000001CFE6A03A90>, 因为这就是实例化对象 c
类中的每一个方法, 第一个参数默认都是self, 因为在使用类中的方法时, python需要知道是哪个实例化对象在调用, 所以self 就是实例化对象本身

[继承]
python的类是支持继承的, 它可以使用现有类的所有功能, 并在无需重新编写代码的情况下对这些功能进行扩展, 通过继承创建的新类我们称之为子类
而被继承的类我们称之为父类, 基类, 或者超类
class A:
    x = 520
    def hello(self):
    print('你好, 我是A')

class B(A):
    pass

这样, 类B就继承了类A, 通过类B实例化的对象可以访问和使用类A的属性或方法, 如果子类中包含与父类中有相同的属性或方法, 那么子类将覆盖父类的同名属性和方法, 例如

class A:
    x = 520
    def hello(self):
    print('你好, 我是A')

class B(A):
    x = 880
    def hello(self):
    print('你好, 我是B')
b = B()
b.x  这里x属性就是880, 因为它会覆盖继承的父类中同名的属性x的值
b.hello() 这里hello() 方法会打印 你好, 我是B, 因为它会覆盖继承的父类中同名的方法

判断一个对象是否属于某个类, 使用 isinstance(), 例如
isinstance(b, B) 这里会返回True, 因为对象b是类B的实例化对象
isinstance(b, A) 这里也会返回True, 类B继承自类A, 那么通过类B实例化的对象, 自然也就会继承类A的属性或方法

判断一个类是为某个类的子类, 使用issubclass()
issubclass(A, B) 这里返回False, 因为类A不继承于类B
issubclass(B, A) 这里返回True, 因为类B继承自类A, B属于A的子类

[多重继承]
python的类是支持多重继承的, 也就是一个子类可以继承多个父类
class A:
    x = 520
    def hello('你好, 我是A')

class B:
    x = 880
    y = 666
    def hello('你好, 我是B')

class C(A, B):
    pass
    
c = C()
c.x 这里会打印520
c.y 这里会打印666
c.hello() 这里会打印 你好, 我是A, 因为它的查找顺序是: 自己 > 父类1 > 父类2 > 父类3···   也就是说先找自己身上是否有这个属性或方法,如果没有再找继承父类中的第一个, 如果
第一个也没有那就找第二个, 以此类推

[组合]
class Turtle:
    def say(self):
        print('不积跬步无以至千里')

class Cat:
    def say(self):
        print('喵喵喵')

class Dog:
    def say(self):
        print('哟吼, 我是一只修狗')

class Garden:
    t = Turtle()
    c = Cat()
    d = Dog()
    def say(self):
        slef.t.say()
        slef.c.say()
        slef.d.say()
这里会调用 t.say(), c.say(), d.say(), 分别打印 不积跬步无以至千里、喵喵喵、 哟吼, 我是一只修狗



什么是self?
self其实就是实例化对象本身, 让python知道是哪个对象在调用类中的方法或属性, 起到一个绑定关系的作用,将实例化对象和类进行绑定


'''