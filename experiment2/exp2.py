import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Load Dataset
try:
    df = pd.read_csv('netflix_titles.csv')
    print("Dataset successfully loaded!")
except FileNotFoundError:
    print("Dataset file not found! Generating sample Netflix dataset...")
    np.random.seed(42)
    n = 300
    df = pd.DataFrame({
        'type': np.random.choice(['Movie', 'TV Show'], size=n, p=[0.7, 0.3]),
        'release_year': np.random.randint(2000, 2024, size=n),
        'duration_num': np.random.exponential(scale=30, size=n) + 40,
        'rating': np.random.choice(['TV-MA', 'TV-14', 'TV-PG', 'R', 'PG-13'], size=n),
        'country': np.random.choice(['United States', 'India', 'United Kingdom', 'Canada'], size=n)
    })

# Summary
print("\n--- DATASET INFORMATION ---")
print(df.info())

# Plot 1: Histogram
plt.figure(figsize=(8, 5))
sns.histplot(df['release_year'], kde=True, bins=20, color='crimson')
plt.title('Distribution of Release Years', fontsize=14, fontweight='bold')
plt.xlabel('Release Year', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.tight_layout()
plt.show()

# Plot 2: Countplot with Hue fix
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='rating', hue='rating', palette='Set2', order=df['rating'].value_counts().index, legend=False)
plt.title('Content Count by Rating', fontsize=14, fontweight='bold')
plt.xlabel('Rating', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.tight_layout()
plt.show()

# Plot 3: Boxplot with Hue fix
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='type', y='duration_num', hue='type', palette='Set3', legend=False)
plt.title('Duration Distribution by Content Type', fontsize=14, fontweight='bold')
plt.xlabel('Content Type', fontsize=12)
plt.ylabel('Duration', fontsize=12)
plt.tight_layout()
plt.show()
