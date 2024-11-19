import snap7
import matplotlib.pyplot as plt
from time import sleep

# สร้าง client object และเชื่อมต่อกับ PLC
plc = snap7.client.Client()
plc.connect("192.168.0.3", 0, 1)

# Byte array สำหรับเก็บข้อมูลที่อ่าน
byte = bytearray(100)  # ขนาด 10 ไบต์ สำหรับการอ่านข้อมูลจาก DB

# ตัวแปรสำหรับเก็บผลลัพธ์
result = []

# ตั้งค่าการแสดงกราฟ
plt.ion()  # เปิดโหมด interactive เพื่อให้กราฟอัพเดตทุกครั้ง
fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-')  # สร้างเส้นกราฟ (เริ่มต้นเป็นข้อมูลว่าง)

# กำหนดค่าต่างๆ
x_data = []  # แกน X (เวลาหรือรอบที่อ่านค่า)
y_data = []  # แกน Y (ค่าที่อ่านจาก PLC)

while True:
    # อ่านข้อมูลจาก DataBlock 3 เริ่มที่ตำแหน่ง 0 จำนวน 10 ไบต์
    seft = plc.db_read(1, 0, 12)
    
    # แปลงข้อมูลจาก 10 ไบต์ให้เป็น int 5 ค่า
    for i in range(1):
        value = snap7.util.get_int(seft, i * 2)  # ค่า int ใช้ 2 ไบต์ในการเก็บ
        result.append(value)
    
    # แสดงผลลัพธ์
    print("Values:", result)
    
    # เพิ่มข้อมูลใน x_data และ y_data
    x_data.append(len(x_data) + 1)  # เพิ่มรอบที่อ่านข้อมูล
    y_data.append(result[-1])  # ใช้ค่าที่ได้รับในรอบนี้

    # อัพเดตกราฟ
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    ax.relim()  # อัพเดตขอบเขตของกราฟ
    ax.autoscale_view()  # อัพเดตมุมมองกราฟ

    # ล้างผลลัพธ์ในลิสต์ก่อนอ่านค่าครั้งถัดไป
    result.clear()
    
    # อัพเดตกราฟในแต่ละรอบ
    plt.draw()
    plt.pause(1)  # รอ 1 วินาที และอัพเดตกราฟ

    # รอ 1 วินาที ก่อนอ่านค่าครั้งถัดไป
    sleep(1)
