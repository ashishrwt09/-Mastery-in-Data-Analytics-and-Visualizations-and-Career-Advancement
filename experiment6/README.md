# Experiment No. 6: Predictive Analytics using Linear Regression and Model Performance Evaluation

## Aim
To develop a Linear Regression model using Python for predicting continuous outcomes and evaluate its performance using appropriate regression metrics.

---

## Questions & Answers

### Q1. What is Predictive Analytics, and how is it used in real-world applications?
**Answer:**
* **Predictive Analytics:** The branch of advanced analytics that utilizes historical data, statistical algorithms, and machine learning techniques to identify the likelihood of future outcomes.
* **Real-World Applications:**
  * **Finance:** Credit scoring, fraud detection, and stock price forecasting.
  * **Healthcare:** Predicting patient readmission rates and disease outbreaks.
  * **Marketing:** Customer churn prediction and targeted advertising.

---

### Q2. Explain the working principle of the Linear Regression algorithm.
**Answer:**
Linear Regression is a supervised learning algorithm used to model the linear relationship between independent variables ($X$) and a continuous target variable ($y$).

* **Mathematical Equation:**
  $$y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_n X_n + \epsilon$$
  Where:
  * $y$ = Target variable
  * $\beta_0$ = $y$-intercept
  * $\beta_1, \beta_2, \dots, \beta_n$ = Regression coefficients
  * $\epsilon$ = Error term

* **Optimization:** The algorithm fits a straight line (or hyperplane) by minimizing the **Sum of Squared Errors (SSE)** between the actual values and predicted values using methods like **Ordinary Least Squares (OLS)** or **Gradient Descent**.

---

### Q3. Differentiate between dependent and independent variables with suitable examples.
**Answer:**

| Feature | Independent Variable ($X$) | Dependent Variable ($y$) |
| :--- | :--- | :--- |
| **Definition** | Inputs/predictors manipulated or measured to predict the output. | Target/outcome metric being predicted. |
| **Role** | Serves as the cause or input factor. | Serves as the effect or response variable. |
| **Example (Housing)** | House Area (SqFt), Number of Bedrooms, Age of House. | House Sale Price. |
| **Example (Sales)** | Advertising Budget spent on TV/Social Media. | Total Units Sold. |

---

### Q4. Why is it necessary to split the dataset into training and testing sets?
**Answer:**
* **Generalization Assessment:** Evaluates how accurately the model performs on unseen, real-world data.
* **Overfitting Prevention:** Ensures the algorithm is not merely memorizing training samples, but learning real underlying patterns.
* **Model Validation:** Provides an unbiased estimate of performance metrics ($MAE$, $RMSE$, $R^2$) prior to production deployment.

---

### Q5. What is the significance of the $R^2$ Score in regression analysis?
**Answer:**
The **$R^2$ Score (Coefficient of Determination)** measures the proportion of total variance in the dependent variable that is predictable from the independent variables.

* **Formula:**
  $$R^2 = 1 - \frac{\text{Sum of Squared Residuals (SSR)}}{\text{Total Sum of Squares (SST)}}$$
* **Interpretation:**
  * Range: $0$ to $1$ (or $0\%$ to $100\%$).
  * An $R^2$ of **0.85** implies that $85\%$ of the variance in the target variable (e.g., House Price) is explained by the model's feature set.

---

### Q6. Differentiate between MAE, MSE, and RMSE. Which metric is more sensitive to large prediction errors?
**Answer:**

* **Mean Absolute Error (MAE):** Average absolute difference between actual and predicted values. It treats all error sizes linearly.
  $$\text{MAE} = \frac{1}{n} \sum |y - \hat{y}|$$

* **Mean Squared Error (MSE):** Average of squared errors. Squaring removes negative signs but alters measurement units to squared values.
  $$\text{MSE} = \frac{1}{n} \sum (y - \hat{y})^2$$

* **Root Mean Squared Error (RMSE):** Square root of MSE. Converts units back to original target scale.
  $$\text{RMSE} = \sqrt{\frac{1}{n} \sum (y - \hat{y})^2}$$

* **Sensitivity:** **MSE and RMSE** are significantly more sensitive to large prediction errors/outliers because the residuals are squared prior to averaging.

---

### Q7. What assumptions should be satisfied before applying Linear Regression?
**Answer:**
1. **Linearity:** Linear relationship between features and target.
2. **Independence:** Observations/errors are independent (no autocorrelation).
3. **Homoscedasticity:** Constant variance of residuals across all predictor levels.
4. **Normality:** Residuals follow a normal distribution.
5. **No Multicollinearity:** Predictor variables are not highly correlated with each other.

---

### Q8. How can overfitting and underfitting affect the performance of a regression model?
**Answer:**
* **Underfitting (High Bias):**
  * Model is too simple to capture patterns.
  * *Effect:* Poor performance on both training and test data.
* **Overfitting (High Variance):**
  * Model learns noise and random fluctuations in training data.
  * *Effect:* Exceptionally low training error, but high error on unseen test data.

---

### Q9. Mention any three real-world applications of Linear Regression in business or industry.
**Answer:**
1. **Real Estate:** Estimating property valuation based on location, square footage, and amenities.
2. **Retail & Sales:** Forecasting seasonal demand and sales revenue based on marketing expenditure.
3. **Insurance:** Setting premium prices based on age, medical history, and risk factors.

---

### Q10. How can feature selection improve the accuracy and interpretability of a predictive model?
**Answer:**
* **Reduces Multicollinearity:** Eliminates redundant features that inflate standard errors of regression coefficients.
* **Mitigates Overfitting:** Simplifies model complexity, improving generalization on test data.
* **Speeds Up Training:** Reduces computational overhead and data storage requirements.
* **Enhances Interpretability:** Focuses business insights on key drivers influencing the target metric.
