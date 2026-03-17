import tkinter as tk
from tkinter import ttk
import threading
import time
import pyautogui
from pynput import keyboard
import sys

# 全局变量
is_clicking = False
click_interval = 0.1  # 默认 0.1秒 = 10次/秒
listener = None

def start_clicking():
    """开始连点"""
    global is_clicking
    is_clicking = True
    # 最小化窗口
    root.iconify()
    
def stop_clicking():
    """停止连点"""
    global is_clicking
    is_clicking = False

def click_worker():
    """鼠标点击工作线程"""
    while True:
        if is_clicking:
            pyautogui.click()
        time.sleep(click_interval)

def on_press(key):
    """键盘监听回调"""
    global click_interval
    try:
        if key == keyboard.Key.f9:
            if not is_clicking:
                # 获取输入的频率
                try:
                    freq = float(freq_entry.get())
                    if freq > 0:
                        click_interval = 1.0 / freq
                except:
                    click_interval = 0.1  # 默认10次/秒
                start_clicking()
            else:
                stop_clicking()
    except:
        pass

def start_listener():
    """启动键盘监听"""
    global listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def on_closing():
    """窗口关闭事件"""
    global is_clicking, listener
    is_clicking = False
    if listener:
        listener.stop()
    root.destroy()
    sys.exit(0)

# 创建主窗口
root = tk.Tk()
root.title("鼠标连点器")
root.geometry("300x200")
root.resizable(False, False)

# 设置窗口置顶
root.attributes("-topmost", True)

# 标题
title_label = tk.Label(root, text="鼠标连点器", font=("Microsoft YaHei", 14, "bold"))
title_label.pack(pady=10)

# 频率设置
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="点击频率:", font=("Microsoft YaHei", 10)).grid(row=0, column=0, padx=5)
freq_entry = tk.Entry(frame, width=10, font=("Microsoft YaHei", 10))
freq_entry.grid(row=0, column=1, padx=5)
freq_entry.insert(0, "10")  # 默认10次/秒
tk.Label(frame, text="次/秒", font=("Microsoft YaHei", 10)).grid(row=0, column=2, padx=5)

# 提示信息
info_frame = tk.Frame(root)
info_frame.pack(pady=15)

tk.Label(info_frame, text="F9: 启动/停止连点", font=("Microsoft YaHei", 9), fg="blue").pack()
tk.Label(info_frame, text="启动后自动最小化", font=("Microsoft YaHei", 8), fg="gray").pack()
tk.Label(info_frame, text="再次按F9停止", font=("Microsoft YaHei", 8), fg="gray").pack()
tk.Label(info_frame, text="停止后需手动恢复窗口", font=("Microsoft YaHei", 8), fg="gray").pack()

# 启动键盘监听
start_listener()

# 启动点击线程
click_thread = threading.Thread(target=click_worker, daemon=True)
click_thread.start()

# 窗口关闭事件
root.protocol("WM_DELETE_WINDOW", on_closing)

# 运行主循环
root.mainloop()