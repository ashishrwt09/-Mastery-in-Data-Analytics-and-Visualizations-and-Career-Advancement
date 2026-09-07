# Experiment 3: Questions & Answers

### Q1. What is the difference between descriptive statistics and inferential statistics?
* **Descriptive Statistics:** Summarizes, organizes, and describes key features of a dataset using numerical measures (e.g., mean, median, variance) and visual plots without making predictions beyond the data[cite: 1].
* **Inferential Statistics:** Uses sample data to draw conclusions, test hypotheses, and make predictions about a larger population using statistical methods[cite: 1].

---

### Q2. Explain the concepts of the Null Hypothesis (H0) and Alternative Hypothesis (H1).
* **Null Hypothesis (H0):** Assumes that there is no effect, no relationship, or no significant difference between variables in a population[cite: 1].
* **Alternative Hypothesis (H1):** Assumes that there is a statistically significant effect, relationship, or difference between variables[cite: 1].

---

### Q3. What is a p-value? How is it used to make statistical decisions?
* **Definition:** The probability of obtaining test results at least as extreme as the observed results, assuming the null hypothesis (H0) is true[cite: 1].
* **Decision Rule:**
  * **p <= 0.05:** Reject H0 (statistically significant)[cite: 1].
  * **p > 0.05:** Fail to reject H0 (insufficient evidence)[cite: 1].

---

### Q4. Differentiate between a t-test and ANOVA. In which situations is each test applied?
* **Independent Sample t-test:** Compares the means of **2 independent groups** (e.g., comparing income between employees who leave vs stay)[cite: 1].
* **One-Way ANOVA:** Compares the means across **3 or more independent groups** simultaneously (e.g., comparing job satisfaction across multiple job roles)[cite: 1].

---

### Q5. What does the Pearson correlation coefficient indicate? What are its possible values?
* **Indication:** Measures the direction and strength of a linear relationship between two continuous variables[cite: 1].
* **Range:** Values range from **-1 to +1**:
  * `+1`: Perfect positive linear correlation.
  * `0`: No linear correlation.
  * `-1`: Perfect negative linear correlation.

---

### Q6. Explain the significance of R² (Coefficient of Determination) in Linear Regression.
* **Significance:** R² represents the proportion of variance in the dependent variable explained by the independent variable(s)[cite: 1].
* **Interpretation:** Values range from `0` to `1` (or `0%` to `100%`). An R² of 0.85 means 85% of the outcome's variability is explained by the regression model.

---

### Q7. Why is statistical analysis important before applying machine learning algorithms?
* Detects anomalies, missing values, and potential outliers in the data.
* Identifies multicollinearity between features to avoid redundant inputs.
* Helps select relevant features based on statistical significance.
* Validates key assumptions (such as normality and variance homogeneity) needed for statistical ML models.

---

### Q8. What assumptions should be satisfied before performing a t-test or ANOVA?
* **Normality:** Data in each group follows an approximately normal distribution.
* **Homogeneity of Variance:** Variances across groups are approximately equal.
* **Independence:** Samples and observations are independent of each other.
* **Continuous Scale:** The target variable is measured on an interval or ratio scale.

---

### Q9. How can regression analysis help organizations in forecasting and decision-making?
* **Forecasting:** Predicts continuous outcomes (e.g., estimating salary based on experience or forecasting sales)[cite: 1].
* **Impact Measurement:** Quantifies how changes in independent variables influence business target metrics[cite: 1].

---

### Q10. Give two real-world applications where hypothesis testing is commonly used in data analytics.
1. **A/B Testing in Digital Marketing:** Testing whether a new webpage design increases user conversions compared to the original design.
2. **Healthcare & Clinical Testing:** Testing whether a new medical treatment significantly improves patient recovery rate compared to a control group.
