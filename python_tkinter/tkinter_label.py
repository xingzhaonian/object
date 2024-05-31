#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:xingzhaonian

import tkinter
window = tkinter.Tk()       # 创建窗口对象
window.title('计算',)       # 窗口标题
window.geometry('500x300+700+350')      # 设置窗口大小, 500x300为大小, +700, +500 为在屏幕中间显示的偏移位置
l = tkinter.Label(window, text='你好, this is Tkinter', bg='green', font=('Arial', 15), width=30, height=3)   # 设置标签: 使用tkinter.Label方法, 参数1为 window窗口对象; text为标签的文字, 数据类型为字符串;  bg为背景颜色,数据类型为字符串; font为字体和文字大小, 需要一个元组, 元组内的第一个参数为字体, 第二个是文字大小, width为标签宽度, height为标签长度
l.pack()  #  放置该Label, Label内容content区域放置Label, 自动调节尺寸
window.mainloop()          # 窗口对象进行循环,每点击一次就会更新一次, 此方法是阻塞的




