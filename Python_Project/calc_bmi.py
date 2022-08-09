from turtle import window_height
import time

class personal_information:
    def get_name():
        while True:
            name = input('请输入你的名字')
            try:
                name = str(name)
            except ValueError:
                print('输入数字哟~')
            if type(name) == str:
                return name
    def get_age():
        while True:
            age = input('请输入你的年龄')
            try:
                age = float(age)
            except ValueError:
                print('输入数字哟~')
            if type(age) == float:
                return age
    def get_height():
        while True:
            height = input('请输入你的身高:单位[米]')
            try:
                height = float(height)
            except ValueError:
                print('输入数字哟~')
            if type(height) == float:
                return height
    def get_weight():
        while True:
            weight = input('请输入你的体重:单位[千克]')
            try:
                weight = float(weight)
            except ValueError:
                print('输入数字哟~')
            if type(weight) == float:
                return weight

def calc_bmi(param1,param2):
    bmi = param1 / (param2**2)
    if bmi > 19:
        print('体重过轻，注意增加饮食')
        return 1
    if 19 < bmi < 25:
        print('体重健康，注意保持')
        return 2
    if 25 < bmi < 30 :
        print('你太胖了，注意减少饮食')
        return 3
    if 30 < bmi < 39:
        print('你太重了，快减肥吧！！！！')
    else:
        print('你不是地球人吧!')
        return 4

def count_num():
    num = 3
    for i in range(num):
        time.sleep(num)
        print(num - i, '秒后退出程序')

per_info = personal_information
name = per_info.get_name()
age = per_info.get_age()
height = per_info.get_height()
weight = per_info.get_weight()

calc_bmi(weight, height)
count_num()    
