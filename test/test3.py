import ast
import configparser

# 定义要保存的配置信息
config = {
    'Server': {'Host': 'localhost', 'Port': '8080'},
    'Database': {'Username': 'admin', 'Password': '123456'},
    'Options': {'Values': [1, 2, 3]}
}

# 创建 ConfigParser 对象
parser = configparser.ConfigParser()

# 将配置信息保存到 ConfigParser 对象中
for section in config:
    parser[section] = config[section]

# 将配置信息写入文件
with open('config.ini', 'w') as fp:
    parser.write(fp)

# 读取配置信息
parser = configparser.ConfigParser()
parser.read('config.ini')
values_str = parser.get('Options', 'Values')

# 将字符串转换为列表
values = ast.literal_eval(values_str)

# 输出配置信息
print(values)
