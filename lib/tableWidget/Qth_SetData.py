# --coding: utf-8 --
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from loguru import logger


class SetData(QThread):
    _sum = pyqtSignal(str)  # 信号类型 str

    def __init__(self, df=None, columnlist=None, tableWidget=None):
        """
        表格更新结果
        :param df: pandas 数据
        :param columnlist: 预设元素
        :param tableWiget: 表格对象

        """
        super().__init__()
        self.df = df
        self.columnlist = columnlist
        self.tableWidget = tableWidget

    def run(self):
        # 发送结果
        try:
            self.tableWidget.QTable_addrowitems(self.df, self.columnlist)
            status = 1
        except Exception as e:
            status = str(e)
            logger.error(f'SetData error: {status}')
        self._sum.emit(str(status))
        # 关闭线程
        self.exit(0)

    def get_df(self):
        return self.df
