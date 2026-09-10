# Experiment No. 8: Customer Churn Prediction using Decision Tree Classification

## Aim
To build and evaluate a Decision Tree Classification model for predicting customer churn using a real-world dataset and analyze the factors influencing customer retention.

---

## Questions & Answers

### Q1. What is classification, and how does it differ from regression?
**Answer:**
* **Classification:** A supervised learning task that maps input features to categorical class labels (e.g., *Churn* vs. *No Churn*).
* **Regression:** A supervised learning task that maps input features to a continuous numerical target (e.g., *Predicting House Prices*).

| Aspect | Classification | Regression |
| :--- | :--- | :--- |
| **Output Type** | Discrete / Categorical labels | Continuous numerical values |
| **Example** | Email Spam vs. Not Spam | Predicting future stock price |
| **Primary Evaluation Metrics** | Accuracy, Precision, Recall, F1-Score | MAE, MSE, RMSE, $R^2$ Score |

---

### Q2. Explain the working principle of the Decision Tree algorithm.
**Answer:**
A Decision Tree builds a flowchart-like tree structure by recursively partitioning the training dataset into smaller subsets:

1. **Root Node Selection:** Evaluates candidate feature split points using impurity criteria (Gini Index or Entropy) to select the optimal root node feature.
2. **Splitting Phase:** Splits data into branches based on feature threshold conditions.
3. **Recursive Partitioning:** Repeats the splitting process on child sub-nodes.
4. **Terminal / Leaf Nodes:** Stops splitting upon hitting predefined stopping criteria (e.g., `max_depth`, `min_samples_split`) and assigns class labels via majority voting.

---

### Q3. Differentiate between Gini Index and Entropy as splitting criteria.
**Answer:**

| Attribute | Gini Index | Entropy |
| :--- | :--- | :--- |
| **Formula** | $1 - \sum_{i=1}^{C} (p_i)^2$ | $-\sum_{i=1}^{C} p_i \log_2(p_i)$ |
| **Range** | $0$ to $0.5$ (for binary classification) | $0$ to $1$ (for binary classification) |
| **Computational Speed** | Faster (no logarithmic calculations required) | Slower (requires log calculations) |
| **Default Usage** | Default impurity measure in Scikit-learn | Preferred when measuring Information Gain explicitly |

---

### Q4. What is a Confusion Matrix? Explain its components.
**Answer:**
A **Confusion Matrix** is a $2 \times 2$ performance evaluation table comparing actual target classes with predicted classes:

* **True Positive (TP):** Model correctly predicted a churning customer as *Churn*.
* **True Negative (TN):** Model correctly predicted a retained customer as *No Churn*.
* **False Positive (FP - Type I Error):** Model incorrectly flagged a retained customer as *Churn*.
* **False Negative (FN - Type II Error):** Model incorrectly flagged an actual churning customer as *No Churn*.

---

### Q5. Define Accuracy, Precision, Recall, and F1-Score. Why are these metrics important?
**Answer:**
* **Accuracy:** Overall proportion of correct predictions across all classes.
  $$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
* **Precision:** Ratio of correctly predicted positive observations to total predicted positives.
  $$\text{Precision} = \frac{TP}{TP + FP}$$
* **Recall (Sensitivity):** Ratio of correctly predicted positive observations to all actual positive instances.
  $$\text{Recall} = \frac{TP}{TP + FN}$$
* **F1-Score:** Harmonic mean of Precision and Recall, crucial for handling imbalanced datasets.
  $$\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

---

### Q6. What is overfitting in a Decision Tree? How can it be reduced?
**Answer:**
* **Overfitting:** Occurs when a Decision Tree grows unconstrained, memorizing noisy training data details and creating overly complex decision boundaries. This results in high training accuracy but poor generalization on test data.
* **Reduction Strategies:**
  1. **Pre-Pruning:** Setting hyperparameter limits like `max_depth`, `min_samples_split`, or `min_samples_leaf`.
  2. **Post-Pruning:** Trimming branches after full tree growth using Cost Complexity Pruning (`ccp_alpha`).
  3. **Ensemble Methods:** Using Random Forests or Gradient Boosted Trees.

---

### Q7. Why is customer churn prediction important for businesses?
**Answer:**
* **Cost Efficiency:** Acquiring a new customer is up to 5x to 25x more expensive than retaining an existing customer.
* **Revenue Protection:** Prevents recurring revenue losses from high-margin subscription accounts.
* **Proactive Interventions:** Allows marketing teams to issue targeted retention offers before customers formally leave.

---

### Q8. What are the advantages and limitations of the Decision Tree algorithm?
**Answer:**
* **Advantages:**
  * High interpretability; decision rules can be easily visualized and explained.
  * Requires minimal data preprocessing (handles numerical and categorical features naturally).
  * Non-parametric; makes no strict assumptions about underlying data distributions.
* **Limitations:**
  * Highly prone to overfitting if not properly pruned.
  * Unstable; small changes in input data can yield vastly different tree structures.
  * Can struggle with complex non-linear relationships compared to gradient boosting.

---

### Q9. Mention three real-world applications of Decision Tree Classification other than customer churn prediction.
**Answer:**
1. **Banking & Credit Scoring:** Evaluating loan applicants as *High Risk* or *Low Risk*.
2. **Healthcare & Diagnosis:** Classifying medical test results to detect specific diseases.
3. **Cybersecurity:** Classifying incoming network traffic as *Legitimate* or *Malicious Intrusion*.

---

### Q10. How can the insights obtained from a churn prediction model help organizations improve customer retention and business profitability?
**Answer:**
* **Targeted Incentives:** Identifies high-churn risk segments to send customized discount vouchers or loyalty extensions rather than blanket promotions.
* **Product Enhancements:** Reveals key churn drivers (e.g., month-to-month contracts or lack of tech support), allowing business teams to optimize product tiers and improve user onboarding.
* **Maximizing Customer Lifetime Value (CLV):** Extends average account lifespan, driving sustainable profit margins.
