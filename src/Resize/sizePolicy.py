from PyQt5.QtWidgets import QSizePolicy


def resize(control):
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    control.setSizePolicy(sizePolicy)
    sizePolicy.setHeightForWidth(control.sizePolicy().hasHeightForWidth())
