import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QTextEdit, 
                              QFileDialog, QVBoxLayout, QWidget, 
                              QPushButton)

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建布局和组件
        layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        save_btn = QPushButton("保存")
        open_btn = QPushButton("打开")
        
        # 连接信号
        save_btn.clicked.connect(self.save_file)
        open_btn.clicked.connect(self.open_file)
        
        # 添加组件到布局
        layout.addWidget(self.text_edit)
        layout.addWidget(save_btn)
        layout.addWidget(open_btn)
        
        central_widget.setLayout(layout)
        self.setWindowTitle("简易文本编辑器")
        self.setGeometry(100, 100, 600, 400)
    
    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "保存文件")
        if filename:
            with open(filename, 'w') as f:
                f.write(self.text_edit.toPlainText())
    
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "打开文件")
        if filename:
            with open(filename, 'r') as f:
                self.text_edit.setPlainText(f.read())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec())