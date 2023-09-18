from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor  # 设置字体颜色

from lib.db.Select import get_info as get_info


def add_text(paragraph, text, Size, Bold=False, C_font='宋体', Color=RGBColor(0, 0, 0), alignment='LEFT'):
    Text = paragraph.add_run(text)
    if alignment == 'LEFT':
        paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT  # 左对齐
    elif alignment == 'RIGHT':
        paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT  # 右对齐
    elif alignment == 'CENTER':
        paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER  # 居中对齐
    elif alignment == 'JUSTIFY':
        paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY  # 两端对齐

    Text.font.size = Pt(Size)  # 字体大小
    Text.bold = Bold  # 字体是否加粗
    Text.font.name = '微软雅黑'  # 控制是英语时的字体
    Text.element.rPr.rFonts.set(qn('w:eastAsia'), C_font)  # 控制是中文时的字体
    Text.font.color.rgb = Color  # 设置颜色为黑色


def add_info(cur, document, data, misson=1):

    if misson == 1:

        # 新建一个不带表头的表格
        table = document.add_table(rows=0, cols=4, style='Table Grid')

        # 设置表格对齐方式为居中
        table.alignment = WD_TABLE_ALIGNMENT.CENTER

        titles = ["姓名", "班级", "学号", "导员"]
        # 添加表头
        cells = table.add_row().cells
        for i in range(4):
            cells[i].text = str(titles[i])
            set_cell_font(cells[i])
        # 设置当前行的行高为 15 磅（约等于 1.5 倍默认字体大小）
        row_height = Pt(15)
        for cell in cells:
            cell.height = row_height

        # 向表格中插入数据
        for row in data:
            cells = table.add_row().cells
            for i in range(4):
                cells[i].text = str(row[i])
                set_cell_font(cells[i])
            # 设置当前行的行高为 15 磅（约等于 1.5 倍默认字体大小）
            row_height = Pt(15)
            for cell in cells:
                cell.height = row_height
    else:
        return data


# 设置字体样式
def set_cell_font(cell):
    cell.paragraphs[0].runs[0].font.name = '微软雅黑'
    cell.paragraphs[0].runs[0]._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    cell.paragraphs[0].runs[0].font.size = Pt(11)
    cell.paragraphs[0].alignment = WD_TABLE_ALIGNMENT.CENTER  # 字相对于单元格居中
