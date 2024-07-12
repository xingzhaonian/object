import tkinter as tk
from tkinter import ttk

class ExampleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Progress Bar Example")

        # 创建一个水平滑动条
        self.progress = ttk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL)
        self.progress.pack(fill=tk.X, padx=15, pady=20, expand=True)

        # 定时更新进度条
        self.update_progress()

    def update_progress(self):
        # 获取当前进度条的值
        current_value = self.progress.get()

        # 每次调用增加10，直到达到最大值
        if current_value < 100:
            self.progress.set(current_value + 10)
        else:
            self.progress.set(0)  # 或者停止更新，或者重置为0重新开始

        # 每1000毫秒（1秒）调用一次自身，更新进度条
        self.root.after(1000, self.update_progress)

root = tk.Tk()
app = ExampleApp(root)
root.mainloop()