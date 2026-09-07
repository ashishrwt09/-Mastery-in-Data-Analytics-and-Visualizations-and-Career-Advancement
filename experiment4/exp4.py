# ==============================================================================
# STEP 1 & 2: Select Dataset & Import Required Libraries
# Selected Dataset: Superstore Sales Dataset (Synthetic fallback provided)
# ==============================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for Seaborn plots
sns.set_theme(style="whitegrid")

# Load Dataset
try:
    df = pd.read_csv('superstore_sales.csv')
    print("Dataset successfully loaded!")
except FileNotFoundError:
    print("Dataset file not found! Generating sample Superstore Sales dataset...")
    np.random.seed(42)
    n = 300
    dates = pd.date_range(start="2023-01-01", periods=n, freq="D")
    df = pd.DataFrame({
        'Date': dates,
        'Region': np.random.choice(['East', 'West', 'Central', 'South'], size=n),
        'Category': np.random.choice(['Technology', 'Furniture', 'Office Supplies'], size=n),
        'Sales': np.random.exponential(scale=200, size=n) + 10,
        'Profit': np.random.normal(loc=50, scale=30, size=n),
        'Discount': np.random.choice([0.0, 0.1, 0.2, 0.3], size=n)
    })

# ==============================================================================
# STEP 3: Bar Chart (Sales by Region / Category)
# ==============================================================================
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Region', y='Sales', estimator=sum, ci=None, palette='viridis')
plt.title('Total Sales by Region', fontsize=14, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.tight_layout()
plt.show()

# ==============================================================================
# STEP 4: Line Chart (Trends over time)
# ==============================================================================
df_monthly = df.set_index('Date').resample('M')['Sales'].sum().reset_index()

plt.figure(figsize=(10, 5))
plt.plot(df_monthly['Date'], df_monthly['Sales'], marker='o', color='b', linewidth=2)
plt.title('Monthly Sales Trend Over Time', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Monthly Sales ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================================================================
# STEP 5: Histogram (Distribution of numerical variable)
# ==============================================================================
plt.figure(figsize=(8, 5))
sns.histplot(df['Sales'], kde=True, bins=30, color='teal')
plt.title('Distribution of Sales Values', fontsize=14, fontweight='bold')
plt.xlabel('Sales Value ($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.show()

# ==============================================================================
# STEP 6: Box Plot (Identify outliers & compare across categories)
# ==============================================================================
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Category', y='Sales', palette='Set2')
plt.title('Sales Distribution & Outliers by Product Category', fontsize=14, fontweight='bold')
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.tight_layout()
plt.show()

# ==============================================================================
# STEP 7: Scatter Plot (Relationship between two numerical variables)
# ==============================================================================
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Sales', y='Profit', hue='Category', style='Category', s=70)
plt.title('Relationship Between Sales and Profit', fontsize=14, fontweight='bold')
plt.xlabel('Sales ($)', fontsize=12)
plt.ylabel('Profit ($)', fontsize=12)
plt.tight_layout()
plt.show()

# ==============================================================================
# STEP 8 & 9: Correlation Heatmap & Customization
# ==============================================================================
plt.figure(figsize=(6, 4))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Numerical Features', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()