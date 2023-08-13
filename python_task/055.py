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
答: 应该要知道吧, 读取到最后, 下面已经没有东西了, 再读就会报错

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
        sub_path = Path(i)  # 这里是重点, 每次循环生成一个子路径, 判断该路径是不是文件夹, 如果是文件夹, 那么就对这文件夹进行递归
        print(sub_path)
        if i.is_dir():
            print(f'{i} 是一个文件夹')
            GetCurrenFile(sub_path, file_type, target)
        if i.is_file():
            print(f'{i} 是一个文件')
            if i.suffix == file_type:
                print('找到了目标文件类型, 进行添加')
                target.append(i)
    return target

current_path = Path.cwd()
result_file_type = '.pkl'
GetCurrenFile(current_path, result_file_type)