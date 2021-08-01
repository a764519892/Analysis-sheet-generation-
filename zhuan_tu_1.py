import os
import fitz
from os import walk

def get_file(url):
    pdf_dir = []

    pdf_name_1 = []
    #docunames = os.listdir()

    directory = url

    for root, dirs, filenames in walk(directory):
        for file in filenames:
            if file.endswith(".pdf") :
                # print(str(root + "\\" + file))
                # doc2pdf(r'D:\Study\pythonProject\remi_design\jisuan_shabu_canshu\来样分析表.docx')
                g = file.split('.')[0] + '.png'
                folder = os.path.exists(r'{}\{}'.format(url, g))
                if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                    t = str(root + "\\" + file)
                    name = file.split('.')[0]
                    pdf_name_1.append(name)
                    pdf_dir.append(t)
                else:
                    pass



    conver_img(pdf_dir ,pdf_name_1 ,url)


def conver_img(pdf_dir ,pdf_name_1,url):
    for pdf in range(len(pdf_dir)):
        doc = fitz.open(pdf_dir[pdf])
        pdf_name = pdf_name_1[pdf]
        for pg in range(doc.pageCount):
            page = doc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
            zoom_x = 2.0
            zoom_y = 2.0
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)
            pm.writePNG(r'{}\{}.png'.format(url,pdf_name))

def run(file):
    get_file(file)
if __name__ == '__main__':
    get_file(r'D:\Study\pythonProject\remi_design\jisuan_shabu_canshu\210726')
