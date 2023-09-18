from pprint import pprint


def list_split(items, minn, maxx):
    splited_items = []  # 分页过后的结果

    page_itmes = []  # 每页的结果

    index = 0
    # TODO 优先同导员一张表格，如果同导员人数过少则添加到上个导员，并且最多不超过 n
    for i in range(0, len(items), maxx):
        i = i if index <= i else index
        name, Class, ID, teacher, year, cnt_teacher = items[i]

        if cnt_teacher >= minn:  # 如果当前导员数足够多
            page_itmes = items[i:i + cnt_teacher]
            splited_items.append(page_itmes)
            index = i + cnt_teacher

            # 如果还有剩余
            if index < maxx and (index % maxx):
                page_itmes = items[i + cnt_teacher:i + maxx]
                if index % maxx > minn and index + items[index][5] <= maxx: # 如果当前页有剩余，且添加下一页的结果不超过最大值
                    splited_items.append(page_itmes)
                else:
                    splited_items[len(splited_items) - 1] += page_itmes
        else:
            if len(splited_items):
                index2 = i
                # 如果能加到前一页，一直加
                while len(splited_items[len(splited_items) - 1]) + len(items[index2: index2 + cnt_teacher]) <= maxx:
                    if index2 < len(items):
                        name, Class, ID, teacher, year, cnt_teacher = items[index2]
                        splited_items[len(splited_items) -
                                      1] += items[index2: index2 + cnt_teacher]
                        index2 += cnt_teacher
                    else:
                        break
                    
                # 如果还有剩余
                if len(items) - index2 > 1:
                    name, Class, ID, teacher, year, cnt_teacher = items[index2]
                    page_itmes = items[index2: index2 + maxx]
                    if cnt_teacher <= minn:  # 如果剩下的少于 minn
                        splited_items[len(splited_items) - 1] += page_itmes
                    else:
                        splited_items.append(
                            items[index2: index2 + cnt_teacher])
                    page_itmes = []
            else:  # 第一页
                page_itmes = items[i: i + maxx]
                splited_items.append(page_itmes)
                page_itmes = []
    pprint(splited_items)

    return splited_items


l = [
    # ['范梦园', '21软工智能4班', '2115925629', '李洋', '21', 5],
    # ['姜晨棋', '21计科2班', '2115915068', '李洋', '21', 5],
    # ['温健聪', '21计科2班', '2115915061', '李洋', '21', 5],
    # ['吕龙', '21计科1班', '2115915053', '李洋', '21', 5],
    # ['马兵德', '21计科1班', '2115915025', '李洋', '21', 5],
    # ['邱鑫洋', '21软工智能2班', '2115925659', '胡晓杰', '21', 3],
    # ['杜亦鸣', '21软工智能1班', '2115925683', '胡晓杰', '21', 3],
    # ['朱佳鑫', '21软件5班', '2115925232', '胡晓杰', '21', 3],
    # ['董丁琳', '21统计', '2110225015', '谭萌', '21', 3],
    # ['郭欣睿', '21经数班', '2110115037', '谭萌', '21', 3],
    # ['郭欣睿2', '21经数班', '2110115037', '谭萌', '21', 3],
    # ['童桂鑫', '21大数据3班', '2115905097', '杨琰', '21', 3],
    # ['童桂鑫2', '21大数据3班', '2115905097', '杨琰', '21', 3],
    # ['童桂鑫3', '21大数据3班', '2115905097', '杨琰', '21', 3],
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

ls = list_split(l, 5, 8)
