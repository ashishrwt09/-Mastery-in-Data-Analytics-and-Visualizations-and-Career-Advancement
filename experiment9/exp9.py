import pandas as pd
import numpy as np

# 1. GENERATE SYNTHETIC GLOBAL SUPERSTORE SALES DATASET
np.random.seed(42)
n_samples = 300

categories = ['Technology', 'Office Supplies', 'Furniture']
regions = ['North', 'South', 'East', 'West']

data = {
    'OrderID': range(1001, 1001 + n_samples),
    'Category': np.random.choice(categories, n_samples, p=[0.4, 0.4, 0.2]),
    'Region': np.random.choice(regions, n_samples),
    'Sales': np.random.uniform(50, 1500, n_samples).round(2),
    'Discount': np.random.choice([0.0, 0.1, 0.2, 0.3, 0.5], n_samples, p=[0.3, 0.3, 0.2, 0.1, 0.1])
}

df = pd.DataFrame(data)

# Calculate Profit
def calculate_profit(row):
    base_margin = 0.25 if row['Category'] == 'Technology' else (0.15 if row['Category'] == 'Office Supplies' else 0.05)
    margin = base_margin - (row['Discount'] * 0.8)
    return round(row['Sales'] * margin, 2)

df['Profit'] = df.apply(calculate_profit, axis=1)

# Save output dataset CSV
df.to_csv('superstore_storytelling_data.csv', index=False)

# 2. KPI COMPUTATION
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
overall_margin = (total_profit / total_sales) * 100
avg_discount = df['Discount'].mean() * 100

print("=" * 60)
print("  EXPERIMENT 9: DATA STORYTELLING & BUSINESS INSIGHTS  ")
print("=" * 60)
print("--- KEY PERFORMANCE INDICATORS (KPIs) ---")
print(f"Total Revenue (Sales) : ${total_sales:,.2f}")
print(f"Total Net Profit       : ${total_profit:,.2f}")
print(f"Overall Profit Margin  : {overall_margin:.2f}%")
print(f"Average Discount Rate  : {avg_discount:.2f}%\n")

# 3. NARRATIVE BREAKDOWN BY CATEGORY
print("--- CATEGORY PERFORMANCE BREAKDOWN ---")
cat_summary = df.groupby('Category').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Avg_Discount=('Discount', 'mean')
).reset_index()

cat_summary['Profit_Margin_%'] = (cat_summary['Total_Profit'] / cat_summary['Total_Sales']) * 100
print(cat_summary.to_string(index=False))

print("\n--- BUSINESS STORYTELLING NARRATIVE ---")
print("1. Insight  : Technology is driving the highest total profit margins due to lower discount dependencies.")
print("2. Challenge: High discount rates (>=30%) in Furniture/Office Supplies lead to negative profit margins.")
print("3. Action   : Cap promotional discounts at 20% to safeguard profit margins without dropping sales volume.")

print("\n[SUCCESS] Storytelling analysis complete & saved to 'superstore_storytelling_data.csv'!")