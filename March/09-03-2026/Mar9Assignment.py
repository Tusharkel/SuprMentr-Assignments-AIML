'''
Assignment (09/03/2026)

Assignment Name : House Price Predictor
Description : Train a Linear Regression model, predict prices, and test with new input.
'''

import math

X_train = [[1500,3,10],[2000,4,5],[1200,2,20],[1800,3,8],[2500,5,3],[1000,2,30],[2200,4,7],[1600,3,12]]
y_train  = [300, 400, 200, 350, 500, 150, 430, 310]

def transpose(M):
    return [[M[r][c] for r in range(len(M))] for c in range(len(M[0]))]

def mat_mul(A, B):
    result = [[0.0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                result[i][j] += A[i][k] * B[k][j]
    return result

def gaussian_inverse(M):
    n = len(M)
    aug = [M[i][:] + [1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
    for col in range(n):
        max_row = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[max_row] = aug[max_row], aug[col]
        aug[col] = [x / aug[col][col] for x in aug[col]]
        for row in range(n):
            if row != col:
                f = aug[row][col]
                aug[row] = [aug[row][k] - f * aug[col][k] for k in range(2*n)]
    return [row[n:] for row in aug]

def train(X, y):
    X_b = [[1.0]+[float(v) for v in r] for r in X]
    Xt  = transpose(X_b)
    inv = gaussian_inverse(mat_mul(Xt, X_b))
    return [t[0] for t in mat_mul(inv, mat_mul(Xt, [[v] for v in y]))]

def predict(theta, x):
    return sum(t*xi for t,xi in zip(theta, [1.0]+[float(v) for v in x]))

theta = train(X_train, y_train)

print("Learned θ:")
for label, t in zip(["Bias","Size","Beds","Age"], theta):
    print(f"  {label:<6} → {t:+.4f}")

print("\nHouse     Actual    Predicted     Error")
total = 0
for i,(x,a) in enumerate(zip(X_train, y_train)):
    p = predict(theta, x)
    e = abs(a-p)
    total += e
    print(f"House {i+1}  ${a*1000:>7,}  ${p*1000:>9,.0f}  ${e*1000:>7,.0f}")
print(f"MAE → ${(total/len(y_train))*1000:,.0f}")

print("\nNew Predictions:")
for h in [[1700,3,9],[3000,5,1],[900,1,40]]:
    print(f"  {h[0]}sqft {h[1]}bed {h[2]}yrs → ${predict(theta,h)*1000:,.0f}")