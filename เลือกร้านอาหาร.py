from pprint import pprint #pretty print ช่วยจัดรูปเเบบการ print
import random

money = int(input('คุณมีเงินเท่าไหร่ :'))
restuarant = {'high':[{'name':'shitsuka sushi','price':700},
                {'name':'Peporini','price':500}],
            'medium':[{'name':'เสวย','price':200},
                {'name':'รสดี','price':250}],
            'low':[{'name':'ป้าส้ม','price':40},
                {'name':'ป้าเล็กกระเพรา','price':50}]}

#pprint(restuarant)
#money = 200
if money >= 500:
    #ใช้ choice ได้ก็ต่อเมื่อข้อมูลเป็น list
    select = random.choice(restuarant['high'])
    print('คุณผู้หญิงทานร้าน {} ดีมั้ยครับ? ราคาเริ่มต้น {} บาท'.format(select['name'],select['price']))
elif money >= 200:
    select = random.choice(restuarant['medium'])
    print('คุณพี่ทานร้าน {} ดีมั้ยครับ? ราคาเริ่มต้น {} บาท'.format(select['name'],select['price']))
else:
    select = random.choice(restuarant['low'])
    print('พี่ทานร้าน {} ดีมั้ยครับ? ราคาเริ่มต้น {} บาท'.format(select['name'],select['price']))