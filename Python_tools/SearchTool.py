import tkinter as tk
from tkinter import simpledialog, messagebox
import os
from pathlib import Path
import subprocess
import platform

class ScrollableListboxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("文件搜索")
        self.root.geometry("650x350")
        
        self.path = Path('D:\\')
        self.history = []  # 存储历史记录
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
        self.listbox = tk.Listbox(self.list_frame, yscrollcommand=self.scrollbar.set,
                                selectmode=tk.SINGLE, bg="white", font=('Arial',12), height=15)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.listbox.yview)
        
        # 绑定双击事件
        self.listbox.bind("<Double-Button-1>", self.open_file)
        
        # 添加右键菜单功能
        self.setup_context_menu()
    
    def setup_context_menu(self):
        """设置右键上下文菜单"""
        self.context_menu = tk.Menu(self.listbox, tearoff=0)
        self.context_menu.add_command(
            label="打开文件所在文件夹",
            command=self.open_file_location
        )
        # 绑定右键点击事件
        self.listbox.bind("<Button-3>", self.show_context_menu)
    
    def show_context_menu(self, event):
        """显示右键菜单"""
        # 获取点击的行
        index = self.listbox.nearest(event.y)
        if index >= 0:  # 确保点击的是有效行
            self.listbox.selection_clear(0, tk.END)
            self.listbox.selection_set(index)
            self.listbox.activate(index)
            # 显示菜单
            self.context_menu.post(event.x_root, event.y_root)
    
    def open_file_location(self):
        """打开文件所在文件夹"""
        selection = self.listbox.curselection()
        if selection:
            file_path = self.listbox.get(selection[0])
            self.reveal_in_explorer(file_path)
    
    def reveal_in_explorer(self, path):
        """根据不同操作系统打开文件所在文件夹"""
        path = os.path.normpath(path.strip('"'))  # 去除可能的引号
        
        if platform.system() == "Windows":
            if os.path.isfile(path):
                # Windows: 选中文件
                subprocess.run(f'explorer /select,"{path}"', shell=True)
            elif os.path.isdir(path):
                # Windows: 打开文件夹
                subprocess.run(f'explorer "{path}"', shell=True)
        elif platform.system() == "Darwin":
            # macOS: 显示文件并选中
            subprocess.run(["open", "-R", path])
        else:
            # Linux: 打开所在文件夹
            subprocess.run(["xdg-open", os.path.dirname(path)])
    
    # 以下是原有方法保持不变...
    def search_item(self):    #搜索文件
        self.listbox.delete(0, tk.END)
        self.result_list.clear()
        file_name = self.search_entry.get()
        for root, directories, files in os.walk(self.path):
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