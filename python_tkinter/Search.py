import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

class SearchTool:
    def __init__(self, root):
        self.root = root
        self.root.title("搜索工具")
        self.root.geometry("500x400")
        
        # 搜索历史记录
        self.search_history = []
        
        # 创建界面组件
        self.create_widgets()
    
    def create_widgets(self):
        # 搜索框框架
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10, padx=10, fill=tk.X)
        
        # 搜索标签
        tk.Label(search_frame, text="搜索内容:").pack(side=tk.LEFT)
        
        # 搜索输入框
        self.search_entry = tk.Entry(search_frame, width=40)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind("<Return>", lambda event: self.do_search())  # 回车键搜索
        
        # 按钮框架
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)
        
        # 搜索按钮
        search_btn = tk.Button(button_frame, text="搜索", command=self.do_search)
        search_btn.pack(side=tk.LEFT, padx=5)
        
        # 取消按钮
        cancel_btn = tk.Button(button_frame, text="取消", command=self.cancel_search)
        cancel_btn.pack(side=tk.LEFT, padx=5)
        
        # 历史记录按钮
        history_btn = tk.Button(button_frame, text="历史记录", command=self.show_history)
        history_btn.pack(side=tk.LEFT, padx=5)
        
        # 清空历史按钮
        clear_btn = tk.Button(button_frame, text="清空历史", command=self.clear_history)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # 结果显示区域
        result_frame = tk.Frame(self.root)
        result_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # 结果标签
        tk.Label(result_frame, text="搜索结果:").pack(anchor=tk.W)
        
        # 结果文本框
        self.result_text = tk.Text(result_frame, height=15, wrap=tk.WORD)
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        # 滚动条
        scrollbar = tk.Scrollbar(self.result_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)
    
    def do_search(self):
        """执行搜索操作"""
        search_term = self.search_entry.get().strip()
        
        if not search_term:
            messagebox.showwarning("警告", "请输入搜索内容")
            return
        
        # 记录搜索历史
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.search_history.append((timestamp, search_term))
        
        # 模拟搜索结果 - 实际应用中这里可以替换为真正的搜索逻辑
        result = f"搜索内容: {search_term}\n"
        result += f"模拟结果: 找到关于'{search_term}'的10条相关信息\n"
        result += "-" * 50 + "\n"
        
        # 显示结果
        self.result_text.insert(tk.END, result)
        self.result_text.see(tk.END)  # 滚动到最新结果
        
        # 清空搜索框以便输入新内容
        self.search_entry.delete(0, tk.END)
    
    def cancel_search(self):
        """取消搜索"""
        self.search_entry.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)
    
    def show_history(self):
        """显示搜索历史"""
        if not self.search_history:
            messagebox.showinfo("历史记录", "没有搜索历史")
            return
        
        # 创建历史记录窗口
        history_window = tk.Toplevel(self.root)
        history_window.title("搜索历史")
        history_window.geometry("400x300")
        
        # 历史记录列表
        history_listbox = tk.Listbox(history_window)
        history_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 添加历史记录到列表
        for timestamp, term in reversed(self.search_history):
            history_listbox.insert(tk.END, f"{timestamp}: {term}")
        
        # 双击历史记录可以重新搜索
        def on_history_select(event):
            selection = history_listbox.curselection()
            if selection:
                selected_item = history_listbox.get(selection[0])
                search_term = selected_item.split(": ", 1)[1]
                self.search_entry.delete(0, tk.END)
                self.search_entry.insert(0, search_term)
                self.do_search()
                history_window.destroy()
        
        history_listbox.bind("<Double-Button-1>", on_history_select)
    
    def clear_history(self):
        """清空搜索历史"""
        if not self.search_history:
            return
        
        if messagebox.askyesno("确认", "确定要清空所有搜索历史吗？"):
            self.search_history = []
            messagebox.showinfo("成功", "搜索历史已清空")

if __name__ == "__main__":
    root = tk.Tk()
    app = SearchTool(root)
    root.mainloop()