class Student:
    def __init__(self,name): # self เปรียบเสมือนใช้เเทนตัวมันเอง
        self.name = name
        self.exp = 0
        self.lesson = 0
        #Call Function
        #self.AddEXP(10)

    def Hello(self):
        print('สวัสดีจ้า ผมชื่อ {}'.format(self.name))

    def Coding(self):
        print('{} : กำลังเขียนโปรเเกรม....'.format(self.name))
        self.exp += 5
        self.lesson += 1
    
    def ShowEXP(self):
        print('{} มีประสบการณ์ {} EXP'.format(self.name,self.exp))
        print('- เรียนไป {} ครั้งเเล้ว '.format(self.lesson))

    def AddEXP(self,score):
        self.exp += score
        self.lesson += 1

class SpecialScore():
    def __init__(self):
        self.score = 500

class SpecialStudent(Student):
    def __init__(self,name,father):
        super().__init__(name) #__init__(name) มีค่า = Student(name)
        self.father = father
        mafia = ['Bill Gates','Thomas Edison']
        if father in mafia:
            self.exp += 100
    
    def AddEXP(self, score):
        self.exp += (score * 3)
        self.lesson += 1
        
    def AskEXP(self,score=10):
        print('ขอคะเเนนพิเศษให้ผมหน่อยสิ {} EXP'.format(score))
        self.AddEXP(score)
            

print('====== 1 Jan ======')

student0 = SpecialStudent('Mark Zuckerberg','Bill Gates')
student0.ShowEXP()
student0.AskEXP()
student0.ShowEXP()

student1 = Student('Albert')
print(student1.name)
student1.Hello()

print("-------------")
student2 = Student('Steve')
print(student2.name)
student2.Hello()
print('====== 2 Jan ======')
print('------- ใครอยากเรียน coding บ้าง (10 exp)--------')
student1.AddEXP(10)

print('====== 3 Jan ======')
student1.name = 'Albert Einstein'
print('ตอนนี้ exp ของเเต่ละคนได้เท่าไหร่กันเเล้ว')
print(student1.name, student1.exp)
print(student2.name, student2.exp)

print('====== 4 Jan ======')
for i in range(5):
    student2.Coding()

student1.ShowEXP()
student2.ShowEXP()