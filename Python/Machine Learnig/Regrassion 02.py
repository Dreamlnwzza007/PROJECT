import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# โหลดข้อมูลจากไฟล์ CSV
file_path = r'C:\\Users\\Dreamlnwzza007\\Desktop\\PROJECT\\Python\\Machine Learnig\\Normal 02.csv'
data = pd.read_csv(file_path)

# ตรวจสอบข้อมูลบางส่วน
print(data.head())

# กำหนดให้ Outcome เป็นหมวดหมู่
data['Outcome'] = data['Outcome'].astype('category')

# ตั้งค่าขนาดกราฟ
plt.figure(figsize=(10, 6))

# ใช้ seaborn เพื่อสร้างกราฟ scatter plot โดยแยกตามคลาสของ Outcome
sns.scatterplot(data=data, x='PV 2', y='MV 2', hue='Outcome', palette='Set1', style='Outcome', s=100)

# ตั้งชื่อกราฟและแกน
plt.title('Scatter plot of PV 1 vs MV 1, colored by Outcome')
plt.xlabel('PV 1')
plt.ylabel('MV 1')

# แสดงตำนาน (legend)
plt.legend(title='Outcome')

# แสดงกราฟ
plt.show()
