'''
0, 请问方法绑定的意义是什么?
答: 绑定的意义是让实例化对象和类进行关联, 让python知道是哪个对象在进行调用

1, 请问可以将下面代码中的 self 替换成其它名称吗？
>>> class C:
...     def hello(self):
...         print("Hello FishC.")
答: 可以, self只是更好理解罢了

2. 下面代码中，调用 c.hello() 和 C.hello(c) 的结果是一样的，请问它们是完全等价的吗？
>>> class C:
...     def hello(self):
...         print("Hello FishC.")
...
>>> c = C()
>>> c.hello()
Hello FishC.
>>> C.hello(c)
Hello FishC.
答: 是等价的

3. 请问下面代码会打印什么呢？
>>> class C:
...     x = 100
...     def get_x(self):
...         print(x)
...
>>> c = C()
>>> c.x = 250
>>> c.get_x()
>>> # 请问这里会打印什么内容？
答: 会报错, 因为调用 c.get_x()方法时, 会执行print(x), 但是在方法中x是未定义的

4. 请问下面代码会打印什么呢？
>>> class C:
...     x = 100
...     def get_x(self):
...         print(self.x)
...
>>> c = C()
>>> c.x = 250
>>> c.get_x()
>>> # 请问这里会打印什么内容？
答: 250, 因为 c.x = 250是给实例化对象c修改或赋值 250, 类中的x=100不会变, 而方法get_x则是打印实例化对象c的属性, 那就是250

5. 请问下面代码会打印什么呢？
>>> class C:
...     x = 100
...     def get_x(self):
...         print(C.x)
...
>>> c = C()
>>> c.x = 250
>>> c.get_x()
>>> # 请问这里会打印什么内容？
答: 100, 因为 c.x = 250是给实例化对象c修改或赋值 250, 类中的x=100不会变, 而方法get_x则是打印类C中的x属性, 100

6. 请问下面代码会打印什么呢？
>>> class C:
...     def f(self):
...         print("Hello FishC.")
...
>>> c = C()
>>> type(C.f) == type(c.f)
>>> # 请问这里会打印什么内容？
答: False, type(C.f)是function(函数); type(c.f) 是method (方法)

7. 请问下面代码会打印什么呢？
>>> class C:
...     x = 100
...     def set_x(self, x):
...         self.x = x
...
>>> c = C()
>>> d = C()
>>> c.set_x(250)
>>> d.set_x(520)
>>> c.x
>>> # 请问这里会打印什么内容？
答: 250

'''

class Memu(object):

    # 1: 鸡蛋
    # 2: 牛肉
    # 3: 羊肉
    # 4: 洋葱
    # 5: 番茄
    # 6: 土豆
    # 7: 萝卜
    dish_name = {'1': '鸡蛋', '2': '牛肉', '3': '羊肉', '4':'洋葱', '5':'番茄', '6':'土豆', '7':'萝卜'}
    Single_item_price = {'1':1, '2':25, '3':30, '4':2, '5':2, '6':3, '7':3}

    menu = {'1':{'鸡蛋':1}, '2':{'牛肉':25}, '3':{'羊肉':30}, '4':{'洋葱', 2}, '5':{'番茄': 2}, '6':{'土豆':3}, '7':{'萝卜':3}}



    def order(self):
        print('客官想吃点什么?')
        self.result = input('1.洋葱炒牛肉; 2.洋葱炒羊肉; 3.煎蛋; 4.番茄炒蛋; 5.土豆萝卜炖羊肉;')
        self.result = self.result.replace(' ', '')


    def pay(self):
        self.spend = 0
        for i in self.result:
            if i == '1':
                print(self.dish_name['4'], self.Single_item_price['4'], '*', '1'+'\n'+self.dish_name['2'], self.Single_item_price['2'], '*', '1')
                self.spend = self.spend + self.Single_item_price['4'] + self.Single_item_price['2']

            elif i == '2':
                print(self.dish_name['4'], self.Single_item_price['4'], '*', '1'+'\n'+self.dish_name['3'], self.Single_item_price['3'], '*', '1')
                self.spend = self.spend + self.Single_item_price['4'] + self.Single_item_price['3']

            elif i == '3':
                print(self.dish_name['1'], self.Single_item_price['1'], '*', '2')
                self.spend = self.spend + self.Single_item_price['1'] * 2

            elif i == '4':
                print(self.dish_name['5'], self.Single_item_price['5'], '*', '2'+'\n'+self.dish_name['1'], self.Single_item_price['1'], '*', '2')
                self.spend = self.spend + self.Single_item_price['4'] * 2 + self.Single_item_price['1'] * 2

            elif i == '5':
                print(self.dish_name['6'], self.Single_item_price['6'], '*', '2' + '\n' + self.dish_name['7'], self.Single_item_price['7'], '*', '1' + '\n' + self.dish_name['3'], self.Single_item_price['3'], '*', '2', '\n')
                self.spend = self.spend + self.Single_item_price['6'] * 2 + self.Single_item_price['7'] * 1 + self.Single_item_price['3'] * 2

        print(f'感谢惠顾, 您一共消费{self.spend}元, 欢迎下次光临~')


m = Memu()
m.order()
m.pay()


