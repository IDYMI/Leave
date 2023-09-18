import io

from PyQt5.QtCore import QFile, QIODevice


# 读取Qss模板
class CommonHelper:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        try:
            file = QFile(style)
            if file.open(QIODevice.ReadOnly):
                f = io.BytesIO(file.readAll().data())
                return str(f.read(), encoding='utf-8')
        except Exception as e:
            print(str(e))
