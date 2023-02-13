import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QFrame, QSplitter,
                             QHBoxLayout, QVBoxLayout, QApplication, QRadioButton, QMainWindow, QAction)
from PyQt5.QtGui import QIcon,QTextCursor
# from PyQt5.QtCore import Qt,QObject
from PyQt5 import QtCore
import json
import sip


class Tool(QMainWindow):

    def __init__(self):
        # 调用父类构造函数
        super().__init__()
        # 中心窗口
        self.widget = QWidget()  # 实例化中心窗口
        self.setCentralWidget(self.widget)  # 设置中心窗口
        # 菜单
        self.menubar = self.menuBar()  # 实例化菜单栏对象
        self.file_menu = self.menubar.addMenu('File')  # 添加文件菜单
        self.tip_act = QAction('啥都没有', self)  # 实例化菜单选项
        self.file_menu.addAction(self.tip_act)  # 添加选项到菜单栏
        # 计数器
        self.counter = 0
        self.local_var = locals()  # 动态控制变量
        # 全局layout
        self.wlayout = QVBoxLayout()
        # 局部layout
        self.hlayout1 = QHBoxLayout()  # android
        self.hlayout2 = QHBoxLayout()  # verion
        self.hlayout3 = QHBoxLayout()  # description
        self.hlayout4 = QHBoxLayout()  # header
        self.hlayout5 = QHBoxLayout()  # title
        self.hlayout6 = QHBoxLayout()  # force
        self.hlayout7 = QHBoxLayout()  # button start
        self.hlayout8 = QHBoxLayout()  # bottom Frame布局
        self.vlayout1 = QVBoxLayout()  # 左侧控件盒子
        self.vlayout2 = QVBoxLayout()  # description add clear按钮盒子
        self.vlayout3 = QVBoxLayout()  # description lineEdit控件布局
        self.widget.setLayout(self.wlayout)  # 添加全局layout到中心窗口
        # 动态控件layout
        self.box_layout = QVBoxLayout()
        # 设置控件
        self.lable_android = QLabel(self)
        self.lable_version = QLabel(self)
        self.lable_desription = QLabel(self)
        self.lable_header = QLabel(self)
        self.lable_title = QLabel(self)
        self.lable_force = QLabel(self)
        # textEdit
        self.text_edit = QTextEdit()  # 显示结果json
        self.text_stream = QTextEdit()  # 显示控制台输出
        self.text_stream.setReadOnly(True)  
        # button_add
        self.button_add = QPushButton("add")
        # button_start
        self.button_start = QPushButton("start")
        # button_clear
        self.button_clear = QPushButton("clear")
        # lineEdit
        self.line_android = QLineEdit()
        self.line_version = QLineEdit()
        self.line_desription = QLineEdit()
        self.line_header = QLineEdit()
        self.line_title = QLineEdit()
        # radio
        self.force_radio_t = QRadioButton("true")
        # 设置force_radio_t为默认选中
        self.force_radio_t.setChecked(True)
        self.force_radio_f = QRadioButton("false")
        # 文本显示
        self.text = QTextEdit()
        # 控件
        self.set_control()
        # 设置布局
        self.set_layout()
        # 调同时间监听
        self.set_event()
        # 将控制台输出重定向到textEdit中
        self.stream_out()

        # resize与move方法的整合方法，窗口大小与鼠标放大缩小/移动
        self.setGeometry(300, 300, 1000, 500)
        self.setWindowTitle("Tool")
        # 设置窗口图标
        self.setWindowIcon(QIcon("./tool.jpg"))
        # 显示窗口
        self.show()

    def set_event(self):
        # button监听事件，信号插槽
        self.button_start.clicked.connect(self.show_text)  # 点击开始
        self.button_add.clicked.connect(self.add_widget)  # 动态添加控件
        self.button_clear.clicked.connect(self.clear_widget)  # clear按钮绑定事件

    def set_control(self):
        """设置窗口控件属性"""
        # lable
        self.lable_android.setText("android")
        self.lable_version.setText("version")
        self.lable_desription.setText("desription")
        self.lable_header.setText("header")
        self.lable_title.setText("title")
        self.lable_force.setText("force")
        # 设置label控件大小
        self.lable_android.setFixedSize(70, 20)
        self.lable_version.setFixedSize(70, 20)
        self.lable_desription.setFixedSize(70, 20)
        self.lable_header.setFixedSize(70, 20)
        self.lable_title.setFixedSize(70, 20)
        self.lable_force.setFixedSize(70, 20)

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
        splitter1 = QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(self.text_edit)
        splitter1.setSizes([200, 100])  # 设置两边frame比例大小

        splitter2 = QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        splitter2.setSizes([400, 100])

        # 添加控件
        # android
        self.hlayout1.addWidget(self.lable_android)
        self.hlayout1.addWidget(self.line_android)
        # version
        self.hlayout2.addWidget(self.lable_version)
        self.hlayout2.addWidget(self.line_version)
        # desription
        self.hlayout3.addWidget(self.lable_desription)
        self.hlayout3.addLayout(self.vlayout3)
        self.vlayout3.addWidget(self.line_desription)
        # header
        self.hlayout4.addWidget(self.lable_header)
        self.hlayout4.addWidget(self.line_header)
        # title
        self.hlayout5.addWidget(self.lable_title)
        self.hlayout5.addWidget(self.line_title)
        # force
        self.hlayout6.addWidget(self.lable_force)
        self.hlayout6.addWidget(self.force_radio_t)
        self.hlayout6.addWidget(self.force_radio_f)
        # button_start
        self.hlayout7.addWidget(self.button_start)
        # button_add
        self.hlayout3.addLayout(self.vlayout2)
        self.vlayout2.addWidget(self.button_add)
        self.vlayout2.addWidget(self.button_clear)

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
        # 添加控制台输出到bottom Frame
        self.hlayout8.addWidget(self.text_stream)
        bottom.setLayout(self.hlayout8)
        # 添加分隔
        self.wlayout.addWidget(splitter2)
        # # 窗口设置布局
        # self.setLayout(self.wlayout)

    def description_decide(self) -> list:
        """循环筛选变量名,return一个list"""
        text_list = []
        for k, v in self.local_var.items():
            if k.startswith("line_description"):
                try:
                    text_list.append(v.text())
                except RuntimeError as e:
                    print("ERROR:{e}")
        return text_list

    def add_widget(self):
        """添加控件"""
        self.counter = self.counter + 1
        self.local_var[f"line_description_{self.counter}"] = QLineEdit()
        self.vlayout3.addWidget(self.local_var[f"line_description_{self.counter}"])
        print("add success")

    def clear_widget(self):
        """清除控件"""
        if self.counter != 0:
            for i in range(self.counter):
                self.vlayout3.removeWidget(self.local_var[f"line_description_{i + 1}"])
                sip.delete(self.local_var[f"line_description_{i + 1}"])
                self.counter = 0
            print("clear success")        

    def radio_check(self):
        if self.force_radio_t.isChecked():
            return True
        return False

    def show_text(self):
        """textEdit控件显示文本"""
        description = self.description_decide()
        description.insert(0, self.line_desription.text())

        res = {
            "android": f"{self.line_android.text()}",
            "version": f"{self.line_version.text()}",
            "description": description,
            "header": f"{self.line_header.text()}",
            "title": f"{self.line_title.text()}",
            "force": self.radio_check()
        }
        # setPlainText()方法显示文本
        self.text_edit.setPlainText(json.dumps(
            res,
            indent=4,
            ensure_ascii=False))
    def stream_out(self):
        """将输出重定向到textEdit中"""
        sys.stdout = EmittingStream(textWritten=self.outputWritten)  
        sys.stderr = EmittingStream(textWritten=self.outputWritten)
    
    def outputWritten(self, text):  
        """接收str的信号槽"""
        cursor = self.text_stream.textCursor()  
        cursor.movePosition(QTextCursor.End)  
        cursor.insertText(text)  
        self.text_stream.setTextCursor(cursor)  
        self.text_stream.ensureCursorVisible()  

class EmittingStream(QtCore.QObject):  
    """发送信号"""
    textWritten = QtCore.pyqtSignal(str)  #定义一个发送str的信号
    def write(self, text):
        self.textWritten.emit(str(text))  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Tool()
    sys.exit(app.exec_())
