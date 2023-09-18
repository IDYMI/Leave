# --coding: utf-8 --
import sys

from PyQt5.QtCore import QTranslator, QLocale, QLibraryInfo
from PyQt5.QtWidgets import QApplication, QMainWindow
from loguru import logger

from lib.functions import function as function
from lib.qss import Logo_Qss_rc
from src.main import Leave_UI as ui

logger.info(f"LogoQss Link Success : {Logo_Qss_rc}")


class mywindow(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()

        # ui
        self.setupUi(self)
        # function
        self.function = function(self)


def get_translator():
    # TODO 全局系统控件切换中文
    translator = QTranslator()
    if len(sys.argv) > 1:
        locale = sys.argv[1]
    else:
        locale = QLocale.system().name()
    # print(locale)
    translator.load('qt_%s' % locale,
                    QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    return translator


if __name__ == '__main__':
    # Ui界面实例
    app = QApplication(sys.argv)
    # 切换语言，主要针对系统窗口如字体选择
    translator = get_translator()
    app.installTranslator(translator)
    # 窗口界面
    UI = mywindow()
    # # 关闭所有窗口,也不关闭应用程序
    # QApplication.setQuitOnLastWindowClosed(False)
    # 显示窗口
    UI.show()
    sys.exit(app.exec_())

# Pyinstaller   
"""
pyi-makespec -w main.py
pyinstaller main.spec
"""

# Git commit
"""
git init
git add .
git commit -m '1.3'
--amend 覆盖提交
git remote add '1.3' https://github.com/IDYMI/NYIST_Award.git
git push -u Award
"""
