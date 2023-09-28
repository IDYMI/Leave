from pprint import pprint


def list_split(items, minn, maxx):
    splited_items = []  # 分页过后的结果

    index = 0  # 现在遍历到哪个同学
    # TODO 优先同导员一张表格，如果同导员人数过少小于 minn 则添加到上个导员，并且最多不超过 maxx
    for i in range(0, len(items), maxx):
        i = index if index >= i else i
        if i >= len(items):
            continue
        name, Class, ID, teacher, year, cnt_teacher = items[i]

        index = i  # 当前编号

        # 无前一页 或者 有前一页且满
        if (not len(splited_items)) or (len(splited_items) and len(splited_items[-1]) >= maxx) or index <= len(items):
            # 插入一页
            splited_items.append([])

        flag = 1  # 少的忽略直接添加最多添加一次
        while index + cnt_teacher <= len(items):
            # 如果小于 minn, 且能添加
            if cnt_teacher < minn and flag:
                splited_items[-1] += items[index: index + cnt_teacher]
                index += cnt_teacher
                if index < len(items):
                    cnt_teacher = items[index][5]
                if len(splited_items[-1]) + cnt_teacher > maxx:
                    flag = 0
            # 超过 maxx， 且能添加
            elif cnt_teacher > maxx:
                cnt = 0
                while cnt < cnt_teacher // maxx:
                    if len(splited_items[-1]) != 0:
                        splited_items.append(items[index: index + maxx])
                    else:
                        splited_items[-1] += (items[index: index + maxx])
                    index += maxx
                    cnt += 1
                if cnt_teacher % maxx > 0:
                    splited_items.append(
                        items[index: index + cnt_teacher % maxx])
                    index += cnt_teacher % maxx
                    if index < len(items):
                        cnt_teacher = items[index][5]
            # 不大于 maxx， 当前页能添加完
            elif len(splited_items[-1]) + cnt_teacher <= maxx:
                splited_items[-1] += items[index: index + cnt_teacher]
                index += cnt_teacher
                if index < len(items):
                    cnt_teacher = items[index][5]
                # if len(splited_items[-1]) == maxx:
                #     splited_items.append([])
            # 大于 maxx， 当前页不能添加完
            elif len(splited_items[-1]) + cnt_teacher > maxx:
                remain = maxx - len(splited_items[-1])
                splited_items[-1] += items[index: index + remain]
                splited_items.append(
                    items[index + remain: index + cnt_teacher + 1])
                index += cnt_teacher
                if index < len(items):
                    cnt_teacher = items[index][5]
            else:
                break
    pprint(splited_items)
    return splited_items


l = [
    ['范梦园', '21软工智能4班', '2115925629', '李洋', '21', 5],
    ['姜晨棋', '21计科2班', '2115915068', '李洋', '21', 5],
    ['温健聪', '21计科2班', '2115915061', '李洋', '21', 5],
    ['吕龙', '21计科1班', '2115915053', '李洋', '21', 5],
    ['马兵德', '21计科1班', '2115915025', '李洋', '21', 5],
    ['邱鑫洋', '21软工智能2班', '2115925659', '胡晓杰', '21', 3],
    ['杜亦鸣', '21软工智能1班', '2115925683', '胡晓杰', '21', 3],
    ['朱佳鑫', '21软件5班', '2115925232', '胡晓杰', '21', 3],
    ['董丁琳', '21统计', '2110225015', '谭萌', '21', 3],
    ['郭欣睿', '21经数班', '2110115037', '谭萌', '21', 3],
    ['郭欣睿2', '21经数班', '2110115037', '谭萌', '21', 3],
    ['童桂鑫', '21大数据3班', '2115905097', '杨琰', '21', 3],
    ['童桂鑫2', '21大数据3班', '2115905097', '杨琰', '21', 3],
    ['童桂鑫3', '21大数据3班', '2115905097', '杨琰', '21', 3],
    ['谢明丽', '22软工', '2215925204', '张媛', '22', 12],
    ['李灿辉', '22计科', '2215915049', '张媛', '22', 12],
    ['张泽楷', '22计科', '2215915001', '张媛', '22', 12],
    ['简肇煜', '22计科', '2215915002', '张媛', '22', 12],
    ['杨纪存', '22计科', '2215915021', '张媛', '22', 12],
    ['王子源', '22计科', '2215915014', '张媛', '22', 12],
    ['孟令婷', '22计科', '2215915041', '张媛', '22', 12],
    ['张泽楷', '22计科', '2215915001', '张媛', '22', 12],
    ['简肇煜', '22计科', '2215915002', '张媛', '22', 12],
    ['杨纪存', '22计科', '2215915021', '张媛', '22', 12],
    ['王子源', '22计科', '2215915014', '张媛', '22', 12],
    ['孟令婷', '22计科', '2215915041', '张媛', '22', 12],
    ['徐萌', '22软工智能5班', '2215925732', '黎翀豪', '22', 5],
    ['陈诗曼', '22软工智能5班', '2215925716', '黎翀豪', '22', 5],
    ['王衡', '22软工智能5班', '2215925721', '黎翀豪', '22', 5],
    ['张霖', '22软工智能2班', '2215925563', '黎翀豪', '22', 5],
    ['尚同铮', '22软工智能2班', '2215925561', '黎翀豪', '22', 5],
    ['陈双', '22软工云计算', '2215925452', '胡晨曼', '22', 1]
]

ls = list_split(l, 5, 10)
