#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:xingzhaonian

import tkinter

window = tkinter.Tk()   # 创建窗口
window.title('测试窗口')  # 添加title
window.geometry('500x300+700+350')  # 设置窗口大小

tag_var = tkinter.StringVar()
tag_var.set('当前为x模式')
label = tkinter.Label(window, textvariable=tag_var, bg='red', font=('SimHei', 20))  # 创建标签
label.place(x=170, y=20)  # 放置标签



is_clieck = None
but_var = tkinter.StringVar()
but_var.set('切换为y模式')
def on_clieck():
    global is_clieck
    if is_clieck:
        tag_var.set('当前为x模式')
        is_clieck = False
        but_var.set('切换y模式')
    else:
        tag_var.set('当前为y模式')
        is_clieck = True
        but_var.set('切换x模式')


but = tkinter.Button(window, textvariable=but_var,  font=('SimHei', 15), width=15, height=1, command=on_clieck)
but.place(x=170, y=120)



window.mainloop()
