import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE

# Load the dataset
data = pd.read_csv('D:\\Local Disk (E)\\ARCH TECHNOLOGIES\\Cyber Security\\Month 2 Tasks\\Task 4 Credit Card Fraud Detection\\creditcard.csv')

# Check for missing values
print(data.isnull().sum())

# Separate features and target variable
X = data.drop(['Class'], axis=1)
y = data['Class']

# Handle class imbalance
smote = SMOTE()
X_resampled, y_resampled = smote.fit_resample(X, y)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate performance
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
