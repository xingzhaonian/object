'''
0. 在还没有学习 isinstance() 函数之前,我们使用 type() 函数判断对象的类型,你觉得两者在检测结果上有何不同呢？
答: isinstance() 是用来判断一个对象是否属于某个类; type()是用来返回该对象是什么类

1. 请问如何证明 bool 是 int 的子类？
答: issubclass(bool, int) 

2. 什么时候应该使用继承,什么时候应该使用组合？
答: 当需要它的实现而非方法时用继承, 当你需要它的方法而非实现时用组合；或者这么说 
假如我们需要定义的几个类,拥有一些共同的属性和方法,那么我们应该考虑使用继承,讲这些共有的属性和方法设计在父类中,而特殊的属性和方法设计
在子类中,这样一来解决了代码冗余的问题,二来提高了代码的可扩展性（比如定义动物为父类,猫、狗、鸡、鸭、鹅则可以定义为子类）。假如我们需要
定义的几个类之间并没有从属关系,而是同级,那么就应该考虑使用组合（比如人的手、脚、嘴巴；花园里的花、草、猫、狗）；简单地说,继承能用“是”来连接
比如猫是动物,狗是动物；而组合能用“有”来连接,比如花园有猫,花园有狗,小甲鱼有手~

3. 在继承中,如果我们不满意父类的方法实现,应该如何修改它呢？
答: 在本体类中重新写一个跟父类相同名称的方法就可以

4. 请问是否可以在子类中修改父类的属性(可以动手尝试一下)？
答: 可以
class A:
    x = 520
class B:
    A.x = 100


5. 请问下面代码中,红色方框的内容应该是什么呢？
class C:
    def myfunc(self):
        print('C')
class D:
    x = 520
    def myfunc(self):
        print('D')
class E(C, D):
    x = 520
答:
e = E()
e.x  打印520
e.myfunc()  打印C
因为它的查找顺序是: 自己 > 父类1 > 父类2 > 父类3···

6. 请看下面代码,如果调用 test() 函数,那么打印的值分别是什么呢？
>>> x = 1
>>> def test():
...     x = 2
...     print(x)
...     class C:
...         x = 3
...         print(x)
...         def m1(self):
...             print(x)
...             print(self.x)
...         def m2(self):
...             x = 4
...             print(x)
...             self.x = 5
...         def m3(self):
...             print(x)
...             print(self.x)
...         c = C()
...         c.m1()
...         c.m2()
...         c.m3()
答:
'''
x = 1
def test():
    x = 2
    print(x)
    class C:
        x = 3
        print(x)
        def m1(self):
            print(x)
            print(self.x)
        def m2(self):
                x = 4
                print(x)
                self.x = 5
        def m3(self):
            print(x)
            print(self.x)
    c = C()
    c.m1()
    c.m2()
    c.m3()
test()

'''
0. 请根据下图所示继承关系创建 A~H 共计 8 个类,其中,父类 A 和 B 均拥有 x 属性(A.x = 250,B.x = 520)
其余子类均为 pass 填充,然后判断 类 H 的实例化对象 h 的 x 属性值应该是多少？
'''
class A:
    x = 250

class B:
    x = 520

class C(B):
    pass

class D(A, B):
    pass

class E:
    pass

class F(D):
    pass

class G(D):
    pass

class H(E, F, G):
    pass

h = H()
print(h.x == 250)

'''
要求大家依葫芦画瓢,定义一个动物园类(Zoo),里面有鸟类如 1 只孔雀(Peacock)、2 只天鹅(Swan)、3 只八哥(Myna),猫科动物类如
 4 头狮子(Lion)、5 头老虎(Tiger)、6 头豹子(Leopard),灵长类(Primate)如 7 只猴子(Monkey)、8 只猩猩(Chimpanzee)、9 只狒狒(Baboon),
 题目要求就这3类动物(当然你想继续发挥也可以),只需要定义类的构成框架就行,内部用 pass 语句填充即可
'''
class Brids:                       #鸟类
    pass

class Peacock(Brids):              #孔雀
    pass

class Swan(Brids):                 #天鹅
    pass

class Myna(Brids):                 #八哥
    pass        

class Felidae:                     #猫科动物类
    pass

class Lion(Felidae):               #狮子
    pass

class Tiger(Felidae):              #老虎
    pass

class Leopard(Felidae):            #豹子
    pass

class Primate:                     #灵长类
    pass

class Monkey(Primate):             #猴子
    pass

class Chimpanzee(Primate):         #猩猩
    pass

class Baboon(Primate):             #狒狒
    pass


class Zoo:
    peacock = [Peacock()]
    swan = [Swan(), Swan()]
    myna = [Myna(), Myna(), Myna()]
    lion = [Lion() for i in range(4)]
    tiger = [Tiger() for i in range(5)]
    leopard = [Leopard() for i in range(6)]
    monkey = [Monkey for i in range(7)]
    chimpanzee = [Chimpanzee() for i in range(8)]
    baboon = [Baboon() for i in range(9)]
    print(f'{len(peacock)}只孔雀: {peacock}\n, {len(swan)}只天鹅{swan}\n, {len(myna)}只八哥{myna}\n, {len(lion)}只狮子{lion}\n,\
           {len(tiger)}只老虎{tiger}\n, {len(leopard)}只豹子{leopard}\n, {len(monkey)}只猴子{monkey}\n, {len(chimpanzee)}只猩猩{chimpanzee}\n, {len(baboon)}只狒狒{baboon}\n')

z = Zoo()
