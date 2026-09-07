# ==============================================================================
# STEP 1 & 2: Load Libraries & Dataset (Synthetic fallback if dataset missing)
# Dataset: Titanic Survival Dataset
# ==============================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Set style
sns.set_theme(style="whitegrid")

# Load Dataset
try:
    df = pd.read_csv('titanic.csv')
    print("Dataset successfully loaded!")
except FileNotFoundError:
    print("Dataset not found! Generating sample Titanic dataset...")
    np.random.seed(42)
    n = 300
    df = pd.DataFrame({
        'PassengerId': range(1, n + 1),
        'Survived': np.random.choice([0, 1], size=n, p=[0.6, 0.4]),
        'Pclass': np.random.choice([1, 2, 3], size=n),
        'Sex': np.random.choice(['male', 'female'], size=n),
        'Age': np.random.choice([np.nan, 22, 38, 26, 35, 54, 2, 27, 14, 4], size=n),
        'SibSp': np.random.choice([0, 1, 2, 3], size=n, p=[0.7, 0.2, 0.05, 0.05]),
        'Parch': np.random.choice([0, 1, 2], size=n, p=[0.8, 0.15, 0.05]),
        'Fare': np.random.exponential(scale=30, size=n) + 7.25,
        'Embarked': np.random.choice(['S', 'C', 'Q', np.nan], size=n, p=[0.7, 0.2, 0.08, 0.02])
    })

# ==============================================================================
# STEP 3: Inspect Dataset
# ==============================================================================
print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- DATASET INFO ---")
print(df.info())

print("\n--- DESCRIPTIVE STATISTICS ---")
print(df.describe())

# ==============================================================================
# STEP 4: Handle Missing Values
# ==============================================================================
# Fill numerical missing values with Median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill categorical missing values with Mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# ==============================================================================
# STEP 5: Remove Duplicates
# ==============================================================================
df.drop_duplicates(inplace=True)

# ==============================================================================
# STEP 6: Categorical Encoding
# ==============================================================================
# Label Encoding for binary feature 'Sex'
le = LabelEncoder()
df['Sex_Encoded'] = le.fit_transform(df['Sex'])

# One-Hot Encoding for multi-class feature 'Embarked'
df = pd.get_dummies(df, columns=['Embarked'], prefix='Embarked', drop_first=True)

# ==============================================================================
# STEP 7: Outlier Detection and Treatment via IQR
# ==============================================================================
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR
lower_bound = Q1 - 1.5 * IQR

# Cap outliers to upper and lower bounds
df['Fare'] = np.where(df['Fare'] > upper_bound, upper_bound, df['Fare'])
df['Fare'] = np.where(df['Fare'] < lower_bound, lower_bound, df['Fare'])

# ==============================================================================
# STEP 8: Feature Scaling (Standardization)
# ==============================================================================
scaler = StandardScaler()
df[['Age_Scaled', 'Fare_Scaled']] = scaler.fit_transform(df[['Age', 'Fare']])

# ==============================================================================
# STEP 9: Feature Engineering
# ==============================================================================
# Create FamilySize feature
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# Create IsAlone indicator feature
df['IsAlone'] = np.where(df['FamilySize'] == 1, 1, 0)

# ==============================================================================
# STEP 10: Save Cleaned Dataset
# ==============================================================================
df.to_csv('cleaned_titanic.csv', index=False)
print("\nCleaned dataset saved successfully as 'cleaned_titanic.csv'!")