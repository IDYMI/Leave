import datetime


def get_Times(StartTime: str, Times: int = 1, Pause: int = 3):
    """
    :param StartTime: 开始时间
    :param Times: 连续几次
    :param Pause: 一次时长
    :return:
    """
    Lst = []
    Pause -= 1
    for i in range(Times):
        date = datetime.datetime.strptime(StartTime, '%m月%d日').date()

        # 计算后两天的日期
        two_days_later = date + datetime.timedelta(days=Pause)

        # 将日期格式化为 "X月X日" 的字符串
        EndTime = two_days_later.strftime('%m{m}%d{d}').format(m='月', d='日')

        Lst.append([StartTime, EndTime])

        StartTime = (datetime.datetime.strptime(EndTime, '%m月%d日').date() + datetime.timedelta(days=1)).strftime(
            '%m{m}%d{d}').format(m='月', d='日')

    return Lst
