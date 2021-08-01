from win32com.client import Dispatch
from os import walk
import os
wdFormatPDF = 17


def doc2pdf(input_file):
    word = Dispatch('Word.Application')
    doc = word.Documents.Open(input_file)
    doc.SaveAs(input_file.replace(".docx", ".pdf"), FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()
def zhi(dizhi):
    doc_files = []
    pdf_file =[]
    directory = dizhi
    for root, dirs, filenames in walk(directory):
        for file in filenames:
            if file.endswith(".doc") or file.endswith(".docx"):
                # print(str(root + "\\" + file))
                # doc2pdf(r'D:\Study\pythonProject\remi_design\jisuan_shabu_canshu\来样分析表.docx')
                g= file.split('.')[0]+'.pdf'
                folder = os.path.exists(r'{}\{}'.format(dizhi,g))
                if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                    doc2pdf(str(root + "\\" + file))
                else:
                    pass




if __name__ == "__main__":
    # doc_files = []
    # directory = r"D:\Study\pythonProject\remi_design\jisuan_shabu_canshu\ceshi"
    # for root, dirs, filenames in walk(directory):
    #     for file in filenames:
    #         if file.endswith(".doc") or file.endswith(".docx"):
    #             #print(str(root + "\\" + file))
    #             #doc2pdf(r'D:\Study\pythonProject\remi_design\jisuan_shabu_canshu\来样分析表.docx')
    #             doc2pdf(str(root + "\\" + file))
    zhi(r'D:\Study\pythonProject\remi_design\jisuan_shabu_canshu\210726')
