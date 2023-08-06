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
    folder = []
    p = Path.cwd()
    for i in p.iterdir():
        if i.is_dir():
            print(i)
            folder.append(i)
    return folder
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
        print(f'文件名: {i.stem + i.suffix}  文件尺寸:{i.stat().st_size} kb')

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