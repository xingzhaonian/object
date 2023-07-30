r'''
0. 如果尝试使用 open() 函数打开一个不存在的文件，是否会报错？
答: 不会哦, 这取决于使用什么模式打开, 如果用'r' 模式就会报错, 但是使用 'w' 模式就不会
'r' 模式表示打开文件并可以进行读取    'w' 模式表示创建文件

1. “在打开一个文件对象之后，大多数的文件操作都是在缓冲区里面进行的。因此，如果希望将文件内容保存，我们需要使用 close() 方法关闭文件对象，这样数据才能从缓冲区写入到文件中。”
那么请问大家，有没有办法在不关闭文件对象的情况下，进行内容的保存呢？
答: 我们可以使用 flush() 方法

2. 请问如果指定 readline(size=-1) 方法的 size 参数为 3, 那么表示的含义是什么？
答: size表示读取字符个数

3. 请问下面代码会在文件中写入几行字符串呢？
f = open("FishC.txt", "w")
f.writelines(["FishA", "FishB", "FishC"])
 f.close()
答: 一行

4. 请问在课堂中的代码，为什么我们写入的时候只有一个换行符，但是使用 for 语句读取并打印出来却多了一个空白行呢？
 f = open("FishC.txt", "w")
 f.writelines(["I love FishC.", "I love my wife."])
 f.close()
 f = open("FishC.txt", "r")
 for each in f:
     print(each)

I love FishC.
   
I love my wife.
答: 因为 print() 函数默认是会在末尾添加一个换行符

5. 请问下面代码为什么会报错？
f = open("C:\Users\goodb\Desktop\FishC.txt", "w")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
答: 因为路径中存在转义字符，导致文件路径解析错误

6. 使用 "w" 模式打开文件之前一定要注意什么？
答: 一定要注意该文件是否存在, 如果存在的话, 它会创建一个新的空文件覆盖之前老的, 老的文件就没了

7. 如果一个文件不存在，是否可以使用 "a" 模式将其打开？
答: 可以, 会创建一个新的文件

8. 文件指针的作用是什么？
答: 指示文件对象当前读取或者写入的位置。

9. 什么是 EOF？
答: end of the file,  文件末尾了

10. 如何知道文件指针当前指定的位置？
答: 使用 tell() 方法, 不过可能不准, 在一个全是英文的文件中, 1个字符占一个字节没有问题, 但是中英文混合的时候就不好用了, 因为
1个中文字符占3个字节, 所以返回的位置就不准
'''

def file_1():
    a = open('D:\\python_file\\FishC.txt', 'r')
    move_seek = a.seek(10)
    temp_txt = a.readline(5)
    new_a = open('D:\\python_file\\FishD.txt', 'w')
    new_a.write(temp_txt)
    a.close()
    new_a.close()


def file_2():
    f = open('D:\\python_file\\FishC.txt', 'r+')
    f.seek()
    f.truncate(10)
    f.close()

def open_myself():
    f = open('D:\\project\\object\\python_task\\053.py', 'r', encoding = 'utf-8')
    while True:
        read_data = f.readline()
        print(read_data)
        if not read_data:
            break

def target():
    f1 = open('D:\\python_file\\hw\\target.zip', 'rb')
    f2 = open('D:\\python_file\\hw\\test.jpg', 'ab')
    f2.write(f1.read())
    f1.close()
    f2.close()

target()
