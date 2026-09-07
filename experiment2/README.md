# Experiment 2: Exploratory Data Analysis (EDA) on a Real-World Business Dataset

## Questions & Answers

### Q1. What is Exploratory Data Analysis (EDA), and why is it performed before machine learning?
* **Definition:** EDA is the process of analyzing datasets through summary statistics and visual representations to understand their structure, distributions, and underlying relationships[cite: 3].
* **Why before Machine Learning:** It helps detect anomalies, handle missing values, uncover feature patterns, and validate assumptions required for reliable predictive modeling[cite: 3].

---

### Q2. Differentiate between univariate, bivariate, and multivariate analysis with suitable examples.
* **Univariate Analysis:** Analyzes a single variable at a time (e.g., studying the histogram of employee ages)[cite: 3].
* **Bivariate Analysis:** Examines the relationship between two variables (e.g., scatter plot of house area vs. price)[cite: 3].
* **Multivariate Analysis:** Explores interactions among three or more variables simultaneously (e.g., analyzing sales across regions colored by product categories)[cite: 3].

---

### Q3. What insights can be obtained from a correlation heatmap?
* **Feature Relationships:** Identifies strong linear relationships (positive or negative) between continuous numerical variables[cite: 3].
* **Multicollinearity Detection:** Highlights redundant or highly collinear independent variables to avoid overfitting in regression models[cite: 3].

---

### Q4. Explain the purpose of histograms, box plots, and scatter plots in EDA.
* **Histogram:** Visualizes the frequency distribution, central tendency, and skewness of a single continuous variable[cite: 3].
* **Box Plot:** Summarizes data dispersion using quantiles and identifies statistical outliers[cite: 3].
* **Scatter Plot:** Displays relationship trends and cluster groupings between two continuous variables[cite: 3].

---

### Q5. How can EDA help identify data quality issues before analysis?
* Flags missing or null values in dataset attributes[cite: 3].
* Spotlights extreme values or data entry errors via box plots and scatter plots[cite: 3].
* Uncovers inconsistent categorical entries (e.g., duplicate names with varied casing) and severe class imbalances[cite: 3].

---

### Q6. Why is correlation important in predictive analytics? Can correlation imply causation?
* **Importance:** Helps select key features that strongly influence the target outcome, improving prediction quality[cite: 3].
* **Causation:** **No, correlation does not imply causation.** Two variables may move together due to a third confounding factor or purely by coincidence, not necessarily because one directly causes the other.

---

### Q7. Which visualization would you use to analyze categorical and numerical variables? Justify your choice.
* **Chosen Visualization:** **Box Plot** or **Grouped Bar Plot** (Count/Mean)[cite: 3].
* **Justification:** Box plots clearly show how a numerical metric's median, spread, and outliers vary across distinct categories[cite: 3].

---

### Q8. What business insights can be derived from the Netflix (or Superstore/HR Analytics) dataset through EDA?
* **Netflix Example:** Reveals shift trends from movies to multi-season TV shows, dominant content ratings (e.g., TV-MA), and top content-producing regions[cite: 3].
* **Superstore Example:** Identifies non-profitable product sub-categories, high-performing regions, and seasonality in annual sales[cite: 3].

---

### Q9. How does EDA contribute to feature selection and model building?
* Helps drop non-informative or redundant features with low variance or extreme correlation[cite: 3].
* Guides feature transformation decisions (e.g., log transforms for skewed features)[cite: 3].
* Informs categorical encoding strategies based on category frequency distributions[cite: 3].

---

### Q10. What challenges might arise while performing EDA on large-scale real-world datasets?
* High memory usage and computational slowness when loading large datasets into RAM.
* Overplotting in scatter plots when rendering millions of data points.
* Managing noisy, incomplete, or high-cardinality categorical data.
