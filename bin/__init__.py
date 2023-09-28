import os
import pathlib
import sys
import warnings
from configparser import ConfigParser

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QGuiApplication
from loguru import logger

warnings.filterwarnings("ignore", category=DeprecationWarning)

# TODO 目录
# 项目根文件名
START_DIR = str(os.path.dirname(os.path.realpath(sys.argv[0])))
# 工作目录
BASE_DIR = str(pathlib.PurePath(START_DIR))
"""START_DIR.parents[0] 向上一级"""

# 测试
# BASE_DIR = r'E:\Project\PythonPj\ACM_Leave'

config_path = str(pathlib.PurePath(BASE_DIR, "docs/config.ini"))
bug_path = str(pathlib.PurePath(BASE_DIR, "docs/bug.log"))
db_path = str(pathlib.PurePath(BASE_DIR, "docs/user.db"))
docs_path = str(pathlib.PurePath(BASE_DIR, "docs/docx"))

# TODO 等比列调整大小的参数

# TODO 预设屏幕大小
screen = QSize(2560, 1440)
screen_width, screen_height = screen.width(), screen.height()

# TODO 用户屏幕大小
app = QGuiApplication([])
user_screen = app.primaryScreen().size()
user_screen_width, user_screen_height = user_screen.width(), user_screen.height()

logger.info(f"user_screen_width : {user_screen_width}, user_screen_height : {user_screen_height}")

# 测试
# user_screen_width = 1920
# user_screen_height = 1080

# 用户与预设的比例差
scale_x = user_screen_width / screen_width
scale_y = user_screen_height / screen_height

scale = max(scale_x, scale_y)

logger.info(f"scale_x : {scale_x}, scale_y : {scale_y}")

# TODO 预设大小
# 初始主窗口大小
base_size = QSize(int(1500 * scale_x), int(1000 * scale_y))
ui_width, ui_height = base_size.width(), base_size.height()

tableWidget_size = QSize(int(1650 * scale), int(45 * scale))

# 透明度
transparency = 0.9


def conf_read():
    # 需要实例化一个ConfigParser对象
    conf = ConfigParser()
    # 读取config.ini
    conf.read(config_path, encoding='utf-8')
    return conf


def conf_save(Data: dir):
    # 创建 ConfigParser 对象
    config = ConfigParser()

    # 添加一些配置项
    config['Reason'] = {'reason': Data['Reason']}
    config['Pause'] = {'pause': Data['Pause']}
    config['Times'] = {'times': Data['Times']}
    config['Class'] = {'class': Data['Class']}

    # 将配置写入文件
    with open(config_path, 'w', encoding='utf-8') as configfile:
        config.write(configfile)


def create_path(path, name):
    if not os.path.exists(path):
        os.makedirs(path)
        logger.info(f'{name} : {path} Create Success')


# TODO 将日志输出到文件
logger.add(bug_path)
# TODO 将 print 的输出到文件中
# sys.stdout = sys.stderr = open(bug_path, 'a')

# TODO 工作路径日志
logger.info(f"BASE_DIR : {BASE_DIR}")

"""
制作目录或者文件
"""

# 制作 docs_path 目录
create_path(docs_path, 'docs_path')
