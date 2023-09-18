import re


def replace_date_in_docx(text, selected_dates):
    # 定义正则表达式匹配 X月X日 格式日期的模式
    date_pattern = r"\d{1,2}月\d{1,2}日"
    # 在段落中查找符合日期格式的文本
    matches = re.findall(date_pattern, text)

    for idx, match in enumerate(matches):
        selected_date = selected_dates[idx]
        text = re.sub(match, selected_date, text)
    return text

