# --coding: utf-8 --
import os
import subprocess

images = os.listdir('../logo')
qss = os.listdir('./')
f = open('Logo_Qss.qrc', 'w+', encoding='utf-8')
f.write(u'<!DOCTYPE RCC>\n<RCC version="1.0">\n<qresource>\n')

for item in images:
    f.write(u'<file alias="logo/' + item + '">../logo/' + item + '</file>\n')

for item in qss:
    # print(item.rsplit('.'))
    try:
        back = item.rsplit('.')[1]
        if back != 'py' and back != 'qrc':
            f.write(u'<file alias="qss/' + item + '">' + item + '</file>\n')
            # print(item.rsplit('.')[1])
    except:
        continue

f.write(u'</qresource>\n</RCC>')
f.close()

pipe = subprocess.Popen(r'pyrcc5 -o Logo_Qss_rc.py Logo_Qss.qrc', stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                        stderr=subprocess.PIPE, creationflags=0x08)
