"""
โปรเเกรมคำนวนราคาสินค้า รวมVAT7%
"""
from tkinter import *
#* ดึงความสามารถหลักมาทั้งหมด(เเค่ main)
from tkinter import ttk # ttk คือ theme ของ tk

GUI = Tk() #สร้างหน้าต่างหลัก
GUI.geometry('500x400') #กว้าง x สูง
GUI.title('โปรเเกรมคำนวณ VAT')

######## ----config------ ########
FONT = ('Angsana New',20)

######## ชื่อสินค้า ########
L1 = ttk.Label(GUI,text='ชื่อสินค้า',font=FONT).pack() #ข้อความแสดง
product_name = StringVar() #กล่องเก็บข้อความ
E1 = ttk.Entry(GUI,textvariable = product_name,font=FONT,width=40) #หากมีการเขียนข้อความลงมาในช่องจะถูกเก็บไว้ที่ product_name
E1.pack()

######## ราคาสินค้า ########
L2 = ttk.Label(GUI,text='ราคาสินค้า',font=FONT).pack()
product_price = StringVar()
E2 = ttk.Entry(GUI,textvariable = product_price,font=FONT,width=40) 
E2.pack()

######## จำนวนสินค้า ########
L3 = ttk.Label(GUI,text='จำนวนสินค้า',font=FONT).pack()
product_quantity = StringVar()
E3 = ttk.Entry(GUI,textvariable = product_quantity,font=FONT,width=40) 
E3.pack()

######## คำนวณ #######
def caluculater(event=None):
    name = product_name.get() #.get คือให้เเสดงผลออกมา
    price = int(product_price.get())
    quantity = int(product_quantity.get())
    total = price * quantity

    vat7 = total * (7/107)
    net_total = total * (100/107) #ราคาก่อนภาษี
    print(name,"ราคาก่อนรวม VAT : {:.2f} (vat 7% : {:.2f})".format(net_total,vat7))
    result.set('สินค้า: {} {} ชิ้น ทั้งหมด {} บาท ({} บาท/ชิ้น)\n ราคาสินค้า: {:.2f} VAT7% : {:.2f}'.format(name,quantity,total,price,net_total,vat7))
    #สั่งโชว์ใน GUI

######## ปุ่มกดเพื่อคำนวณ ######
B1 = ttk.Button(GUI,text = 'Calculate',command=caluculater)     #สร้างปุ่มขึ้นมาชื่อ Translate
B1.pack(ipadx=20,ipady=10,pady=10)  # show ปุ่มขึ้นมาวางจากบนลงล่าง

"กด Enter ผ่านช่อง E3 ได้เลย"
E3.bind('<Return>',caluculater)

###### Result #######
result = StringVar()

R1 = ttk.Label(GUI,textvariable=result,font=FONT)
R1.pack()

GUI.mainloop() #ทำให้โปรเเกรมรันได้ตลอดเวลาจนกว่าจะปิด (เอาไว้บรรทัดสุดท้าย)
