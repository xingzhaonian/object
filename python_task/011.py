r'''
----问答题----

0. 请问下面表达式的值是什么？
3 == not 5
答: 语法错误, 会报错

1. 请问下面表达式的值是什么？
3 or 5 and 0
答: 3, 因为python运算有优先级的   这道题目里 not > and > or  

2. 请问下面表达式的值是什么？
3 and 5 + True or False
答: 返回6, 因为python运算有优先级的   这道题目里 加法 > and > or 

3. 请问下面表达式的值是什么？
 0 and not 1 or not 2 and 3 or 4 and not 5
0 and False or False and 3 or 4 and False
False or False or False
答: 返回False 因为python运算有优先级的   这道题目里 not > and > or  

4. 请问下面表达式的值是什么？
1 == 2 < 3
答: 返回True  1 == True

5. 请将下面的链式比较转换为使用 and 的普通比较
1 < 2 > 3 < 4 < 5
1 < 2 and 2 > 3 and 3 < 4 and 4 < 5


----动动手----
0. 爱因斯坦曾出过这样一道有趣的数学题：
有一个长阶梯，若每步上 2 阶，最后剩 1 阶；若每步上 3 阶，最后剩 2 阶；若每步上 5 阶，
最后剩 4 阶；若每步上 6 阶，最后剩 5 阶；只有每步上 7 阶，最后刚好一阶也不剩。

'''
step_num = 1
find = False
while True:
    if step_num % 2 == 1 and step_num % 3 == 2 and step_num % 5 == 4 and step_num % 6 == 5 and step_num % 7 == 0:
        find = True
        break
    else:
        step_num += 1

if find == True:
    print('该阶梯的最总数量是{}个'.format(step_num))
else:
    print('程序未找到该阶梯数量')





