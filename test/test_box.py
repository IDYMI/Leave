from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from lib.comboWidget.MyMultiComboWidget import MyMultiComboWidget as MyMultiComboWidget
from lib.db.Cur import get_cur as get_cur, end_conn as end_conn
from lib.db.Select import get_info as get_info


class MultiComboBox(QWidget):

    def __init__(self, options):
        super().__init__()

        self.main(options)

    def main(self, options):
        # 初始化下拉多选框
        self.cb = MyMultiComboWidget(options=options)

        # 布局
        layout = QVBoxLayout(self)
        layout.addWidget(self.cb)


if __name__ == '__main__':
    app = QApplication([])

    font = QFont('Microsoft YaHei', 12)
    app.setFont(font)

    conn, cur = get_cur()

    options = get_info(cur, misson=3)

    w = MultiComboBox(options)
    w.show()

    end_conn(conn)
    app.exec_()
