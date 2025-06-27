

class Item(object):
    def __init__(self, name, price, use_count, effcet):
        self.gem = 500
        self.name = name
        self.price = price
        self.use_count = use_count
        self.effcet = effcet

    # 是否可使用
    def can_use(self):
        return self.use_count >= 1
        
    # 使用道具
    def use_item(self, player):
        if self.can_use(self):
            self.use_count -= 1
            player(self.effcet)
        else:
            print(f'道具数量不足')
    
    # 购买道具
    def buy_itme(self, player):
        if self.gem >= self.price:
            self.gem -= self.price
            player.bag.add_itme(self)
            print(f'装备{self.name}已购买')


class Animal:
    def __new__(cls, animal_type):
        if animal_type == 'dog':
            return Dog()
        print(super().__new__(cls), cls)
        return super().__new__(cls)
    
class Dog:
    def bark(self):
        return 'woof'
    
animal = Animal('do3')
print(animal)

#print(animal())

        


