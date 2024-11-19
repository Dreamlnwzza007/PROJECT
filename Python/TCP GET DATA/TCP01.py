import snap7
from time import sleep

# สร้าง client object และเชื่อมต่อกับ PLC
plc = snap7.client.Client()
plc.connect("192.168.0.3", 0, 1)

# Byte array สำหรับเก็บข้อมูลที่อ่าน
byte = bytearray(100)  # ขนาด 10 ไบต์ สำหรับการอ่านข้อมูลจาก DB

# ตัวแปรสำหรับเก็บผลลัพธ์
result = []

while True:
    # อ่านข้อมูลจาก DataBlock 3 เริ่มที่ตำแหน่ง 0 จำนวน 10 ไบต์
    seft = plc.db_read(1, 0, 10)
    
    # แปลงข้อมูลจาก 10 ไบต์ให้เป็น int 5 ค่า
    for i in range(5):
        value = snap7.util.get_int(seft, i * 2)  # ค่า int ใช้ 2 ไบต์ในการเก็บ
        result.append(value)
    
    # แสดงผลลัพธ์
    print("Values:", result)
    
    # ล้างผลลัพธ์ในลิสต์ก่อนอ่านค่าครั้งถัดไป
    result.clear()
    
    # รอ 1 วินาที
    sleep(1)
