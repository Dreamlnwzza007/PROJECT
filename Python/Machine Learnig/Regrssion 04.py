import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# โหลดข้อมูลจากไฟล์ CSV
file_path = r'C:\\Users\\Dreamlnwzza007\\Desktop\\PROJECT\\Python\\Machine Learnig\\Normal 02.csv'
data = pd.read_csv(file_path)

# ตรวจสอบข้อมูลเบื้องต้น
print(data.head())

# กำหนดให้ Outcome เป็นหมวดหมู่
data['Outcome'] = data['Outcome'].astype('category')

# สร้างกราฟ Scatter plot ของทุกข้อมูล (PV 1, PV 2, MV 1, MV 2)
plt.figure(figsize=(10, 8))

# แสดงข้อมูลทั้งหมดในกราฟเดียว โดยใช้ค่า Outcome แยกสี
sns.scatterplot(data=data, x='PV 1', y='MV 1', hue='Outcome', palette='Set1', style='Outcome', s=100)

# เพิ่มข้อมูล PV 2, MV 2 ในกราฟเดียว
sns.scatterplot(data=data, x='PV 2', y='MV 2', hue='Outcome', palette='Set2', style='Outcome', s=100, marker='X')

# ตั้งชื่อกราฟและแกน
plt.title('Scatter plot of PV 1, PV 2, MV 1, MV 2 by Outcome')
plt.xlabel('PV 1 & PV 2')
plt.ylabel('MV 1 & MV 2')

# แสดงตำนาน (legend)
plt.legend(title='Outcome')

# แสดงกราฟ
plt.show()
