'''
=============文件储存===================
打开文件使用open() 函数, 把打开的结果赋值给一个变量
open()函数第一个参数文件路径, 第二个为打开模式; 第一个参数如: 'C:\Users\Administrator.DESKTOP-SAM6F91\AppData\Local\Programs\Python\Python311'
第二个参数为模式, 表示使用什么模式打开该文件, 例如 f = oopen('D:\\Project_Flie\\object\\Python_StudyCourse', w)

文件对象的各种方法
f.cloose()------关闭文件
f.flush() ------将文件对象中的缓存数据写入到文件中(某种情况下不一定有效)
f.read(size = -1, /)  ------从文件对象中读取指定剩余字符(或者遇到EOF停止); 当未指定该参数或该参数
为负值的时候, 读取剩余的所有字符
f.readable()----判断该文件对象是否支持读取(返回值为False, 调用read()方法会导致OS Error异常)
f.readline(size = -1, /)-----从文件对象中读取一行字符串(包括换行符), 如果指定了size参数, 则读取size个字符
f.seek(offset, whence = 0, /) ------修改文件指针的位置, 从whence参数指定的位置(0代表文件起始位置, 1代表当前位置, 2代表文件末尾)
偏移offset个字节, 返回值是新的索引位置
f.seekable()-----判断该文件对象是否支持修改文件指针的位置, 如果返回值为False, 则调用seek(), tell(), turncate()方法                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         






'''