from pathlib import Path

def get_current_working_directory():
    '''
    使用 pathlib 模块，获取当前的工作目录
    '''
    current_working_directory = Path.cwd()
    print(current_working_directory)
    return current_working_directory
get_current_working_directory()

def RelativePathConvertAbsolutePath():
    '''
    相对路径转换为绝对路径
    '''
    Path('./doc')
    print(Path('./doc').resolve())
    return Path('./doc').resolve()
RelativePathConvertAbsolutePath()

def current_is_dir():
    p = Path.cwd()
    if p.is_dir():
        p = p / 'FishC.txt'
        print(p)
        return p
current_is_dir()

def GetCurrentDirectoryAllSubDirectory():
    '''
    获取当前目录下的所有子文件夹
    '''
    p = Path.cwd()
    l = [i for i in p.iterdir() if i.is_dir()]
    print(l)
    return l 
GetCurrentDirectoryAllSubDirectory()

def GetCurrentFileSize():
    '''
    获取当前文件夹下的文件数量和所有文件尺寸
    '''
    p = Path.cwd()
    count = 0
    s = p.iterdir()
    for i in p.iterdir():
        count += 1
        print(f'文件名：{i.name}  文件尺寸:{i.stat().st_size} kb')

GetCurrentFileSize()

def GetCurrentFileTime():
    import time 
    '''
    获取当前文件夹下的文件数量和所有文件尺寸
    '''
    p = Path.cwd()
    count = 0
    for i in p.iterdir():
        count += 1
        print(f'文件名: {i.stem + i.suffix}  修改时间:{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(i.stat().st_mtime)))}')
GetCurrentFileTime()


def GetAllFileSize():
    dic_file = {}
    p = Path('D:\project\object\python_task')
    for i in p.iterdir():
        dic_file[i.name] = i.stat().st_size
    new_dic = (sorted(dic_file.items(), key = lambda s:s[1]))
    for i in new_dic:
        print(f'{i[0]}  ({(i[1])})字节')
GetAllFileSize()



def GetLastModificationFile():
    import time 
    dic_file = {}
    p = Path('D:\project\object\python_task')
    for i in p.iterdir():
        dic_file[i.name] = i.stat().st_atime
    new_dic = (sorted(dic_file.items(), key = lambda s:s[1], reverse = True))
    print(f'(修改时间 -> {time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(new_dic[0][1])))}, 文件名 -> {new_dic[0][0]})')
GetLastModificationFile()