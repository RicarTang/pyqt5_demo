import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel,QLineEdit,QTextEdit,QFrame,QSplitter,
    QHBoxLayout, QVBoxLayout, QApplication)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Tool(QWidget):
    def __init__(self):
        # 调用父类构造函数
        super().__init__()
        # 设置控件
        self.set_control()
        # 设置布局
        self.set_layout()
        # button监听事件，信号插槽
        self.button.clicked.connect(self.show_text)
        
        # resize与move方法的整合方法，窗口大小与鼠标放大缩小/移动
        self.setGeometry(300,300,500,300)
        self.setWindowTitle("Tool")
        # 设置窗口图标
        self.setWindowIcon(QIcon("./tool.jpg"))
        # 显示窗口
        self.show()
    
    def set_control(self):
        """设置窗口控件"""
        # button
        self.button = QPushButton()
        # textEdit
        self.text_edit = QTextEdit()
        # lable
        self.lable_android = QLabel(self)
        self.lable_version = QLabel(self)
        self.lable_desription = QLabel(self)
        self.lable_header = QLabel(self)
        self.lable_title = QLabel(self)
        self.lable_force = QLabel(self)
        self.lable_android.setText("android")
        self.lable_version.setText("version")
        self.lable_desription.setText("desription")
        self.lable_header.setText("header")
        self.lable_title.setText("title")
        self.lable_force.setText("force")
        # lineEdit
        self.line_android = QLineEdit()
        self.line_version = QLineEdit()
        self.line_desription = QLineEdit()
        self.line_header = QLineEdit()
        self.line_title = QLineEdit()
        self.line_force = QLineEdit()
        self.button = QPushButton("start")
        self.text = QTextEdit()

    def set_layout(self):
        """设置窗口布局"""
        # splitter分隔
        # 左上
        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)
        # # 右上
        # topright = QFrame()
        # topright.setFrameShape(QFrame.StyledPanel)
        # 下
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        # 分隔符
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(self.text_edit)
        splitter1.setSizes([200,100])  # 设置大小
        
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        splitter2.setSizes([400,100])
        
        # 全局
        self.wlayout = QVBoxLayout(self)
        # 局部
        self.hlayout1 = QHBoxLayout()  
        self.hlayout2 = QHBoxLayout()  
        self.hlayout3 = QHBoxLayout()  
        self.hlayout4 = QHBoxLayout()  
        self.hlayout5 = QHBoxLayout()  
        self.hlayout6 = QHBoxLayout()  
        self.hlayout7 = QHBoxLayout()  
        self.vlayout1 = QVBoxLayout()
        self.vlayout2 = QVBoxLayout()

        # 添加控件
        # android
        self.hlayout1.addWidget(self.lable_android)
        self.hlayout1.addWidget(self.line_android)
        # version
        self.hlayout2.addWidget(self.lable_version)
        self.hlayout2.addWidget(self.line_version)
        # desription
        self.hlayout3.addWidget(self.lable_desription)
        self.hlayout3.addWidget(self.line_desription)
        # header
        self.hlayout4.addWidget(self.lable_header)
        self.hlayout4.addWidget(self.line_header)
        # title
        self.hlayout5.addWidget(self.lable_title)
        self.hlayout5.addWidget(self.line_title)
        # force
        self.hlayout6.addWidget(self.lable_force)
        self.hlayout6.addWidget(self.line_force)
        # button
        self.hlayout7.addWidget(self.button)

        # 添加布局
        # 标签/输入框垂直布局
        self.vlayout1.addLayout(self.hlayout1)
        self.vlayout1.addLayout(self.hlayout2)
        self.vlayout1.addLayout(self.hlayout3)
        self.vlayout1.addLayout(self.hlayout4)
        self.vlayout1.addLayout(self.hlayout5)
        self.vlayout1.addLayout(self.hlayout6)
        self.vlayout1.addLayout(self.hlayout7)
        # 垂直布局1添加到topleft Frame
        topleft.setLayout(self.vlayout1)
        # 添加分隔
        self.wlayout.addWidget(splitter2)
        # 窗口设置布局
        self.setLayout(self.wlayout)
        
    
        
    def show_text(self):
        """textEdit控件显示文本"""
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Tool()
    sys.exit(app.exec_())