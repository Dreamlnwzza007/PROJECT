import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
file_path = 'C:\\Users\\MSI\\Desktop\\PROJECT\\Python\\Machine Learnig\\Normal.csv'
data = np.loadtxt(file_path, delimiter=",", skiprows=1)

# Feature names
feature_names = ['SETPOINT', 'PV 1', 'PV 2', 'MV 1', 'MV 2']

# Separate features (X) and target (y)
X = data[:, :-1]  # All rows, all columns except the last (features)
y = data[:, -1]   # Last column (target: Outcome)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Plot 1: Box plot of original features
plt.figure(figsize=(13, 6))
plt.boxplot(X, patch_artist=True)
plt.title('The distribution of features before scaling', fontsize=14)
plt.xticks(ticks=range(1, len(feature_names) + 1), labels=feature_names, fontsize=14)
plt.yticks(fontsize=14)
plt.tight_layout()
plt.show()

# Plot 2: Box plot of scaled features
plt.figure(figsize=(13, 6))
plt.boxplot(X_scaled, patch_artist=True)
plt.title('The distribution of features after scaling', fontsize=14)
plt.xticks(ticks=range(1, len(feature_names) + 1), labels=feature_names, fontsize=14)
plt.yticks(fontsize=14)
plt.tight_layout()
plt.show()

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Prompt user for input (new sample)
def get_user_input():
    print("กรุณากรอกค่าตัวอย่างใหม่สำหรับการทำนาย:")
    inputs = []
    for feature in feature_names:
        value = float(input(f"{feature}: "))
        inputs.append(value)
    return np.array(inputs).reshape(1, -1)

# Standardize the new input using the same scaler
user_input = get_user_input()
user_input_scaled = scaler.transform(user_input)

# Make prediction for the new input
prediction = model.predict(user_input_scaled)

# Output the result
print(f"ผลลัพธ์การทำนาย (1-6): {prediction[0]}")

# Check if the input matches known conditions (optional enhancement)
def check_condition(prediction):
    # Define your conditions, for example:
    conditions = {
        1: "Condition 1: This is the first condition",
        2: "Condition 2: This is the second condition",
        3: "Condition 3: This is the third condition",
        4: "Condition 4: This is the fourth condition",
        5: "Condition 5: This is the fifth condition",
        6: "Condition 6: This is the sixth condition",
    }

    # Check if prediction matches any condition
    if prediction[0] in conditions:
        print(f"ผลลัพธ์ตรงกับเงื่อนไข: {conditions[prediction[0]]}")
    else:
        print("ผลลัพธ์ไม่เข้าเงื่อนไขใด")

# Check if the new sample matches any known condition
check_condition(prediction)
