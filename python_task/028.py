r'''
0. 请问下面代码打印的结果是什么？
>>> str1 = "xxxxx"
>>> str1.count("xx")
答: 2, 因为str1中有两个xx, 不足第三个

1. 字符串的 find() 方法和 index() 方法同样是返回查找对象的下标值，那么它们之间的区别是？
答: 使用find() 方法如果找不到字符串内容会返回-1, 而使用index()方法找不到字符串内容则抛出ValueError

2. 请问下面代码返回的值是什么？
>>> x = "上海自来水来自海上"
>>> x.rindex("来水来")
答: 返回值是3

3. 请问下面代码执行的结果是 A 还是 B 抑或是 C 呢（为了你可以更容易地计数，下面使用 * 表示空格）？
print(x)
print(x.expandtabs(2))
print(x.expandtabs(5))
print(x.expandtabs(10))
A:
Hello****FishC
Hello**ishC
Hello*****FishC
Hello**********FishC
B:
Hello***FishC
Hello*FishC
Hello*****FishC
Hello*****FishC
C:
Hello***FishC
Hello*FishC
Hello*****FishC
Hello**********FishC

答: B

4. 请问下面代码打印的结果是什么？
>>> "I love FishC.com".translate(str.maketrans("ABCDEFG", "12345678"))
答: 报错, str.maketrans 的两个参数长度不一致
相当于
'''
table = str.maketrans('ABCDEFG', '1234567')
str1 = 'I love Fishc.com'
str1.translate(table)
r'''
5. 请问下面代码打印的结果是什么？
>>> "I love FishC.com".translate(str.maketrans("love", "1234", "love"))
答: I  FishC.cm


动动手
0. 用户输入两个版本号 v1 和 v2, 请编写代码比较它们, 找出较新的版本
科普：

版本号是由一个或多个修订号组成，各个修订号之间由点号（.）连接，每个修订号由多位数字组成，例如 1.2.33 和 0.0.11 都是有效的版本号。

从左到右的顺序依次比较它们的修订号，点号（.）左侧的值要比右侧的权重大，即 0.1 要比 0.0.99 大。
'''
version_1 = input('请输入第一个版本号, V1: ')
version_2 = input('请输入第二个版本号, V2: ')
division_version_1 = version_1.split('.')
division_version_2 = version_2.split('.')
version_1_lenght = len(division_version_1)
version_2_lenght = len(division_version_2)
if version_1_lenght >= version_2_lenght:
    for i in range(version_1_lenght):
        if i < version_2_lenght:
            if int(division_version_1[i]) > int(division_version_2[i]):
                print('V1')
                break
            if int(division_version_1[i]) < int(division_version_2[i]):
                print('V2')
                break
            if int(division_version_1[i]) == int(division_version_2[i]):
                continue
        else:
            if int(division_version_1[i]) > 0:
                print('V1')
                break
            else:
                if int(division_version_1[i]) == 0:
                    continue
    else:
        print('V1 = V2')
else:
    for i in range(version_2_lenght):
        if i < version_1_lenght:
            if int(division_version_1[i]) > int(division_version_2[i]):
                print('V1')
                break
            if int(division_version_1[i]) < int(division_version_2[i]):
                print('V2')
                break
            if int(division_version_1[i]) == int(division_version_2[i]):
                continue
        else:
            if int(division_version_2[i]) > 0:
                print('V2')
                break
            else:
                if int(division_version_2[i]) == 0:
                    continue
    else:
        print('V1 = V2')

r'''
1. 编写一个加密程序，其实现原理是通过替换指定的字符进行加密，附加要求是实现密文逆向检测。
'''
encrypt_txt = input('请输入要加密的文件')
need_replace_txt = input('请输入需要替换的文本')
will_releacr_txt = input('请输入将要替换的文本')
need_replace_txt_lenght = len(need_replace_txt)
will_releacr_txt_lenght = len(will_releacr_txt)
Encrypted = None
if need_replace_txt_lenght != will_releacr_txt_lenght:
    print('需要替换的字符数量必须要跟将要替换的字符数量一致')
else:
    Encrypted = encrypt_txt.translate(str.maketrans(need_replace_txt, will_releacr_txt))
    print('加密后的密文是', Encrypted)
    for i in will_releacr_txt:
        if will_releacr_txt.count(i) > 1:
            print('由于将要替换的文本出现冲突, 该文件无法解密')
            break
    for i in need_replace_txt:
        if need_replace_txt.count(i) > 1:
            print('由于需要替换的文本出现冲突, 该文件无法解密')
            break
print('test')
print('test push')