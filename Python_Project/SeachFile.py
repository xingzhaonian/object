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
        print(SeachName)
        if SeachName == None:
            break
        if SeachName == '':
            g.msgbox(msg='输入为空, 请重新输入')
            continue
        start_time = time.time()
        for i in AllSpace:
            print(i[0])
            subprocess.run(' echo "搜索中, 请稍后···"', shell=True)
            Search(i[0], file_name = SeachName)
        end_time = time.time()
        result_time = end_time - start_time
        print(f'搜索完成, 共找到{len(target)}个文件, 耗时{result_time}秒')
        print(len(target))
        if len(target) == 0:
            continue
        if len(target) == 1:
            result = g.ccbox(msg = target[-1], title='打开文件', choices =('打开', '取消'))
            if result:
                try :
                    subprocess.run(['powershell', '-Command', str(target[-1])], timeout=1)
                except subprocess.TimeoutExpired:
                    target.clear()
                    continue
        result = g.choicebox(msg='选择打开文件并打开', title='打开文件', choices = target)
        try:
            subprocess.run(['powershell', '-Command', str(result)], timeout=1)
        except subprocess.TimeoutExpired:
            target.clear()
            continue
        target.clear()

if __name__ == '__main__':
    AllSeach()


