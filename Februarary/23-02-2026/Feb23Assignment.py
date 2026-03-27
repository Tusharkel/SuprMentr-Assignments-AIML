'''
Docstring for assignment.ipynb

Task 1: Car Price Prediction (Multiple Features)

Dataset features:

Engine Size

Mileage

Age

Price

Steps:

Create DataFrame

Train model

Predict price for:

Engine = 1500

Mileage = 20

Age = 3

Print coefficients

Interpret which feature impacts price most

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as ply
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
data={
    "Engine_Size":[1000, 1500, 2000, 1200, 1800, 2200, 1300, 2500],
    "Mileage":[50, 30, 20, 70, 25, 15, 60, 10],
    "Age":[8, 5, 3, 10, 4, 2, 7, 1],
    "Price":[3, 6, 9, 2, 8, 11, 4, 13]
}
df=pd.DataFrame(data)
model=LinearRegression()
x=df[["Engine_Size","Mileage","Age"]]
y=df["Price"]
model.fit(x,y)
new_car=[[1500,20,3]]
print("Predicted_car:",model.predict(new_car))
print(model.coef_)
#Engine Size has a positive impact on car price, meaning that as engine size increases, 
# the price of the car also increases. Mileage has a negative impact on price, 
# which means that cars with higher mileage tend to have lower prices. Age also has a negative 
# impact on price, and its coefficient has the largest absolute value among all features. 
# Therefore, Age affects the car price the most, indicating that as a car becomes older, 
# its price decreases significantly compared to the impact of the other features.
