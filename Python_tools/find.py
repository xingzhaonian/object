a = []
b = [1,2,1,3,4,1,2,3,1,2,3,4,5,67,78,89,9,2,3,4,6,8,9,0,1,1,1,1,111,1,1,2,12,]


class list_collection:
    def merge(self, param1, param2):
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
                        
                    
    def merge_1(self, param1,param2):
        for i in param2:
            if i not in param1:
                param1.append(i)



    def duplicat(self, param1, param2):
        for i in param2:
            if i == param1:
                return True

    def merge_2(self, param1, param2):
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
        time.sleep(0.5)
        os.system("cls")

loading_time(10)