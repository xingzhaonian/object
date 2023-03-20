r'''
0. 列表的 sort() 方法和 sorted() 函数有哪些异同点(至少各举 3 个)？
答: 共同点: ① 都可以对可迭代对象进行排序 ② 都可以使用key参数  ③ 都可以使用reverse参数;
    不同点: ① sort直接在对象本身进行排序, sorted则是返回一个全新的列表 ② sort 只能处理列表, 而sorted则可以处理任何可迭代对象  ③ 

1. 如果将 "PPAP"、"ppap"、"Ppap"、"PPaP" 使用 sorted() 函数进行排序，你觉得结果应该是怎样？
答: ["PPAP", "PPaP", "Ppap", "ppap"]

2. 请问 sorted() 函数和 reversed() 函数返回的是同一个类型的对象吗？
答: 不是同一个类型大的对象, sorted()函数返回的是一个列表(可迭代对象), 而reversed()则返回一个迭代器

3. 请问下面代码执行后的结果是？
>>> max("FishC") and min("FishC")
答: 返回 'C', 解析: max("FishC") 返回s, min("FishC")返回C; 's' and 'C' 返回'C'

4. 请问下面代码会打印什么内容？ 
>>> x = [1, 2, 5, 8, 0]
>>> y = reversed(x)
>>> y[2]
答:  y[2] = 2, 解析: reversed(x) = [0, 8, 5, 2, 1], 所以 y[2] = 5

5. 请问下面代码会打印什么内容?
>>> list(reversed(sorted("FishC520")))
['s', 'i', 'h', 'F', 'C', '5', '2', '0']

'''

r'''
0. 给定一个整数列表，请编程来调整该列表中整数的顺序，使得所有奇数排好序后放在数组的前半部分，所有偶数排好序后放在数组的后半部分。
比如给定的整数列表是 [1, 8, 7, 3, 6, 5, 4, 2]，那么调整后的结果应该是 [1, 3, 5, 7, 2, 4, 6, 8]。
'''

initial_list = [1, 8, 7, 3, 6, 5, 4, 2]
odd_number_list = []
even_number_list = []
for i in initial_list:
    if i % 2 == 0:
        even_number_list.append(i)
    else:
        odd_number_list.append(i)

odd_number_list.sort()
even_number_list.sort()
result_list = odd_number_list +even_number_list
print(result_list)

r'''
1. 翻转单词顺序。
用户输入一个英文句子，请编程翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
例如输入字符串是 "I love FishC."，则输出 "FishC. love I"
注意1:用户输入的字符串可能会在前面或者后面包含任意数量的空格，但是反转后的结果将会去除这些空格(例如输入字符串是 "   I love FishC.   ", 
结果依然输出 "FishC. love I")
注意2:用户输入的字符串中，单词之间可能不止一个空格，但是反转后的结果将统一使用一个空格作为单词之间的间隔(例如输入字符串是 "I   love        FishC."
结果依然输出 "FishC. love I")
'''
init_string = 'I   love        FishC.'
result_list = []
split_string = init_string.split(' ')
for i in split_string:
    if i != '':
        result_list.append(i)
result_string = ' '.join(list(reversed(result_list)))        
print(result_string)