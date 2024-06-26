r'''
----问答题----
0. Python 同一个代码块中的所有语句必须遵循什么原则？
答: 需要遵守同一缩进的原则 缩进: 使用4个空格或者 1个tab位

1. 请问下面代码是否能够正常执行？
x = 3
y = 5
if x > y:
print("x比y大")
答: 不可正常执行, 缩进错误

2. 请问下面代码是否能够正常执行？
x = 3
y = 5
if x < y: print("x比y小")
答: 可以正常执行

3. 请问下面代码是否能够正常执行？
x = 3
y = 4
z = 5

if x < y:
  print(x, "<", y)
  if y < z:
            print(y, "<", z)
            print(x, "<", z)
答: 可以, 因为python不关注你的缩进是几个空格或者几个tab, python 只关注缩进是否一致

4. 请问下面代码是否能够正常执行？
x = 3
y = 4
z = 5

if x < y:
  print(x, "<", y)
  if y < z:
            print(y, "<", z)
        print(x, "<", z)

答: 不可以, 因为第二个判断条件的缩进是错误的


----动动手----
0. 编写一个程序,让用户输入一个整数,判断其是否奇数还是偶数
'''
num = int(input('请输入数组'))
if num % 2 == 0:
    print(num, '是偶数', sep = '')
else:
    print(num, '是奇数', sep = '')

r'''
1. 通常企业发放的年终奖是根据一年的盈利进行提成,A 公司的提成规则如下:
当利润低于或等于 10 万元时:年终奖为 10%
当利润高于 10 万元,低于 20 万元时:低于 10 万元的部分按 10% 提成,高于 10 万元的部分,按 7.5% 提成
当利润 20 万到 40 万之间时:低于 10 万元的部分按 10% 提成,高于 10 万元低于 20 万元的部分,按 7.5% 提成,高于 20 万元的部分,按 5% 提成
当利润 40 万到 60 万之间时:低于 10 万元的部分按 10% 提成:高于 10 万元低于 20 万元的部分,按 7.5% 提成:高于 20 万元低于 40 万元的部分,
按 5% 提成:高于40万元的部分,按 3% 提成
当利润 60 万到 100 万之间时:低于 10 万元的部分按 10% 提成:高于 10 万元低于 20 万元的部分,按 7.5% 提成:高于 20 万元低于 40 万元的部分,
按 5% 提成:高于40万元低于 60 万元的部分,按 3% 提成:高于60万元的部分,按 1.5% 提成
当利润高于 100 万元时:低于 10 万元的部分按 10% 提成:高于 10 万元低于 20 万元的部分,按 7.5% 提成:高于 20 万元低于 40 万元的部分,
按 5% 提成:高于40万元低于 60 万元的部分,按 3% 提成:高于60万元低于 100 万的部分,按 1.5% 提成:超过 100 万元的部分按 1% 提成

'''

money_num = int(input('请输入今年的利润'))
if money_num <= 100000:
    Commission = money_num * 0.1
    print('年终奖为 10%, 金额为', Commission)
elif 200000 > money_num > 100000:
    Commission = (money_num - 100000) * 0.75
    Commission_1 = 100000 * 0.1
    print('年终奖为 7.5%, 金额为',Commission + Commission_1)
elif 400000 > money_num > 200000:
    Commission_1 = 100000 * 0.1
    Commission_2 = 100000 * 0.75
    Commission = (money_num - 100000) * 0.75
    print('年终奖为 7.5%, 金额为',Commission + Commission_1)

