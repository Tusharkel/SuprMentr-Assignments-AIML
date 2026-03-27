'''
Assignment Name : Customer Segmentation
Description : Perform K-Means clustering on a mall dataset and describe customer groups.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
df = pd.read_csv("mall_customers.csv")
features = ["Age", "Annual_Income_k$", "Spending_Score"]
X_scaled = StandardScaler().fit_transform(df[features])
inertia, sil = [], []
for k in range(2, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertia.append(km.inertia_)
    sil.append(silhouette_score(X_scaled, km.labels_))
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(range(2, 11), inertia, 'bo-')
axes[0].set_title("Elbow Method")
axes[0].set_xlabel("K")
axes[0].set_ylabel("Inertia")
axes[1].plot(range(2, 11), sil, 'gs-')
axes[1].set_title("Silhouette Score")
axes[1].set_xlabel("K")
plt.tight_layout()
plt.savefig("elbow.png", dpi=150)
plt.show()
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)
means = df.groupby("Cluster")[["Annual_Income_k$", "Spending_Score"]].mean()
sorted_idx = means.sort_values(["Spending_Score", "Annual_Income_k$"]).index
labels = dict(zip(sorted_idx, ["Low-Income Low-Spenders", "Wealthy Conservatives","Average Customers", "Young Budget Shoppers", "Premium Loyal Shoppers"]))
df["Segment"] = df["Cluster"].map(labels)
COLORS = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6']
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Customer Segmentation (K-Means, K=5)", fontweight='bold')
for c in range(5):
    m = df["Cluster"] == c
    axes[0].scatter(df[m]["Annual_Income_k$"], df[m]["Spending_Score"], c=COLORS[c], s=60, alpha=0.7, label=labels[c])
    axes[1].scatter(df[m]["Age"], df[m]["Spending_Score"], c=COLORS[c], s=60, alpha=0.7, label=labels[c])
for ax, xlabel in zip(axes, ["Annual Income (k$)", "Age"]):
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Spending Score")
    ax.legend(fontsize=7)
plt.show()