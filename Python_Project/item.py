
class Item(object):
    def __init__(self, name, price, use_count, effcet):
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
        if player.gem >= self.price:
            player.gem -= self.price
            player.bag.add_itme(self)
            print(f'装备{self.name}已购买')


