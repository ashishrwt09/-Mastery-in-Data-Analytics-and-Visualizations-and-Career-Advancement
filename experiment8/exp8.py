import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# 1. GENERATE SYNTHETIC TELCO CUSTOMER CHURN DATASET
np.random.seed(42)
n_samples = 250

tenure = np.random.randint(1, 72, n_samples)
monthly_charges = np.random.uniform(20.0, 120.0, n_samples).round(2)
contract_type = np.random.choice([0, 1, 2], n_samples) # 0: Month-to-month, 1: One year, 2: Two year
tech_support = np.random.choice([0, 1], n_samples)    # 0: No, 1: Yes

# Churn logic
churn_prob = 0.6 * (tenure < 12) + 0.3 * (contract_type == 0) + 0.1 * (monthly_charges > 70) - 0.2 * (tech_support == 1)
churn = (churn_prob > 0.5).astype(int)

df = pd.DataFrame({
    'Tenure_Months': tenure,
    'Monthly_Charges': monthly_charges,
    'Contract_Type': contract_type,
    'Tech_Support': tech_support,
    'Churn': churn
})

# Save output dataset CSV
df.to_csv('customer_churn_data.csv', index=False)

# 2. FEATURE SELECTION & TRAIN-TEST SPLIT (80:20)
X = df[['Tenure_Months', 'Monthly_Charges', 'Contract_Type', 'Tech_Support']]
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. TRAIN DECISION TREE CLASSIFIER
clf = DecisionTreeClassifier(criterion='gini', max_depth=4, random_state=42)
clf.fit(X_train, y_train)

# 4. PREDICTIONS & EVALUATION
y_pred = clf.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("=" * 55)
print("  EXPERIMENT 8: DECISION TREE CHURN CLASSIFICATION  ")
print("=" * 55)
print(f"Accuracy  : {acc * 100:.2f}%")
print(f"Precision : {prec:.4f}")
print(f"Recall    : {rec:.4f}")
print(f"F1-Score  : {f1:.4f}\n")

print("--- CONFUSION MATRIX ---")
print(f"True Negatives (TN): {cm[0][0]} | False Positives (FP): {cm[0][1]}")
print(f"False Negatives (FN): {cm[1][0]} | True Positives (TP) : {cm[1][1]}\n")

print("--- FEATURE IMPORTANCE ---")
for feature, importance in zip(X.columns, clf.feature_importances_):
    print(f"{feature}: {importance:.4f}")

print("\n[SUCCESS] Model evaluation complete & saved to 'customer_churn_data.csv'!")