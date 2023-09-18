def get_info(cur, Class: str = None, misson=1):
    if misson == 1:
        # 获取状态正常
        sql = f"""
SELECT `name`, `class`, `ID`, `teacher`, `year`, subquery.cnt
FROM `info`
JOIN (
  SELECT `teacher` AS sub_teacher, COUNT(1) AS cnt
  FROM `info`
  WHERE `year` = '{Class}' AND `status` = 1
  GROUP BY `teacher`
) AS subquery
ON `info`.`teacher` = subquery.sub_teacher
WHERE `info`.`year` = '{Class}' AND `info`.`status` = 1
ORDER BY subquery.cnt DESC, `class` ASC, `name` DESC;
"""
    elif misson == 2:
        sql = f"""
SELECT `name`, `class`, `ID`, `teacher`, `year`, subquery.cnt
FROM `info`
JOIN (
  SELECT `teacher` AS sub_teacher, COUNT(1) AS cnt
  FROM `info`
  WHERE `year` in {Class} AND `status` = 1
  GROUP BY `teacher`
) AS subquery
ON `info`.`teacher` = subquery.sub_teacher
WHERE `info`.`year` in {Class} AND `info`.`status` = 1
ORDER BY subquery.cnt DESC,`name` ASC, `class` DESC;
"""
    else:
        sql = f"SELECT  DISTINCT `year` FROM `info` ORDER BY `year`;"

    # print(sql)
    # 从数据库中查询信息
    cursor = cur.execute(sql)

    data = cursor.fetchall()

    if len(data) == 0:
        return []
    if len(data[0]) == 1:
        list_rows = [i[0] for i in data]
    else:
        list_rows = [list(i) for i in data]
    return list_rows
