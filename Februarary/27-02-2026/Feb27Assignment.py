'''
Today's Task
Use:

from sklearn.datasets import load_breast_cancer

Steps:

Train KNN classifier

Try different K values (1–15)

Plot Accuracy vs K

Try Euclidean vs Manhattan

Compare results

Explain why accuracy changes with K.
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

data = load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

k_values           = list(range(1, 16))
accuracy_euclidean = []
accuracy_manhattan = []

for k in k_values:
    model_euc = KNeighborsClassifier(n_neighbors=k, metric="euclidean")
    model_euc.fit(X_train, y_train)
    accuracy_euclidean.append(round(accuracy_score(y_test, model_euc.predict(X_test)), 4))

    model_man = KNeighborsClassifier(n_neighbors=k, metric="manhattan")
    model_man.fit(X_train, y_train)
    accuracy_manhattan.append(round(accuracy_score(y_test, model_man.predict(X_test)), 4))

print("K\tEuclidean\tManhattan")
print("-" * 35)
for k, euc, man in zip(k_values, accuracy_euclidean, accuracy_manhattan):
    print(f"{k}\t{euc}\t\t{man}")

best_k_euc = k_values[accuracy_euclidean.index(max(accuracy_euclidean))]
best_k_man = k_values[accuracy_manhattan.index(max(accuracy_manhattan))]
print(f"\nBest K (Euclidean): {best_k_euc} → Accuracy: {max(accuracy_euclidean)}")
print(f"Best K (Manhattan): {best_k_man} → Accuracy: {max(accuracy_manhattan)}")

x     = np.arange(len(k_values))
width = 0.4

plt.figure(figsize=(12, 5))
plt.bar(x - width/2, accuracy_euclidean, width, label="Euclidean", color="#4e79a7")
plt.bar(x + width/2, accuracy_manhattan, width, label="Manhattan", color="#e15759")

plt.xticks(x, [f"K={k}" for k in k_values], rotation=45)
plt.ylim(0.85, 1.02)
plt.xlabel("K Value")
plt.ylabel("Accuracy")
plt.title("Accuracy vs K  —  Euclidean vs Manhattan")
plt.legend()
plt.tight_layout()
plt.show()

print("""
Why accuracy changes with K:

K=1   → overfits → memorizes training data → unstable
K=1-3 → high variance → sensitive to noise
K=5-9 → balanced → usually best accuracy
K=10+ → underfits → misses local patterns

Euclidean vs Manhattan:
Euclidean → straight-line distance → sensitive to large differences
Manhattan → sum of absolute gaps  → robust against outliers
Both perform similarly here because StandardScaler was applied.
""")