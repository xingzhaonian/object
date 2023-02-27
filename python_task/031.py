r'''
0, 请问下面的代码执行结果分别是什么？
'www.iloveshc.com'.lstrip('wcom')
'www.iloveshc.com'.rstrip('wcom')
'www.iloveshc.com'.strip('wcom')
答: '.iloveshc.com', 'www.iloveshc.', '.iloveshc.'

1. 请问下面代码打印的内容是什么？
"www.ilovefishc.com".removeprefix("w.")
答: 'www.ilovefishc.com'

2. split() 方法常常被应用于对数据的解析处理，那么考考大家，如果要从字符串"https://ilovefishc.com/html5/index.html" 
中提取出 "ilovefishc.com"，使用 split() 方法应该如何实现呢？
答: "https://ilovefishc.com/html5/index.html".split('//')[1].split('/')[0]


3. 如果要求按换行符来分割字符串，小甲鱼推荐使用 splitlines() 方法，而非 split("\n")，你觉得小甲鱼的依据是什么？
答: 因为换行符在不同的操作系统中表示不一样, 要想代码兼容所有操作系统或平台, 用splitlines()最合适

4. 下面代码使用加号运算符（+）进行字符串拼接，现在看起来有点太 low 了，请将它改为使用 join() 方法来拼接吧~
s = "I" + " " + "love" + " " + "FishC"
'I love FishC'
答: s = ' '.join(['I', 'Love', 'FishC'])

5. 请问下面代码打印的内容是什么？
print(",\n".join("FishC"))
答: 
F,
i,
s,
h,
C

'''

r'''
动动手
0, 编写一个生成凯撒密码的程序
凯撒密码最早由古罗马军事统帅盖乌斯·尤利乌斯·凯撒在军队中用来传递加密信息，故称凯撒密码。
原理：
凯撒密码是一种通过位移加密的方法，对 26 个（大小写）字母进行位移加密，比如下方是正向位移 6 位的字母对比表：
明文字母表如下
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
密文字母表如下
GHIJKLMNOPQRSTUVWXYZABCDEFghijklmnopqrstuvwxyzabcdef
所以，如果给定加密的明文是:
I love FishC
那么程序加密后输出的密文便是:
O rubk LoynI
'''

plaintext_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
need_cipher_text = input('请输入需要加密的明文')
move_step = int(input('请输入需要移动的位数'))
if move_step >= 26:
    print('数字过大, 无效')
    exit()
result_cipher_text = ''
print(need_cipher_text)
for i in need_cipher_text:
    if i == ' ':
        result_cipher_text += i
    need_cipher_text_position = plaintext_table.find(i)
    for k in range(len(plaintext_table)):
        if need_cipher_text_position + move_step + 1 > 52:
            need_cipher_text_position = need_cipher_text_position - 26
        if int(need_cipher_text_position) == k:
            i = plaintext_table[k + move_step: k + move_step + 1]
            result_cipher_text += i
print(result_cipher_text)

'''1. 给定一个字符串数组 words, 只返回可以使用在美式键盘同一行的字母打印出来的单词, 键盘布局如下图所示.
美式键盘中:
第一行由字符 "qwertyuiop" 组成
第二行由字符 "asdfghjkl" 组成
第三行由字符 "zxcvbnm" 组成
举例：
输入: words = ["Twitter", "TOTO", "FishC", "Python", "ASL"]
输出：['Twitter', 'TOTO', 'ASL']
''' # Twitter, TOTO, FishC, Python, ASL
line_1 = 'qwertyuiop'
line_2 = 'asdfghjkl'
line_3 = 'zxcvbnm'
words_list = ["Twitter", "TOTO", "FishC", "Python", "ASL"]
#    words = input('请输入列表形式的单词, 输入stop停止输入')
#    if words == 'stop':
#        break
#    words_list.append(words)


result_list = []
for i in words_list:
    if i.casefold().strip(line_1) == '' or i.casefold().strip(line_2) == '' or i.casefold().strip(line_3) == '':
        result_list.append(i)
print(result_list)

'''
for i in words_list:
    for k in i:
        k = k.casefold()
        if k not in line_1:
            break
    else:
        result_list.append(i)

for i in words_list:
    for k in i:
        k = k.casefold()
        if k not in line_2:
            break
    else:
        result_list.append(i)

for i in words_list:
    for k in i:
        k = k.casefold()
        if k not in line_3:
            break
    else:
        result_list.append(i)
print(result_list)'''