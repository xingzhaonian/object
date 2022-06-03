'''用python设计第一个小游戏'''
import random
result = random.randint(1,10)
count = 3
while count > 0:
    count = count - 1
    while True:
        temp = input('不妨猜猜我现在心里想的什么数字')
        try:
            temp = float(temp)
        except ValueError:
            print('请输入数字')
        finally:
            if  type(temp) == float:
                print(temp)
                break
    guess = temp
    if guess == result:
        print('你是小甲鱼心里的蛔虫吗？')
        print('猜对也没有奖励')
        break
    else:
        if guess > result:
            print('输入的数字太大了')
        else:
            guess < result
            print('输入的数字太小了')

print('小甲鱼心里想的是', result)
print('游戏结束 不玩了')








# 运算符： <  判断左边是否小于右边
# 运算符： <= 判断左边是否小于等于右边
# 运算符： >  判断左边是否大于右边
# 运算符： >= 判断左边是否大于等于右边
# 运算符： == 判断左右两边是否相等
# 运算符： ！= 判断左右两边是否不相等
# 运算符： is 判断两个对象的id是否相等
# 运算符： is not 判断两个对象id是否不相等
# 运算符： in 判断in左边对象是否在右边里，换句话说，右边对象是否包含左边对象
# 运算符： not in 判断not in 左边对象是否不在右边对象里面，换句话说，右边对象是不是不包含左边对象
