import tkinter as tk
from tkinter import ttk
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        pygame.mixer.init()

        self.music_file = 'D:\\Music\\陈奕迅\\陈奕迅&韩红-十年.mp3'  # 您的音乐文件路径
        self.duration = 300000  # 假设音乐长度300秒（单位毫秒）

        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play()

        self.is_dragging = False  # 标志变量，用于判断是否正在手动调整进度条

        self.progress = ttk.Scale(self.root, from_=0, to=self.duration, orient=tk.HORIZONTAL, command=self.on_change_progress)
        self.progress.pack(fill=tk.X, padx=15, pady=20)

        # 绑定鼠标按下和释放事件
        self.progress.bind("<ButtonPress-1>", self.start_drag)
        self.progress.bind("<ButtonRelease-1>", self.stop_drag)

        self.update_progress()

    def start_drag(self, event):
        self.is_dragging = True

    def stop_drag(self, event):
        self.is_dragging = False
        # 设置音乐播放的新位置
        pygame.mixer.music.rewind()
        print(self.progress.get())
        pygame.mixer.music.set_pos(int(self.progress.get()) / 1000.0)  # pygame使用秒为单位
        self.update_progress()  # 确保更新一次进度，防止拖动后不更新

    def on_change_progress(self, value):
        # 这个方法现在不做任何事情，因为我们已经在其他地方处理了逻辑
        pass

    def update_progress(self):
        if not self.is_dragging:
            current_time = pygame.mixer.music.get_pos()  # 获取当前播放位置（毫秒）
            self.progress.set(current_time)
        # 确保只在非拖动状态下更新进度条
        if not self.is_dragging:
            self.root.after(1000, self.update_progress)  # 每秒更新一次

root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()