import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. GENERATE SYNTHETIC DATASET (House Price Prediction)
np.random.seed(42)
n_samples = 200

area = np.random.randint(600, 3500, n_samples)
bedrooms = np.random.randint(1, 6, n_samples)
age = np.random.randint(1, 30, n_samples)

price = 50000 + (area * 150) + (bedrooms * 10000) - (age * 2000) + np.random.normal(0, 15000, n_samples)

df = pd.DataFrame({
    'Area_SqFt': area,
    'Bedrooms': bedrooms,
    'Age_Years': age,
    'Price': price.round(2)
})

# Save clean dataset
df.to_csv('house_price_data.csv', index=False)

# 2. FEATURE SELECTION & TRAIN-TEST SPLIT (80:20)
X = df[['Area_SqFt', 'Bedrooms', 'Age_Years']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. TRAIN LINEAR REGRESSION MODEL
model = LinearRegression()
model.fit(X_train, y_train)

# 4. PREDICTIONS
y_pred = model.predict(X_test)

# 5. MODEL EVALUATION METRICS
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("=" * 50)
print("     EXPERIMENT 6: LINEAR REGRESSION EVALUATION     ")
print("=" * 50)
print(f"Mean Absolute Error (MAE)  : ${mae:,.2f}")
print(f"Mean Squared Error (MSE)   : ${mse:,.2f}")
print(f"Root Mean Squared Error    : ${rmse:,.2f}")
print(f"R-squared (R2) Score       : {r2:.4f}\n")

print("--- REGRESSION COEFFICIENTS ---")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.2f}")
print(f"Intercept: {model.intercept_:.2f}\n")
print("[SUCCESS] Model trained and evaluated successfully!")