'''
=============文件储存===================
打开文件使用open() 函数, 把打开的结果赋值给一个变量
open()函数第一个参数文件路径, 第二个为打开模式; 第一个参数如: 'C:\Users\Administrator.DESKTOP-SAM6F91\AppData\Local\Programs\Python\Python311'
第二个参数为模式, 表示使用什么模式打开该文件, 例如 f = open('D:\\Project_Flie\\object\\Python_StudyCourse', w)

[文件打开方式]
'r' ----------- 读取(默认)
'w' ----------- 写入(如果文件已经存在, 则先截断清空文件)
'x' ----------- 排他性创建文件(如果文件已经存在， 则打开(创建)失败)
'a' ----------- 追加(如果文件已经存在, 则在末尾追加内容)
'b' ----------- 二进制模式打开文件
't' ----------- 文本模式
'+' ----------- 更新文件(读取和写入)
'b' 可以和别的模式一起用, 比如 'rb' 表示用二进制模式打开进行读取, 'wb'表示二进制模式打开进行写入, 'ab'表示二进制模式打开追加写入

[文件对象的各种方法]
f.cloose()------关闭文件
f.flush() ------将文件对象中的缓存数据写入到文件中(某种情况下不一定有效)
f.read(size = -1, /)  ------从文件对象中读取指定剩余字符(或者遇到EOF停止); 当未指定该参数或该参数
为负值的时候, 读取剩余的所有字符
f.readable()----判断该文件对象是否支持读取(返回值为False, 调用read()方法会导致OS Error异常)
f.readline(size = -1, /)-----从文件对象中读取一行字符串(包括换行符), 如果指定了size参数, 则读取size个字符个数
f.seek(offset, whence = 0, /) ------修改文件指针的位置, 从whence参数指定的位置(0代表文件起始位置, 1代表当前位置, 2代表文件末尾)
偏移offset个字节, 返回值是新的索引位置
f.seekable()-----判断该文件对象是否支持修改文件指针的位置, 如果返回值为False, 则调用seek(), tell(), turncate()方法都会导致OSError异常
f.tell()------返回当前文件指针在对象中的位置
f.turncate(pos = None, /)-----将文件对象截取到pos的位置, 默认是截取到文件指针当前的位置
f.write(text, /)------将字符串写入到文件对象中, 并返回写入的字符数量(字符的长度)
f.writable()-----判断该文件对象是否支持写入(如果返回False, 则调用write()方法会导致OSError异常)
f.writelines(lines, /)------将一系列字符串写入到文件对象中(不会自动添加换行符, 所以通常人为的加在每个字符串的末尾)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         d
[处理路径]
可以使用旧的os模块和新的pathlib模块
[pathlib]模块
from pathlib import Path
Path('路径名称') 生成 WindowsPath路径
比如: p = Path('D:/python_file'), p 就是 WindowsPath('D:/python_file'), / 可以对WindowsPath路径进行拼接
比如: q = p / 'FishC.txt', q就是WindowsPath('D:/python_file/FishC.txt')
Path.cwd()-------------------方法获取当前工作目录
Path.is_dir()----------------判断一个路径是否为一个文件夹
Path.is_file()---------------判断一个路径是否为一个文件
Path.exists()----------------判断一个路径是否存在
Path.name--------------------name属性可以获取路径的最后一个部分
Path.stem--------------------stem属性获取文件的文件名
Path.suffix------------------suffix属性获取文件的后缀
Path.parent------------------parent属性获取其父级目录
Path.parents-----------------parents属性获取其逻辑祖先构成的一个不可变序列
Path.parts-------------------parts属性将路径的各个组件拆分为元组
Path.stat()------------------stat()方法用来查询文件的信息状态(文件信息中有很多数据,比如Path.stat().st_size 可以获取该文件的尺寸)
Path.iterdir()---------------iterdir()方法可以获取当前路径下所有的子文件和子文件夹
Path.mkdir()-----------------mkdir()可以创建一个新文件夹(Path路径应该是一个当前不存在新的文件夹, 否则报错; mkdir()中参数
exist_ok = True 则可忽略报错, 如果Path中存在多个不存在的父级目录也会报错, mkdir()中参数parents = True 会将路径中不存在的
一个或多个文件夹创建出来, 使得这个Path是一个存在的路径文件夹)
Path.open()------------------open()方法可以打开一个文件, 除了不用传入路径(因为Path就是路径), 其余跟普通open是一样的
Path.rename()----------------rename()可以给文件重新命名, rename中要包含绝对路径, 例如 Path = 'D:/python_file/hw/haha/fishc/a/b/c/fishc.txt'
那么p.rename('D:/python_file/hw/haha/fishc/a/b/c/fishcsdfsdf.txt')就把'D:/python_file/hw/haha/fishc/a/b/c/fishc.txt'的 fishc.txt 改为了 fishcsdfsdf.txt
Path.rmdir()-----------------rmdir()适用于删除文件夹
Path.unlink()----------------unlink()适用于删除文件
Path.glob()------------------glob()可以查找Path目录下的文件, 例如Path.glob('*.txt') 查找Path路径下的所有txt文件, 返回一个generator(生成器); 如果是找某一个文件的话,比如 Path.glob('fishc.txt')
返回 FishCd.txt 文件绝对路径的generator(生成器) 
如果要查找当前目录的下一级目录中的所有.txt文件, 可以这么写 Path.glob('*/*.txt')
如果希望向下递归的搜索, 也就是说查找当前目录以及该目录下面的所有子目录中的txt文件, 那么我们可以使用两个 ' ** '表示, Path.glob('**/*.txt')


[绝对路径]
绝对路径是文件真正存在的路径, 如果一个路径从根目录开始, 然后一级一级的指向最终的文件或文件夹, 那么这个路径就是绝对路径

[相对路径]
相对路径是以当前目录作为基准, 进行一级一级的目录推导的一个路径, '.' 表示当前所在的目录, '..'表示上一级路径
对于相对路径, 有一个resolve()的方法, 可以将相对路径转为绝对路径 










'''