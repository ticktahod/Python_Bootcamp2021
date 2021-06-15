"โปรเเกรมคำนวนราคาสินค้า รวมVAT7%"

from tkinter import *
#* ดึงความสามารถหลักมาทั้งหมด(เเค่ main)
from tkinter import ttk # ttk คือ theme ของ tk

GUI = Tk() #สร้างหน้าต่างหลัก
GUI.geometry('500x450') #กว้าง x สูง
GUI.title('โปรเเกรมคำนวณ VAT')

######## ----config------ ########
FONT = ('Angsana New',20)

"==============ช่องกรอกข้อมูล============="

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

######## Radio เลือกประเภท VAT ########
F1 = Frame()
F1.pack(pady=10)

v_radio = StringVar()

R1 = ttk.Radiobutton(F1,text='ราคารวม vat เเล้ว',variable=v_radio,value='ic') # ic คือรหัส
R1.grid(row=0,column=0)

R1.invoke() #ตั้งให้เลือกเป็นค่าเริ่มต้น กรณีไม่ได้เลือก

R2 = ttk.Radiobutton(F1,text='ราคา + vat 7%',variable=v_radio,value='av') # ic คือรหัส
R2.grid(row=0,column=1)

R3 = ttk.Radiobutton(F1,text='ราคาไม่รวม vat',variable=v_radio,value='nic') # ic คือรหัส
R3.grid(row=0,column=2)

"================= คำนวณ ================"

def caluculater(event=None):
    #print('RADIO :',v_radio.get())
    name = product_name.get() #.get คือให้เเสดงผลออกมา
    price = int(product_price.get())
    quantity = int(product_quantity.get())
    total = price * quantity
    if v_radio.get() == 'ic':
        vat7 = total * (7/107)
        net_total = total * (100/107) #ราคาก่อนภาษี
        print(name,"ราคาก่อนรวม VAT : {:.2f} (vat 7% : {:.2f})".format(net_total,vat7))
        result.set('สินค้า: {} จำนวน {} ชิ้น ทั้งหมด {} บาท ({} บาท/ชิ้น)\n ราคาสินค้า: {:.2f} VAT7% : {:.2f}'.format(name,
                                                                                                        quantity,
                                                                                                        total,
                                                                                                        price,
                                                                                                        net_total,
                                                                                                        vat7))
        #สั่งโชว์ใน GUI
    
    elif v_radio.get() == 'av':
        vat7 = (total * (7/100))
        net_total = total #ราคาไม่รวม vat
        sum_total = total + vat7
        result.set('สินค้า: {} จำนวน {} ชิ้น ทั้งหมด {:.2f} บาท ({:.2f} บาท/ชิ้น)\n ราคาสินค้า: {:.2f} VAT7% : {:.2f}'.format(name,
                                                                                                            quantity,
                                                                                                            sum_total,
                                                                                                            price + (vat7 / quantity),
                                                                                                            net_total,vat7))
    else:
        result.set('สินค้า: {} จำนวน {} ชิ้น ทั้งหมด {:.2f} บาท ({:.2f} บาท/ชิ้น)'.format(name,quantity,total,price))
                                                                                                        
                                                                                                            

######## ปุ่มกดเพื่อคำนวณ ######
B1 = ttk.Button(GUI,text = 'Calculate',command=caluculater)     #สร้างปุ่มขึ้นมาชื่อ Translate
B1.pack(ipadx=20,ipady=10,pady=10)  # show ปุ่มขึ้นมาวางจากบนลงล่าง

"กด Enter ผ่านช่อง E3 ได้เลย"
E3.bind('<Return>',caluculater)

###### Result #######
result = StringVar()
result.set('<<<ผลลัพธ์โชว์จุดนี้>>>')

R1 = ttk.Label(GUI,textvariable=result,font=FONT)
R1.pack()

GUI.mainloop() #ทำให้โปรเเกรมรันได้ตลอดเวลาจนกว่าจะปิด (เอาไว้บรรทัดสุดท้าย)
