# --coding: utf-8 --
"""
Author : DYM_
ProjectName : ACM_Award_Maker
"""

import pandas as pd
from loguru import logger


class Data():
    def __init__(self):

        self.columnlist = None
        self.df = pd.DataFrame()
        self.df_backup = pd.DataFrame()

    def get_df(self, filepath=None):
        try:
            if filepath:
                self.filepath = filepath.replace('\\', '/')

                # 显示所有行，把列显示设置成最大
                pd.set_option('display.max_rows', None)
                # 设置value的显示长度为200，默认为50
                pd.set_option('max_colwidth', 200)

                self.filename, suffix = self.filepath.split('.')

                # 转存文件位置
                self.paths = f"{self.filename}_backup.xlsx"

                # 根据文件类型使用pandas读入文件
                if suffix == 'xlsx' or suffix == 'xls':
                    self.df = pd.read_excel(self.filepath, keep_default_na=False)
                elif suffix == 'csv':
                    self.df = pd.read_csv(self.filepath, keep_default_na=False)
                else:
                    logger.error(f"FormRead error : Unsupported file type.")

                return self.df

            else:
                return self.df_backup

        except Exception as e:
            logger.error(f"Form error : {str(e)}")
            # 报错返回空列表
            return pd.DataFrame()

    def set_columnlist(self, columnlist):

        # columnlist 在数据表中有对应
        self.columnlist = [column for column in self.get_columns() if column in columnlist]

        # 需要的数据
        self.df_backup = self.df.loc[:, self.columnlist]

        # self.df_backup = self.df_backup.assign(状态=0)

    def get_columns(self):
        # 获取所有列名
        columns = self.df.columns.tolist()
        return columns

    def save(self):
        # 保存文件
        self.df_backup.to_excel(self.paths, index=False)

    def save_status(self, index, status):
        """
        设置图片状态
        :param index: 行数
        :param status: 结果
        :return:
        """
        # TODO 状态所在的列
        self.df_backup.loc[index, '状态'] = str(status)

# import bin as bin
#
# if __name__ == '__main__':
#     # TODO 文件位置
#     xlsx_path = f"{bin.BASE_DIR}/lib/data/决赛最终成绩.xlsx"
#
#     # TODO 需要的内容
#     list_usecols = ['排名', '', '状态']
#
#     data = Data()
#     data.get_df(xlsx_path)
#
#     data.set_columnlist(list_usecols)
#
#     data.get_df()
#
#     data.save_status(2, 1)
#
#     data.save_status(3, 1)
#     data.save_status(4, 1)
#
#     df = data.get_df()
#
#     for index, i in enumerate(list_usecols):
#         if i == '':
#             df.insert(loc=index, column='', value=['' for i in range(len(df))])
#
#     print(df[:3])
