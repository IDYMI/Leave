import sqlite3

import bin as bin


def get_cur():
    # 连接 SQLite3 数据库
    conn = sqlite3.connect(bin.db_path)
    cur = conn.cursor()

    return conn, cur


def end_conn(conn):
    # 关闭数据库连接
    conn.close()
