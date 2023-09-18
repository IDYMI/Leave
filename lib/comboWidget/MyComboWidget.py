# --coding: utf-8 --
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QComboBox, QLineEdit, QMessageBox


class MyLineEdit(QLineEdit):
    def __init__(self, Box):
        super(MyLineEdit, self).__init__()
        self.Box = Box

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        # TODO 双击鼠标事件显示下拉框
        self.Box.showPopup()


class MyComboBox(QComboBox):
    def __init__(self, title=None, options=None, ui=None, session: bool = True):
        super(MyComboBox, self).__init__()

        self.ui = ui
        self.options = options

        # 设置 Tip
        self.setToolTip(title)

        # 创建一个QLineEdit控件
        self.line_edit = MyLineEdit(self)
        # 设置提示文本
        self.line_edit.setPlaceholderText(title)
        # 禁用自带菜单
        self.setContextMenuPolicy(Qt.NoContextMenu)
        # 设置不可输入 ( 防止改变下拉选项 )
        # self.line_edit.setEnabled(False)

        # 设置QComboBox的LineEdit控件
        self.setLineEdit(self.line_edit)

        # self.Box_AddItems(options)

        # self.line_edit.setText(' ')
        if session:
            self.currentIndexChanged.connect(self.text_change)

    def text_change(self):
        text = self.line_edit.text()
        # print(f"#{text}#")
        if text in self.options:
            self.Set_Text(text)
        else:
            self.MessageBox("""请输入有效数据点""")
            self.removeItem(len(self.options))
            self.Set_Text('')

    def MessageBox(self, text):
        QMessageBox.critical(self.ui or self, "添加数据点失败", text,
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        self.line_edit.clear()

    def Box_AddItems(self, options):
        self.addItems(options)
        # 设置初始值为无
        self.setCurrentIndex(-1)

    def Set_Text(self, text):
        self.line_edit.setText(text)
