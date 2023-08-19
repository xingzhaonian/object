'''
0. with 上下文管理器最核心的功能是什么？
答: with 的核心功能是确保资源的释放, 不用去手动关闭文件

1. 请问下面代码段 A 和代码段 B 的执行结果是否等价？
f = open("FishC.txt", "w")
f.write("I love FishC.")
1 / 0
f.close()

with open("FishC.txt", "w") as f:
    f.write("I love FishC.")
    1 / 0
答: 不等价, 代码A执行到 1 / 0的时候就会报错, f.close()执行不到, 文件无法关闭和写入成功; 而代码B则可以写入成功, 因为代码B即使
报错了, 文件也能正常的进行关闭和写入成功

2. 下面是使用 pickle 保存 Python 对象的代码，请问哪里做错了？
import pickle
    
x = 250
y = 3.14
z = "FishC"
    
with open("data.pkl", "w") as f:
    pickle.dump((x, y, z), f)
答: pickle 模块是python对象序列化的第一人, 所谓序列化就是将python对象转换为二进制字节流的一个过程, 所以, 打开的模式要用'wb'

3. 如果想要读取一个 pickle 文件，是否需要预先知道其中的对象类型和数量？
答: 不需要, load() 函数会根据 dump() 函数保存的顺序，将对象逐个读取出来。

4. 请问可以使用 with 语句管理两个文件的上下文吗？
答: 可以, 比如说 with open(txt_file_path_name, 'r', encoding = 'utf-8')as a, open(result_path, 'w', encoding = 'utf-8')as b:
分别操作 a和b 是可以的
'''

from pathlib import Path
def GetCurrenFile(path, file_type, target = [] ):
    '''
    递归查找文件
    '''
    p = Path(path)
    all_file = p.iterdir()
    for i in all_file:
        sub_path = Path(i)   # 当前路径下生成子路径，判断子路径是不是文件夹，如果是，就对这个文件夹进行递归
        if i.is_dir():
            print(f'{i} 是一个文件夹')
            GetCurrenFile(sub_path, file_type, target)
        if i.is_file():
            print(f'{i} 是一个文件')
            if i.suffix == file_type:
                target.append(i)
    return target

current_path = Path.cwd()
result_file_type = '.py'
print(GetCurrenFile(current_path, result_file_type))


count = 0
def get_file_all_line(file_path):
    global count
    p = Path(file_path)
    all_file = p.iterdir()
    for i in all_file:
        sub_path = Path(i)
        if i.is_dir():
            get_file_all_line(sub_path)
        if i.is_file():
            print(f'{i}')
            f = i.open('r', encoding = 'utf-8')
            s = f.readlines()
            for i in s:
                if i != '\n':
                    count += 1
            f.close()
    return count
path = "D:\\project\\object\\python_task"
print(get_file_all_line(path))


def mkdir(path):
    p = path
    for i in range(10):
        p = p / str(i + 1)
        p.mkdir(exist_ok = True)
        p = Path.cwd()
    for i in p.iterdir():
        if i.is_dir():
            print(i)
            for k in range(10):
                with open (__file__, 'r', encoding = 'utf-8') as a, open(str(i) + '\\' + str(k) + '.py', 'w', encoding = 'utf-8') as b:
                    b.write(a.read())
mkdir(Path.cwd())