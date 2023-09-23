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


'''