from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QWidget, QCalendarWidget, QMessageBox

import bin as bin
from lib.comboWidget.MyComboWidget import MyComboBox as MyComboBox
from lib.comboWidget.MyMultiComboWidget import MyMultiComboWidget as MyMultiComboWidget
from lib.qss.Qss import CommonHelper as CommonHelper
from lib.tableWidget.MyTableWiget import MyTableWidget as MyTableWidget
from src.Resize.sizePolicy import resize as Resize


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()

    def Sizes(self):
        self.transparency = bin.transparency
        self.ui_width, self.ui_height = bin.ui_width, bin.ui_height
        self.user_screen_width, self.user_screen_height = bin.user_screen_width, bin.user_screen_height

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1800, 1034)

        # TODO 全局尺寸自适应
        self.Sizes()

        # 屏幕正中间出现窗口
        base_pos = QRect((self.user_screen_width - self.ui_width) // 2, (self.user_screen_height - self.ui_height) // 2,
                         self.ui_width, self.ui_height)
        MainWindow.setGeometry(base_pos)
        # 设置窗口图标
        MainWindow.setWindowIcon(QIcon(":/logo/NYIST.ico"))
        # 设置窗口透明度
        MainWindow.setWindowOpacity(self.transparency)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.ReasonBox = MyComboBox(title='请假理由', session=False)
        self.ReasonBox.setObjectName("ReasonBox")
        Resize(self.ReasonBox)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout")

        self.StartTimeLineEdit = QLineEdit(self.centralwidget)
        self.StartTimeLineEdit.setObjectName("StartTimeLineEdit")
        self.StartTimeLineEdit.setToolTip('点击选择开始日期')
        self.StartTimeLineEdit.setText('点击选择开始日期')
        # self.StartTimeLineEdit.mousePressEvent = self.show_calendar  # 绑定鼠标点击事件
        # self.StartTimeLineEdit.returnPressed.connect(self.hide_calendar)

        self.calendar = QCalendarWidget(self.centralwidget)
        self.calendar.setGridVisible(True)

        # self.calendar.show()

        self.verticalLayout_3.addWidget(self.StartTimeLineEdit)
        self.verticalLayout_3.addWidget(self.calendar)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)

        self.PauseLineEdit = MyComboBox(title='连续时长', ui=self)
        self.PauseLineEdit.setObjectName("PauseLineEdit")
        Resize(self.PauseLineEdit)

        self.TimesLineEdit = MyComboBox(title='连续次数', ui=self)
        self.TimesLineEdit.setObjectName("TimesLineEdit")
        Resize(self.TimesLineEdit)

        self.tableWidget = MyTableWidget(self)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.Class_Combox = MyMultiComboWidget(ui=self)
        self.Class_Combox.setObjectName("Class_Combox")
        Resize(self.Class_Combox)

        self.horizontalLayout.addWidget(self.ReasonBox)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.PauseLineEdit)
        self.horizontalLayout.addWidget(self.TimesLineEdit)
        self.horizontalLayout.addWidget(self.Class_Combox)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 1)

        self.Operation_QHLayout = QHBoxLayout()
        self.Operation_QHLayout.setObjectName("Operation_QHLayout")

        self.Save_Btn = QPushButton(self.centralwidget)
        self.Save_Btn.setObjectName("Save_Btn")
        Resize(self.Save_Btn)

        self.Make_Btn = QPushButton(self.centralwidget)
        self.Make_Btn.setObjectName("Make_Btn")
        Resize(self.Make_Btn)

        self.Operation_QHLayout.addWidget(self.Save_Btn)
        self.Operation_QHLayout.addWidget(self.Make_Btn)

        self.Operation_QHLayout.setStretch(0, 1)
        self.Operation_QHLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.Operation_QHLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        # qss
        self.Qss_Base()
        # 指向效果
        self.Click_Base()
        # Logo
        self.Logo_Base()

        self.retranslateUi(MainWindow)

    def Qss_Base(self):
        # 公共按键主题
        self.Qss_Add(self.Save_Btn, "QPushButton")
        self.Qss_Add(self.Make_Btn, "QPushButton")

        # 下拉框主题
        self.Qss_Add(self.ReasonBox, "QComboBox")
        self.Qss_Add(self.Class_Combox, "QComboBox")
        self.Qss_Add(self.PauseLineEdit, "QComboBox")
        self.Qss_Add(self.TimesLineEdit, "QComboBox")

    def Click_Base(self):
        self.setTextView(self.ReasonBox, '请假理由')
        self.setTextView(self.Class_Combox, '选择届别')
        self.setTextView(self.TimesLineEdit, '连续次数')
        self.setTextView(self.PauseLineEdit, '连续时长')
        self.setTextView(self.StartTimeLineEdit, '点击选择开始日期')

    def Logo_Base(self):
        pass

    def Qss_Add(self, items, name):
        Style = CommonHelper.readQss(f":/qss/{name}.qss")
        items.setStyleSheet(Style)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Save_Btn.setText(_translate("MainWindow", "保存模板"))
        self.Make_Btn.setText(_translate("MainWindow", "生成假条"))

    # def show_calendar(self, event):
    #     if event.button() == 1:  # 捕获左键单击事件
    #         self.calendar.show()
    #
    # def hide_calendar(self):
    #     self.calendar.hide()

    def setTextView(self, item, text):
        item.setToolTip(text)
        item.setPlaceholderText(text)

    def send_message(self, place):
        QMessageBox.about(self, "假条已保存", f"保存位置 ： {place}")

