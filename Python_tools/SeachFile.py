from pathlib import Path
import psutil
import os
import easygui as g
import time
import subprocess


AllSpace = psutil.disk_partitions()
target = []

def Search(path, file_name):
    global target
    for root, directories, files in os.walk(path):
        for file in files:
            if file_name == None or file_name == '':
                continue
            if file_name in file:
                if '&' in file_name:
                    result_path = list(str(Path(root, file)))
                    result_path.insert(0, '"')
                    result_path.insert(len(result_path), '"')
                    target.append(''.join(result_path))
                else:
                    target.append(str(Path(root, file)))


def AllSeach():
    while True:
        SeachName = g.enterbox(msg='输入要查找的文件', title='文件查找')
        SeachScope_list = ['overall_situation']
        for i in AllSpace:
            SeachScope_list.append(i[0])
        TargetSeachScope = g.choicebox(msg='请选择查找区域', title='文件查找', choices=SeachScope_list)
        print(TargetSeachScope)
        if SeachName == None:
            break
        if SeachName == '':
            g.msgbox(msg='输入为空, 请重新输入')
            continue
        if TargetSeachScope in "C:\\" or TargetSeachScope in 'D:\\' or TargetSeachScope in 'E:\\' or TargetSeachScope in 'F:\\':
            start_time = time.time()
            Search(TargetSeachScope, SeachName)
            end_time = time.time()
            result_time = end_time - start_time
            if len(target) == 1:
                result = g.ccbox(msg = target[-1], title='打开文件', choices =('打开', '取消'))
                if result:
                    try :
                        subprocess.run(['powershell', '-Command', str(target[-1])], timeout=1)
                    except subprocess.TimeoutExpired:
                        target.clear()
                        continue
            else:
                result = g.choicebox(msg = '搜索结果', title='选择以下文件并打开', choices = target)
                if result:
                    try :
                        subprocess.run(['powershell', '-Command', str(target[-1])], timeout=1)
                    except subprocess.TimeoutExpired:
                        target.clear()
                        continue
        else:
            if not SeachName:
                break
            if SeachName == '':
                g.msgbox(msg='输入为空, 请重新输入')
                continue

if __name__ == '__main__':
    AllSeach()


