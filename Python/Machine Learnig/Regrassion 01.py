import pandas as pd
import matplotlib.pyplot as plt

# โหลดข้อมูลจากไฟล์ CSV
data = pd.read_csv('C:\\Users\\MSI\\Desktop\\PROJECT\\Python\\Machine Learnig\\Normal 02.csv')  # เปลี่ยน path ให้ตรงกับที่เก็บไฟล์ของคุณ

# แสดงข้อมูลเบื้องต้น
print(data.head())

# สร้างกราฟให้แต่ละคอลัมน์ A, B, C, D, E
plt.figure(figsize=(10, 6))

# กำหนดกราฟประเภทที่ต้องการ เช่น เส้น, แท่ง หรือ scatter
plt.plot(data['SETPOINT'], label='SETPOINT', marker='o')
plt.plot(data['PV 1'], label='PV 1', marker='s')
plt.plot(data['PV 2'], label='PV 2', marker='^')
plt.plot(data['MV 1'], label='MV 1', marker='x')
plt.plot(data['MV 2'], label='MV 2', marker='d')

# เพิ่มรายละเอียดกราฟ
plt.title('Graph of SETPOINT, PV1, PV2, MV1, MV2')
plt.xlabel('Index')
plt.ylabel('Values')
plt.legend()

# แสดงกราฟ
plt.show()
