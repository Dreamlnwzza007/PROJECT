int analogPin = A1;  // กำหนดขา Analog ที่จะอ่านค่า
int analogValue = 0;  // ตัวแปรเก็บค่าที่อ่านจากเซ็นเซอร์
int outputValue = 0;  // ตัวแปรเก็บค่าที่แปลงแล้วให้อยู่ในช่วง 0-255
int pumpPin = 10;  // กำหนดขา PWM ที่ใช้ควบคุมปั๊ม

void setup() {
  Serial.begin(9600);  
  pinMode(pumpPin, OUTPUT);  
}

void loop() {
  analogValue = analogRead(analogPin);  // อ่านค่าจากขา Analog
  outputValue = map(analogValue, 0, 1023, 0, 255);  // แปลงค่าจาก 0-1023 เป็น 0-255

  // ควบคุมปั๊มด้วย PWM
  analogWrite(pumpPin, outputValue);

  // แสดงผลค่าที่อ่านและแปลงแล้วใน Serial Monitor
  Serial.print("Analog Value: ");
  Serial.print(analogValue);
  Serial.print(" -> Mapped Value: ");
  Serial.println(outputValue);

  delay(100); 
}
