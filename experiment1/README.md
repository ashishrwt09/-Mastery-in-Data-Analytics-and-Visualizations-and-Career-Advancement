# Experiment 1: Real-World Data Collection, Cleaning and Preprocessing using Python

## Questions & Answers

### Q1. Why is data preprocessing considered one of the most important phases in data analytics?
* **Ensures Data Quality:** Real-world datasets contain noise, missing values, duplicates, and outliers that ruin analytical accuracy.
* **Improves Model Accuracy:** High-quality preprocessed data prevents biased learning and enables machine learning algorithms to converge faster with better accuracy.

---

### Q2. Explain different methods of handling missing values with suitable examples.
* **Deletion:** Dropping rows or columns with excessive missing data (e.g., dropping a column missing 80% of its records).
* **Imputation (Mean/Median):** Replacing missing numerical values with the mean (for normal distributions) or median (for skewed data, like replacing missing Age with 28).
* **Categorical Imputation (Mode):** Replacing missing categorical values with the most frequent value (e.g., filling missing Embarked with 'S').

---

### Q3. Differentiate between Label Encoding and One-Hot Encoding.
* **Label Encoding:** Assigns an integer value to each category (e.g., Low=0, Medium=1, High=2). Best for ordinal variables where rank matters.
* **One-Hot Encoding:** Creates separate binary columns (0 or 1) for each category. Best for nominal variables with no inherent order (e.g., Red, Blue, Green) to prevent false numerical ordering assumptions.

---

### Q4. What are outliers? How can they affect analytical results?
* **Definition:** Outliers are data points that differ significantly from other observations in the dataset.
* **Effect:** They skew mean and variance calculations, distort regression lines, and negatively impact distance-based machine learning algorithms (like k-NN or K-Means).

---

### Q5. Explain the difference between normalization and standardization.
* **Normalization (Min-Max Scaling):** Scales features to a fixed range, typically [0, 1].
* **Standardization (Z-Score Normalization):** Centers data around a mean of 0 with a standard deviation of 1.

---

### Q6. Why should duplicate records be removed before analysis?
* **Prevents Data Bias:** Prevents giving double weight to identical records, which skews statistical metrics.
* **Prevents Overfitting:** Avoids data leakage between training and testing split sets during model evaluation.

---

### Q7. What is feature engineering? Give two practical examples.
* **Definition:** The process of using domain knowledge to create new input variables/features from raw data to enhance model performance.
* **Example 1:** Combining `SibSp` (siblings/spouses) and `Parch` (parents/children) to create `FamilySize`.
* **Example 2:** Extracting `IsAlone` (binary indicator) or converting raw timestamps into `HourOfDay` or `IsWeekend`.

---

### Q8. Which preprocessing techniques would you apply to the IBM HR Employee Attrition dataset and why?
* **One-Hot Encoding:** Convert categorical attributes like `Department` and `JobRole` into numerical binary columns.
* **Outlier Capping:** Apply Interquartile Range (IQR) capping on skewed financial variables like `MonthlyIncome`.
* **Standardization:** Scale continuous numerical attributes like `Age`, `TotalWorkingYears`, and `MonthlyIncome`.

---

### Q9. How does poor-quality data affect machine learning model performance?
* Leads to "Garbage In, Garbage Out" (GIGO) where model predictions become unreliable.
* Introduces algorithmic bias, high variance, and poor generalization performance on unseen real-world test data.

---

### Q10. Name any three Python libraries commonly used for data preprocessing.
1. **Pandas:** For data manipulation, missing value handling, and duplicate removal.
2. **NumPy:** For vectorized numerical operations and mathematical array transformations.
3. **Scikit-Learn (sklearn.preprocessing):** For feature scaling, normalization, and categorical encoding.
