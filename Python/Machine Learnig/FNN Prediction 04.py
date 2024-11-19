import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np

# 1. นำเข้าข้อมูลจากไฟล์ CSV
df = pd.read_csv('C:\\Users\\MSI\\Desktop\\PROJECT\\Python\\Machine Learnig\\Normal.csv')  # เปลี่ยนชื่อไฟล์ตามที่คุณใช้

# 2. แยกฟีเจอร์และคลาส (คอลัมน์สุดท้ายคือ class)
X = df.iloc[:, :-1].values  # ฟีเจอร์ (ตัวแปร X) คือทุกคอลัมน์ยกเว้นคอลัมน์สุดท้าย
y = df.iloc[:, -1].values  # ป้ายคลาส (target variable y) คือคอลัมน์สุดท้าย

# 3. ทำการ Scaling ข้อมูล (ฟีเจอร์)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # การทำ scaling ข้อมูล

# 4. แปลงป้ายคลาส (labels) เป็นตัวเลข โดยใช้ LabelEncoder
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# 5. เปลี่ยนค่าป้ายคลาสเป็นรูปแบบ One-hot encoding
y_onehot = to_categorical(y_encoded)

# 6. แบ่งข้อมูลเป็น training set และ test set (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_onehot, test_size=0.2, random_state=42)

# 7. สร้างโมเดล FNN
model = Sequential()

# เลเยอร์ input layer
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))  # 64 units, input size = จำนวนฟีเจอร์

# เลเยอร์ hidden layer
model.add(Dense(64, activation='relu'))  # เลเยอร์ hidden ขนาด 64 units

# เลเยอร์ output layer (ใช้ softmax สำหรับ classification แบบหลายคลาส)
model.add(Dense(y_train.shape[1], activation='softmax'))  # จำนวน output units เท่ากับจำนวนคลาส

# สรุปโครงสร้างของโมเดล
model.summary()

# 8. คอมไพล์โมเดล
model.compile(loss='categorical_crossentropy',  # loss function สำหรับ multi-class classification
              optimizer='adam',  # optimizer ที่นิยมใช้
              metrics=['accuracy'])  # metric ที่ใช้วัดความแม่นยำ

# 9. ฝึกโมเดลด้วยข้อมูล training set
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

# 10. ทำนายผลลัพธ์จากข้อมูล test set
y_pred = model.predict(X_test)

# 11. เปลี่ยนค่าผลลัพธ์ที่เป็น One-hot encoding กลับมาเป็นป้ายคลาสเดิม
y_pred_classes = encoder.inverse_transform(y_pred.argmax(axis=1))
y_true_classes = encoder.inverse_transform(y_test.argmax(axis=1))

# 12. ประเมินผลโมเดลด้วยข้อมูล test set
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy*100:.2f}%")

# 13. ดูการทำนาย 5 ตัวอย่างแรก
print("Predictions:", y_pred_classes[:5])
print("True Labels:", y_true_classes[:5])

# 14. การ plot graph ของ training/validation loss และ accuracy
plt.figure(figsize=(12, 6))

# Plot loss
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='validation loss')
plt.title('Loss over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# Plot accuracy
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='train accuracy')
plt.plot(history.history['val_accuracy'], label='validation accuracy')
plt.title('Accuracy over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.tight_layout()
plt.show()

# ฟังก์ชันที่ให้กรอกข้อมูลใหม่และทำนาย
def predict_new_data(model, scaler, encoder):
    # ให้ผู้ใช้กรอกข้อมูลใหม่
    print("กรุณากรอกข้อมูลใหม่:")
    features = []
    
    # ใช้ชื่อคอลัมน์ของฟีเจอร์ทั้งหมดเพื่อให้กรอกข้อมูลได้สะดวก
    feature_names = df.columns[:-1]  # คอลัมน์ทั้งหมดยกเว้นสุดท้ายที่เป็น class
    for feature_name in feature_names:
        feature_value = float(input(f"กรอกค่าของ {feature_name}: "))
        features.append(feature_value)

    # แปลงข้อมูลที่กรอกให้เป็นรูปแบบ array
    new_data = np.array(features).reshape(1, -1)
    
    # ทำการ Scaling ข้อมูลใหม่
    new_data_scaled = scaler.transform(new_data)

    # ทำนายผลลัพธ์จากข้อมูลใหม่
    prediction = model.predict(new_data_scaled)

    # หาค่าความมั่นใจของการทำนาย
    confidence = np.max(prediction)

    # ถ้าความมั่นใจมากกว่า 50% แสดงว่าโมเดลมั่นใจในคลาสนั้นๆ
    if confidence >= 0.5:
        predicted_class = encoder.inverse_transform([np.argmax(prediction)])[0]
        print(f"ผลการทำนาย: ข้อมูลนี้เข้าข่ายคลาส '{predicted_class}' ด้วยความมั่นใจ {confidence*100:.2f}%")
    else:
        print("ผลการทำนาย: โมเดลไม่มั่นใจในผลลัพธ์นี้ (ความมั่นใจ < 80%) ไม่เข้าข่ายคลาสใด")

# เรียกใช้งานฟังก์ชันการทำนายข้อมูลใหม่
predict_new_data(model, scaler, encoder)
