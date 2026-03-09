from pathlib import Path
import easygui as g
import tkinter
from tkinter import filedialog
import subprocess


result_list = []
def SearchFile(path, file_name):
    if file_name == None or file_name == ' ':
        return 
    global result_list
    p = Path(path)
    all_file = p.iterdir()
    for each in all_file:
        sub_path = Path(each)
        if each.is_dir():
            SearchFile(sub_path, file_name)
        if each.is_file():
            if file_name.lower() in str(each).lower():
                result_list.append(sub_path)


def openFile():
    while True:
        path = Path('O:\皇上快点')
        file_name = g.enterbox(msg = '请输入要搜索的文件', title = '文件搜索')
        if file_name == None:
            break
        SearchFile(path, file_name)
        print(result_list)
        if len(result_list) == 1:
            choice_result = g.ccbox(msg=result_list[0], title='选择以下文件并打开', choices=('打开', '取消'))
            single = str(result_list[-1])
            if '&' in single:
                single = list(single)
                single.insert(0, "&")
                single.insert(1, '"')
                single.insert(len(single), '"')
                single = ''.join(single)
            if choice_result:
                try:
                    print('准备调用打开方法')
                    subprocess.run(['powershell', '-Command', single])
                    print('打开方法调用完毕')
                except :
                    result_list.clear()
                    continue
                result_list.clear()
                continue
            else:
                result_list.clear()
                continue
        if not result_list:
            result_list.clear()
            continue
        else:
            choice_result = g.choicebox(msg='搜索结果', title='选择以下文件并打开', choices=result_list)
            print(choice_result)
            if choice_result == None:
                result_list.clear()
                continue
            else:
                if '&' in choice_result:
                    choice_result = list(choice_result)
                    choice_result.insert(0, "&")
                    choice_result.insert(1, '"')
                    choice_result.insert(len(choice_result), '"')
                    choice_result = ''.join(choice_result)
                try:
                    print('准备调用打开方法')
                    print(choice_result)
                    subprocess.run(['powershell', '-Command', choice_result])
                    print('打开方法调用完毕')
                except:
                    result_list.clear()
                    continue
        result_list.clear()
openFile()
#if __name__ == '__main__':
#   openFile()

