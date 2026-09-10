import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 1. GENERATE DATASET (Mall Customer Segmentation)
np.random.seed(42)
n_samples = 200

data = {
    'CustomerID': range(1, n_samples + 1),
    'Age': np.random.randint(18, 70, n_samples),
    'Annual_Income_k$': np.random.randint(15, 140, n_samples),
    'Spending_Score': np.random.randint(1, 100, n_samples)
}

df = pd.DataFrame(data)
df.to_csv('mall_customers.csv', index=False)

# 2. FEATURE SELECTION & SCALING
X = df[['Annual_Income_k$', 'Spending_Score']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. ELBOW METHOD & SILHOUETTE SCORE
wcss = []
silhouette_scores = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# 4. TRAIN K-MEANS WITH OPTIMAL K=5
optimal_k = 5
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# 5. DISPLAY RESULTS & METRICS
print("=" * 55)
print("   EXPERIMENT 7: K-MEANS CUSTOMER SEGMENTATION   ")
print("=" * 55)
print(f"Optimal Clusters Selected (K) : {optimal_k}")
print(f"Silhouette Score (K={optimal_k})       : {silhouette_scores[optimal_k-2]:.4f}\n")

print("--- CLUSTER CHARACTERISTICS (MEAN VALUES) ---")
cluster_summary = df.groupby('Cluster').agg(
    Avg_Age=('Age', 'mean'),
    Avg_Income=('Annual_Income_k$', 'mean'),
    Avg_Spending_Score=('Spending_Score', 'mean'),
    Customer_Count=('CustomerID', 'count')
).reset_index()

print(cluster_summary.to_string(index=False))
print("\n[SUCCESS] Customer Segmentation completed & saved to 'mall_customers.csv'!")