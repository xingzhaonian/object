import tkinter as tk
from tkinter import simpledialog, messagebox
import os
from pathlib import Path
import subprocess

class ScrollableListboxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("文件搜索")
        self.root.geometry("650x350")
        

        self.path = Path('O:\docs\皇上快点\数值文档')
        # 存储历史记录
        self.history = []

        self.result_list = []
        
        # 创建顶部按钮框架
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill=tk.X, padx=50, pady=10)
        
        # 创建历史按钮
        self.search_btn = tk.Button(self.button_frame, text="历史记录",command=self.show_history, bg="#2196F3",fg="white", width=10)
        self.search_btn.pack(side=tk.LEFT, padx=5)
        tk.Label(self.button_frame, text="输入要搜索的文件:").pack(side=tk.LEFT)
        
        # 搜索输入框
        self.search_entry = tk.Entry(self.button_frame, width=40)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind("<Return>", lambda event: self.search_item())  # 回车键搜索

        
        # 创建搜索按钮
        self.history_btn = tk.Button(self.button_frame, text="搜索", command=self.search_item, bg="#4CAF50", fg="white",width=10)
        self.history_btn.pack(side=tk.LEFT, padx=5)
        
        # 创建列表框架
        self.list_frame = tk.Frame(root)
        self.list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 创建垂直滚动条
        self.scrollbar = tk.Scrollbar(self.list_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 创建列表框
        self.listbox = tk.Listbox(self.list_frame,yscrollcommand=self.scrollbar.set,selectmode=tk.SINGLE,bg="white",font=('Arial',12),height=15)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # 配置滚动条
        self.scrollbar.config(command=self.listbox.yview)
        # 绑定双击事件
        self.listbox.bind("<Double-Button-1>", self.open_file)
        
    

    
    def search_item(self):    #搜索文件
        self.listbox.delete(0, tk.END)
        self.result_list.clear()
        file_name = self.search_entry.get()
        for root, directories, files in os.walk( self.path):
            for file in files:
                if file_name == None or file_name == '':
                    break
                if file_name.lower() in file.lower():
                    if '&' in file_name:
                        result_path = list(str(Path(root, file)))
                        result_path.insert(0, '"')
                        result_path.insert(len(result_path), '"')
                        self.result_list.append(''.join(result_path))
                    else:
                        self.result_list.append(str(Path(root, file)))
        if self.result_list:
            for file in self.result_list:
                self.listbox.insert(tk.END, file)
        else:
             messagebox.showinfo('未找到文件！！！')


    def show_history(self):   #展示历史记录
        self.listbox.delete(0, tk.END)
        self.result_list.clear()
        if self.history:
            for file_name in self.history:
                self.listbox.insert(tk.END, file_name)


    def open_file(self, event):
        # 双击事件处理
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            original_value = self.listbox.get(index)
            if '&' in original_value:
                value = list(original_value)
                value.insert(0, "&")
                value.insert(1, '"')
                value.insert(len(value), '"')
                value = ''.join(value)
                subprocess.run(['powershell', '-Command', value])
                print(f'打开{value}已执行')
            else:
                subprocess.run(['powershell', '-Command', original_value])
                print(f'打开{original_value}已执行')
            if original_value not in self.history:
                self.history.append(original_value)

            

if __name__ == "__main__":
    root = tk.Tk()
    app = ScrollableListboxApp(root)
    root.mainloop()