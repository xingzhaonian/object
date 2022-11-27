
r'''
0. casefold() 和 lower() 两个方法都是将所有的字母变成小写,那它们有什么区别呢？
答: casefold() 更加强大, 它可以支持很多种不同种类的语言, 比如说 β , lower只能显示出原形而casefold则能显示他的小写'ss'

1. 请问下面代码执行的结果是？
>>> "-520".zfill(10)
答: -000000520

2. 请问 "-520".zfill(10) 和 "-520".rjust(10, "0") 的执行结果一样吗？
答:  "-520".zfill(10) 的结果为 '-000000520';  "-520".rjust(10, "0")的结果为 "000000-520"  结果不一样

3. 请问下面代码执行的结果是？
>>> "-520".center(6, "0").zfill(10)
答: '00000-5200'

4. 请问下面代码执行的结果是？
>>> "I love FishC".swapcase()[::-1]
答: 'cHSIf EVOL i'

5. 请使用一行代码来检测列表中的每个元素是否为回文数,并返回一个结果为回文数构成的列表。
提供的列表：["123", "33211", "12321", "13531", "112233"]
返回的结果：['12321', '13531']

'''
Palindrome_number_list = [i for i in ["123", "33211", "12321", "13531", "112233"] if i == i[::-1]]
print(Palindrome_number_list)

r'''
动动手：
0. 请按照以下规则整理一个给定的字符串 s
一个整理好的字符串中,两个相邻字符 s[j] 和 s[j+1],其中 0 <= j <= s.length - 2,要满足如下条件：
若 s[j] 是小写字符,则 s[j+1] 不可以是相同的大写字符
若 s[j] 是大写字符,则 s[j+1] 不可以是相同的小写字符
如果 s[j] 和 s[j+1] 满足以上两个条件,则将它们一并删除
举例：
整理前："FishCcCode"
整理后："FishCcCode" -> "FishCode"

整理前："AbBaACc"
整理后："AbBaACc" -> "AaACc" -> "AaA" -> "A"

整理前："AABaAbCc"
整理后："AABaAbCc" -> "AABbCc" -> "AACc" -> "AA"

请按要求整理好字符串,并将结果打印到屏幕上。
提示(小甲鱼不想限制大家的思路,如果想看的话,请使用鼠标刮开叭~)：将字符串逐个读取,整理后放到一个列表中,最后将列表中的元素挨个打印即可。

'''
temp_list = []
string = "FishCcCode"
string_lenght = len(string)
for i in range(string_lenght):
    if not temp_list:
        temp_list.append(string[i])
        continue
    if (temp_list[-1].upper() == string[i].upper()) and  (temp_list[-1].lower() == string[i].lower()) and (temp_list[-1] != string[i]):
        temp_list.pop()
    else:
        temp_list.append(string[i])
for i in temp_list:
    print(i, end = '')
print('')

r'''
1. 给定的字符串 s 是按照如下规则存放的：它的偶数下标为小写英文字母,奇数下标为正整数。
题目要求：编写代码,将奇数下标的数字转换为相对于上一个字母偏移后的字母
比如 s = "a1b2c3" 转换后的结果是 "abbdcf"(a1 -> ab,b2 -> bd,c3 -> cf);s = "x7y8z9" 转换后的结果是 "xeygzi"(遇到最后字母 z ,则从 a 继续计算偏移)
提示(小甲鱼不想限制大家的思路,如果想看的话,请使用鼠标刮开叭~)：你可能会用到 chr() 和 ord() 这两个函数。

'''
s = input("请按规则输入一个字符串：")
   
length = len(s)
res = []
# 获取字母 a 的编码值
base = ord('a')
   
# 从第一个元素开始，每次迭代跳过一个元素
for i in range(0, length, 2):
    # ord(s[i]) - base 操作得到一个字母的偏移值，比如 b 就是 1
    # 跟 26 求余数的作用是防止溢出，循环计算偏移
    shift = chr((ord(s[i]) - base + int(s[i+1])) % 26 + base)
    print(s[i]+shift, end="")