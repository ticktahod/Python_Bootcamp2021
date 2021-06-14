#pip install easyread
from easyread.translator import Translate #import easyread มีปัญหา
from openpyxl import Workbook
from datetime import datetime

article = open('article.txt','r',encoding='utf-8')
article = article.read()
article = article.split() #ใช้เเยกคำ

print('Count : ',len(article))
result = []

for word in article:
    res = Translate(word)
    if res != None: #เวลา search ทุกครั้งจะได้ผลลัพธ์เป็น None เลยต้องใส่เงื่อนไข
        result.append([word,res['meaning']]) #res['meaning'] คือ ปริ้นเฉพาะความหมาย
        #ตัวอย่าง result.append(['Cat','[N] แมว'])

excelfile = Workbook()
sheet = excelfile.active

header = ['Vocab','Translate']
sheet.append(header)

for rs in result:
    sheet.append(rs)

dt = datetime.now().strftime('%Y-%m-%d %H%M%S')
excelfile.save('Vocab - {}.xlsx'.format(dt))