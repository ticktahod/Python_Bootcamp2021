from tkinter import *
#* ดึงความสามารถหลักมาทั้งหมด(เเค่ main)
from tkinter import ttk # ttk คือ theme ของ tk
##------Google Translator-------
from googletrans import Translator
translator = Translator() #สร้่าง function เเปลภาษาขึ้นมา

GUI = Tk() #สร้างหน้าต่างหลัก
GUI.geometry('500x300') #กว้าง x สูง
GUI.title('โปรเเกรมเเปลภาษา by Ticky')

#----config------
FONT = ('Angsana New',15)
#----Label-------
L = ttk.Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการเเปล',font=FONT)
L.pack()
#-----Entry(ช่องกรอกข้อความ)----
v_vocab = StringVar() #กล่องเก็บข้อความ

E1 = ttk.Entry(GUI,textvariable = v_vocab,font=FONT,width=40) #หากมีการเขียนข้อความลงมาในช่องจะถูกเก็บไว้ที่ v_vocab
E1.pack(pady=20)
#pad.. ใช้เพิ่มระยะห่างระหว่างปุ่มตามเเนว y
#textvariable ข้อความที่เปลี่ยนเเปลงได้ตลอด

#-----Button(ปุ่มแปล)-----
def Translate():
    vocab = v_vocab.get() #.get คือให้เเสดงผลออกมา
    meaning = translator.translate(vocab,dest = 'th')
    print(vocab + ' : ' + meaning.text)
    print(meaning.pronunciation)
    v_result.set(vocab + ' : ' + meaning.text) #สั่งโชว์ใน GUI

B1 = ttk.Button(GUI,text = 'Translate',command=Translate)#สร้างปุ่มขึ้นมาชื่อ Translate
B1.pack(ipadx=20,ipady=10) # show ปุ่มขึ้นมาวางจากบนลงล่าง
#ipadx/y internalpading เเนวเเกน x,y ใช้ขยายขนาดปุ่ม
#ipad.. ใช้เพิ่มขนาดภายในปุ่ม

#----Label-------
L = ttk.Label(GUI,text='คำแปล',font=FONT)
L.pack()

#----Result-------
v_result = StringVar() #กล่องสำหรับเก็บคำเเปล
FONT2 = ('Angsana New',20)
R1 = ttk.Label(GUI,textvariable=v_result,font = FONT2,foreground = 'green')
R1.pack()
GUI.mainloop() #ทำให้โปรเเกรมรันได้ตลอดเวลาจนกว่าจะปิด (เอาไว้บรรทัดสุดท้าย)
