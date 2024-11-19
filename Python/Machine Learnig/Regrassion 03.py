import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# โหลดข้อมูลจากไฟล์ CSV
file_path = r'C:\\Users\\MSI\\Desktop\\PROJECT\\Python\\Machine Learnig\\Normal 02.csv'
data = pd.read_csv(file_path)

# ตรวจสอบข้อมูลเบื้องต้น
print(data.head())

# กำหนดให้ Outcome เป็นหมวดหมู่ (สำหรับการแบ่งกลุ่มข้อมูลในกราฟ)
data['Outcome'] = data['Outcome'].astype('category')

# 1. สร้าง Pair Plot โดยแสดงความสัมพันธ์ระหว่างทุกคอลัมน์ PV 1, PV 2, MV 1, MV 2
sns.pairplot(data, hue='Outcome', palette='Set1', markers=["o", "s"])

# กำหนดชื่อกราฟและแสดงผล
plt.suptitle('Pair Plot of PV 1, PV 2, MV 1, MV 2 by Outcome', y=1.02)
plt.show()

# 2. หรือสร้างกราฟ Scatter ของแต่ละคู่คอลัมน์
# กราฟ 1: PV 1 vs PV 2
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='PV 1', y='PV 2', hue='Outcome', palette='Set1', style='Outcome', s=100)
plt.title('Scatter plot of PV 1 vs PV 2 by Outcome')
plt.xlabel('PV 1')
plt.ylabel('PV 2')
plt.legend(title='Outcome')
plt.show()

# กราฟ 2: MV 1 vs MV 2
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='MV 1', y='MV 2', hue='Outcome', palette='Set1', style='Outcome', s=100)
plt.title('Scatter plot of MV 1 vs MV 2 by Outcome')
plt.xlabel('MV 1')
plt.ylabel('MV 2')
plt.legend(title='Outcome')
plt.show()

# กราฟ 3: PV 1 vs MV 1
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='PV 1', y='MV 1', hue='Outcome', palette='Set1', style='Outcome', s=100)
plt.title('Scatter plot of PV 1 vs MV 1 by Outcome')
plt.xlabel('PV 1')
plt.ylabel('MV 1')
plt.legend(title='Outcome')
plt.show()

# กราฟ 4: PV 2 vs MV 2
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='PV 2', y='MV 2', hue='Outcome', palette='Set1', style='Outcome', s=100)
plt.title('Scatter plot of PV 2 vs MV 2 by Outcome')
plt.xlabel('PV 2')
plt.ylabel('MV 2')
plt.legend(title='Outcome')
plt.show()
