import tkinter as tk

def setup_text_widget(root):
    # 创建 Text 控件
    text_area = tk.Text(root, wrap=tk.WORD, width=40, height=10, font=("Times New Roman", 15))
    text_area.pack(padx=10, pady=10)
    
    # 创建一个名为 'right' 的标签，用于右对齐文本
    text_area.tag_configure('right', justify='right')
    
    # 插入文本并应用 'right' 标签
    text_area.insert(tk.END, "This text is right aligned.\n", 'right')
    text_area.insert(tk.END, "This text is also right aligned.\n", 'right')
    
    # 你也可以插入不使用任何标签的普通文本（默认左对齐）
    text_area.insert(tk.END, "This text is left aligned.\n")
    
    # 禁止编辑
    text_area.config(state=tk.DISABLED)

    return text_area

def main():
    root = tk.Tk()
    root.title("Right Aligned Text in Tkinter Text Widget")

    text_widget = setup_text_widget(root)

    root.mainloop()

if __name__ == "__main__":
    main()