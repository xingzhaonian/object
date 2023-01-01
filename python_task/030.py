r'''
0. 请问下面代码执行的结果是？
>>> x = "我爱Pyhon"
>>> x.startwith(["你", "我", "她"])
答: False, startwith() 方法接收一个参数, 这个参数可以是元组数据, 但不可以是列表数据

1. 请问下面代码执行的结果是？
>>> "I love FishC\s".isprintable()
答: 返回True, isprintable()判断参数是否是一个可打印的参数, 转义符不可打印, 其余都可以; 而'\s'不是转义符

2. isdecimal()、isdigit() 和 isnumeric() 这 3 个方法都是判断数字的,那么请问这其中哪一个方法 “最严格”,哪一个又是 “最宽松” 的呢？
答: isdecimal()和isdigit() 最严格, 而 isnumeric()则是最宽松的

3. 请问下面代码执行的结果是？
>>> "一二三四五上山打老虎".isalnum()
答: 返回True;  isalnum()方法集大成者, 只要isalpa(), isdecimal(), isdigit(), isnumeric()中任意一个方法返回Ture, 这个方法就返回True

4. 请使用一行代码判断 s 字符串中,是否所有字符都是英文字母？
答: 
s = 'lovepython'
s.isalpha()

5. 请问下面代码执行的结果是？
>>> "一二三木头人".isidentifier()
答: 返回True, isidentifier()方法用来判断是否是一个合法的python 表示符号, 而python中中文是可以用来作变量名的

===================================
动动手:
0. 给定一个字符串 text 和字符串列表 words,返回 words 中每个单词在 text 中的位置（要求最终的位置从小到大进行排序）。
举例:
text: "I love FishC and FishC love me"
words:"FishC"
输出:[[7, 11], [17, 21]]

text:"I love FishC and FishC love me"
words:"FishC love"
输出:[[2, 5], [7, 11], [17, 21], [23, 26]]

'''
text = input('请输入text内容')
words = input('请输入word内容')
result_list = []
text_lenght = len(text)
words_split_list = words.split(' ')
words_split_list_lenght = len(words_split_list)
print(words_split_list)
for i in range(words_split_list_lenght):
    for k in range(text_lenght):
        