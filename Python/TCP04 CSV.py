import snap7
from time import sleep
import matplotlib.pyplot as plt
import csv

# สร้าง client object และเชื่อมต่อกับ PLC
plc = snap7.client.Client()
plc.connect("192.168.0.3", 0, 1)

# ตัวแปรสำหรับเก็บผลลัพธ์ที่อ่านมา
results = [[] for _ in range(5)]  # สำหรับเก็บค่าทั้ง 5 ค่าใน 5 รายการ

# ฟังก์ชันอ่านและแปลงข้อมูล
def read_values_from_plc():
    # อ่านข้อมูลจาก DataBlock 1 เริ่มที่ตำแหน่ง 0 จำนวน 10 ไบต์
    data = plc.db_read(4, 0, 10)
    
    # แยกค่า 5 ค่าออกมาเป็น int
    values = []
    for i in range(5):
        value = snap7.util.get_int(data, i * 2)  # ค่า int ใช้ 2 ไบต์ในการเก็บ
        values.append(value)
    
    return values

# ฟังก์ชันเขียนข้อมูลลงไฟล์ CSV
def write_to_csv(filename, data):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# สร้างกราฟ
plt.ion()  # เปิดโหมด interactive เพื่อให้กราฟอัพเดตตลอดเวลา
fig, ax = plt.subplots()  # สร้างกราฟ
line1, = ax.plot([], [], label='SETPOINT')
line2, = ax.plot([], [], label='PV 1')
line3, = ax.plot([], [], label='PV 2')
line4, = ax.plot([], [], label='MV 1')
line5, = ax.plot([], [], label='MV 2')

ax.set_xlim(0, 100000)  # ขอบเขตแกน x
ax.set_ylim(0, 100)  # ขอบเขตแกน y
ax.legend()  # แสดง legend

# ตัวแปรสำหรับเก็บข้อมูล time step (แกน x)
x_data = []

# สร้างไฟล์ CSV และเขียนหัวข้อ (Header) ครั้งแรก
csv_filename = 'plc_data.csv'
write_to_csv(csv_filename, ['Time', 'SETPOINT', 'PV 1', 'PV 2', 'MV 1', 'MV 2'])

while True:
    # อ่านข้อมูลจาก PLC
    values = read_values_from_plc()
    
    # เก็บผลลัพธ์ลงในลิสต์
    for i in range(5):
        results[i].append(values[i])  # เก็บค่าที่อ่านมาในลิสต์
    
    # เก็บเวลาใน x_data สำหรับการพลอต
    x_data.append(len(x_data))

    # อัพเดตกราฟ
    line1.set_data(x_data, results[0])
    line2.set_data(x_data, results[1])
    line3.set_data(x_data, results[2])
    line4.set_data(x_data, results[3])
    line5.set_data(x_data, results[4])

    # รีเฟรชกราฟ
    plt.draw()
    plt.pause(1)  # รอ 1 วินาที เพื่อให้ข้อมูลอัพเดต

    # เขียนข้อมูลลงไฟล์ CSV ทุกครั้ง
    write_to_csv(csv_filename, [len(x_data), *values])  # บันทึกเวลาและค่าทั้ง 5

    # ออกเมื่อจำนวนข้อมูลเกิน 100 จุด
    if len(x_data) > 1000000:
        break

# ปิดการแสดงกราฟเมื่อเสร็จสิ้น
plt.ioff()
plt.show()
