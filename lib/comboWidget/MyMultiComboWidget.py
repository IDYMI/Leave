import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QComboBox, QLineEdit, QListWidget, QCheckBox, QListWidgetItem, QMessageBox

from lib.db.Cur import get_cur as get_cur, end_conn as end_conn
from lib.db.Select import get_info as get_info
from lib.tableWidget.Qth_SetData import SetData as SetData


class MyLineEdit(QLineEdit):
    def __init__(self, Box):
        super(MyLineEdit, self).__init__()
        self.Box = Box

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        # TODO 双击鼠标事件显示下拉框
        self.Box.showPopup()


class MyMultiComboWidget(QComboBox):
    def __init__(self, title=None, options=None, ui=None):  # options==[str,str...]
        super(MyMultiComboWidget, self).__init__()

        self.ui = ui

        self.title = ['姓名', '班级', '学号', '导员', '年级']

        self.selectedrow_num = 0
        self.qCheckBox = []

        # 自定义双击下拉框
        self.qLineEdit = MyLineEdit(self)
        self.qLineEdit.setReadOnly(True)
        self.qListWidget = QListWidget()

        self.setModel(self.qListWidget.model())
        self.setView(self.qListWidget)

        # 设置提示文本
        self.qLineEdit.setPlaceholderText(title)
        # 禁用自带菜单
        self.setContextMenuPolicy(Qt.NoContextMenu)

        self.setLineEdit(self.qLineEdit)

    def add_items(self, options, checks):
        self.options = options
        self.options.insert(0, '全部')

        self.row_num = len(self.options)

        # 全选
        self.addQCheckBox(0)
        self.qCheckBox[0].stateChanged.connect(self.All)

        # 单个选择
        for i in range(1, self.row_num):
            self.addQCheckBox(i)
            self.qCheckBox[i].stateChanged.connect(self.show)

        if len(options) == len(checks):
            # 默认全部选中
            self.qCheckBox[0].setChecked(True)
        else:
            for check in checks:
                if check in self.options:
                    index = self.options.index(check)
                    self.qCheckBox[index].setChecked(True)

    def addQCheckBox(self, i):
        self.qCheckBox.append(QCheckBox())
        qItem = QListWidgetItem(self.qListWidget)
        self.qCheckBox[i].setText(self.options[i])
        self.qListWidget.setItemWidget(qItem, self.qCheckBox[i])

    def getCheckItems(self):
        checkedItems = []
        for i in range(1, self.row_num):
            if self.qCheckBox[i].isChecked() == True:
                checkedItems.append(self.qCheckBox[i].text())
        self.selectedrow_num = len(checkedItems)
        return checkedItems

    def show(self):
        Outputlist = self.getCheckItems()
        self.qLineEdit.setReadOnly(False)
        self.qLineEdit.clear()

        show = ','.join(Outputlist) if Outputlist else '选择届别'

        if self.selectedrow_num == 0:
            self.qCheckBox[0].setCheckState(0)
        elif self.selectedrow_num == self.row_num - 1:
            self.qCheckBox[0].setCheckState(2)
        else:
            self.qCheckBox[0].setCheckState(1)

        self.qLineEdit.setText(show)
        self.qLineEdit.setReadOnly(True)

        # self.get_df(Outputlist)

        # 创建一个线程
        self.col = SetData(self.get_df(Outputlist), self.title, self.ui.tableWidget)
        # 线程发过来的信号挂接到槽函数 Qth_update_table
        self.col._sum.connect(self.Qth_update_table)
        # 线程启动
        self.col.start()

    def get_df(self, Outputlist):
        # 选择年级列表转化为字符串
        Class = str(tuple(Outputlist)).replace(",)", ")")

        conn, cur = get_cur()
        options = get_info(cur, Class=Class, misson=2)

        end_conn(conn)

        df = pd.DataFrame(options)

        return df

    def Qth_update_table(self, i):
        if i != '1':
            QMessageBox.critical(self, "修改文档失败", """神秘原因""",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def All(self, state):
        if state == 2:
            for i in range(1, self.row_num):
                self.qCheckBox[i].setChecked(True)
        elif state == 1:
            if self.selectedrow_num == 0:
                self.qCheckBox[0].setCheckState(2)
        elif state == 0:
            self.clear()

    def clear(self):
        for i in range(self.row_num):
            self.qCheckBox[i].setChecked(False)
