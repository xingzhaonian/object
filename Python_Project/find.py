a = []
b = [1,2,1,3,4,1,2,3,1,2,3,4,5,67,78,89,9,2,3,4,6,8,9,0,1,1,1,1,111,1,1,2,12,]


class list_collection:
    def merge(param1, param2):
        '''查找 a列表中的每个元素存在于B列表中的个数，如果为0，说明不存在'''
        if len(param1) == 0:
            print('无数据')
            param1.append(param2[0])
            for i in param1:
                for k in param2:
                    if param1.count(k) > 0:
                        continue
                    else:
                        param1.append(k)
        else:
            print('有数据')
            for i in param1:
                for k in param2:
                    if param1.count(k) > 0:
                        continue
                    else:
                        param1.append(k)
                        
                    
    def merge_1(param1,param2):
        '''暴力一点, 直接判断是否存在b列表中的每个元素是否存在于a列表中'''
        for i in param2:
            if i not in param1:
                param1.append(i)



    def duplicat(param1, param2):
        '''看看param1有没有在param2列表中,如果找到直接返回True'''
        for i in param2:
            if i == param1:
                return True

    def merge_2(param1, param2):
        '''调用写的 duplicat()方法，判断一下b列表中的元素是否存在于a列表中，如果没有直接塞进去 '''
        for i in param2:
            if  not list_collection.duplicat(i, param1):
                param1.append(i)

import time
import  os
def loading_time(num):
    count = 0
    for i in range(num):
        count += 1
        if count > 3:
            count = 1
        print('loading' + '.' * count, end='\r', flush = True)
        time.sleep(1)
        os.system("cls")

list_collection.merge_2(a, b)
print(a, b)