with open('1.txt','r',encoding='utf-8') as f:
    neirong=f.read().split('\n')
    neirong.pop()
    print(neirong)
import time
localtime = time.localtime(time.time())
print(time.strftime("%Y%m%d", time.localtime()) )
ri_qi=str(time.strftime("%Y%m%d", time.localtime()))
bianma=2
deng_ji_hao =ri_qi[2:] +'-%s' %bianma
print(deng_ji_hao)
import os
docunames = os.listdir()
print(docunames)
from os import walk
directory = r"D:\Study\pythonProject\remi_design\jisuan_shabu_canshu\ceshi"
for root, dirs, filenames in walk(directory):
    print(filenames)
    for file in filenames:
        if file.endswith(".doc") or file.endswith(".docx"):
            print(str(root + "\\" + file))
            print(file)
            print(dirs)
docunames = os.listdir()
for docuname in docunames:
    if os.path.splitext(docuname)[1] == '.pdf':  # 目录下包含.pdf的文件
        #pdf_dir.append(docuname)
        print(docuname)
res_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res')
print(res_path)