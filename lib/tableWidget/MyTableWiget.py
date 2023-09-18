# --coding: utf-8 --
from functools import partial

from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QScrollBar, QHeaderView, QMessageBox
from loguru import logger

from src.Resize.sizePolicy import resize as Resize


class NumericItem(QTableWidgetItem):
    def __lt__(self, other):
        try:
            return (self.data(Qt.UserRole) <
                    other.data(Qt.UserRole))
        except:
            logger.info(f"Data error : can not compare")
            return True


# 自定义的QTableWidget,使用ToolTip提示用户当前单元格内的详细内容
class MyTableWidget(QTableWidget):
    # Select_ColSignal = pyqtSignal(int)

    def __init__(self, MainWindow=None):
        super(MyTableWidget, self).__init__()

        self.MainWindow = MainWindow

        self.ini_table()

    def ini_table(self):
        """---------初始化表格的常用选项(按需修改)------------"""
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

        # 设置tablewidget禁止编辑
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置tablewidget不可选中
        # self.setSelectionMode(QAbstractItemView.NoSelection)
        # 设置隔行变色方法
        self.setAlternatingRowColors(True)
        # 表格中不显示分割线
        self.setShowGrid(False)
        # 自动换行
        self.setWordWrap(True)

        # 隐藏列的序号
        self.verticalHeader().setVisible(False)

        # 设置选择整行
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 自动拓展最后一行适应表格高度
        self.verticalHeader().stretchLastSection()

        self.btn_width = int(self.width() / 5)
        self.btn_height = int(self.height() / 10)

        # 设置自适应宽度
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 最小行高
        self.verticalHeader().setDefaultSectionSize(self.btn_height)

        # 设置大小策略
        Resize(self)

        self.setStyleSheet("QTableView{border: none;}")

        """------------关键代码--------------"""
        self.vertical_scrollbar = QScrollBar()
        self.horizon_scrollbar = QScrollBar()
        self.vertical_scrollbar.valueChanged.connect(partial(self.scollbar_change_slot, "vertical"))
        self.horizon_scrollbar.valueChanged.connect(partial(self.scollbar_change_slot, "horizon"))
        self.setVerticalScrollBar(self.vertical_scrollbar)
        self.setHorizontalScrollBar(self.horizon_scrollbar)
        self.init_row = 0
        self.init_col = 0
        # self.title_row_height = 0

        # 元素弹窗显示
        # self.tool_tip = ""
        # self.update_table_tooltip_signal.connect(self.update_table_tooltip_slot)
        # self.install_eventFilter()

    # 设置表格列标题
    def set_horizon_title(self, title_list):
        self.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.horizontalHeader().setVisible(True)

        for col, item in enumerate(title_list):
            item = QTableWidgetItem(str(item))
            # 默认列标题的宽和高
            item.setSizeHint(QSize(self.btn_width, self.btn_height))
            # 元素居中显示
            item.setTextAlignment(Qt.AlignCenter)
            self.setHorizontalHeaderItem(col, item)

        # # (关键值)这里的值设置为列标题高
        # self.title_row_height = self.tableWidget_size.height()

    # 为TableWidget安装事件过滤器
    def install_eventFilter(self):
        self.installEventFilter(self)
        self.setMouseTracking(True)

    # 改变滚动条时重置当前页面的初始行和列
    def scollbar_change_slot(self, type):
        if type == "vertical":
            value = self.verticalScrollBar().value()
            self.init_row = value
            # print("垂直滚动条当前的值为:",value)
            # print("当前页面的起始行为:",self.init_row)
        else:
            value = self.horizontalScrollBar().value()
            self.init_col = value
            # print("水平滚动条当前的值为:",value)
            # print("当前页面的起始列为:",self.init_col)

    def QTable_clear(self):
        self.clear()
        # 不允许排序
        self.setSortingEnabled(False)
        # 清除所有行
        self.setRowCount(0)
        self.clearContents()

    def QTable_addrowitems(self, df, title):
        """

        :param df: pandas 排行榜数据
        :param title: 列标题
        :return:
        """

        # TODO 清除所有元素
        self.QTable_clear()

        # 设置行列数
        self.row_length, self.col_length = len(df), len(title)

        # 设置列数
        self.setColumnCount(self.col_length)
        # 设置行数
        self.setRowCount(self.row_length)

        # TODO 设置自定义标题

        if self.horizontalHeaderItem(0) is None:
            # 设置表头的列标签
            self.set_horizon_title(title)

        # TODO 添加元素
        for i in range(self.row_length):
            # if i < self.row_length:
            row = df.iloc[i].values.tolist()
            # logger.info(row)
            for index, value in enumerate(row):
                if value == None:
                    item_ac = QTableWidgetItem('')
                elif isinstance(value, str):
                    item_ac = QTableWidgetItem(value)
                else:
                    item_ac = NumericItem(str(value))
                    item_ac.setData(Qt.UserRole, int(value))
                # 元素居中显示
                item_ac.setTextAlignment(Qt.AlignCenter)
                # 插入元素
                self.setItem(i, index, item_ac)
                # 释放内存
                del item_ac

    def QTable_update(self, col, order=None):
        # 允许排序
        self.setSortingEnabled(True)
        if order:
            # 降序
            self.sortItems(col, Qt.AscendingOrder)
        else:
            # 升序
            self.sortItems(col, Qt.DescendingOrder)
        # 更新表单
        self.viewport().update()

    # # 通过计算坐标确定当前位置所属单元格
    # def update_table_tooltip_slot(self, posit):
    #     self.tool_tip = ""
    #     self.mouse_x = posit.x()
    #     self.mouse_y = posit.y()
    #     self.row_height = self.title_row_height  # 累计行高,初始值为列标题行高
    #     for r in range(self.rowCount()):
    #         current_row_height = self.rowHeight(r)
    #         self.col_width = 0  # 累计列宽
    #         if self.row_height <= self.mouse_y <= self.row_height + current_row_height:
    #             for c in range(self.columnCount()):
    #                 current_col_width = self.columnWidth(c)
    #                 if self.col_width <= self.mouse_x <= self.col_width + current_col_width:
    #                     r = self.init_row + r
    #                     c = self.init_col + c
    #                     # print("鼠标当前所在的行和列为:({},{})".format(r, c))
    #                     item = self.item(r, c)
    #                     if item != None:
    #                         self.tool_tip = item.text()
    #                     else:
    #                         self.tool_tip = ""
    #                     return self.tool_tip
    #                 else:
    #                     self.col_width = self.col_width + current_col_width
    #         else:
    #             if self.mouse_y < self.row_height:
    #                 break
    #             else:
    #                 self.row_height = self.row_height + current_row_height
    #
    # # 事件过滤器
    # def eventFilter(self, object, event):
    #     try:
    #         if event.type() == QEvent.ToolTip:
    #             self.setCursor(Qt.ArrowCursor)
    #             # print("当前鼠标位置为:", event.pos())
    #             self.update_table_tooltip_signal.emit(event.pos())
    #             # 设置提示气泡显示范围矩形框,当鼠标离开该区域则ToolTip消失
    #             rect = QRect(self.mouse_x, self.mouse_y, 30, 10)  # QRect(x,y,width,height)
    #             # 设置QSS样式
    #             self.setStyleSheet(
    #                 """QToolTip{border:10px;
    #                    border-top-left-radius:5px;
    #                    border-top-right-radius:5px;
    #                    border-bottom-left-radius:5px;
    #                    border-bottom-right-radius:5px;
    #                    background:#4F4F4F;
    #                    color:#00BFFF;
    #                    font-size:18px;
    #                    font-family:"微软雅黑";
    #                 }""")
    #             QApplication.processEvents()
    #             # 在指定位置展示ToolTip
    #             QToolTip.showText(QCursor.pos(), self.tool_tip, self, rect, 1500)
    #             """
    #             showText(QPoint, str, QWidget, QRect, int)
    #             #############参数详解###########
    #             # QPoint指定tooptip显示的绝对坐标,QCursor.pos()返回当前鼠标所在位置
    #             # str为设定的tooptip
    #             # QWidget为要展示tooltip的控件
    #             # QRect指定tooltip显示的矩形框范围,当鼠标移出该范围,tooltip隐藏,使用该参数必须指定Qwidget!
    #             # int用于指定tooltip显示的时长(毫秒)
    #             """
    #         return QWidget.eventFilter(self, object, event)
    #     except Exception as e:
    #         logger.error(f'Maketablewidget_error : {str(e)}')
