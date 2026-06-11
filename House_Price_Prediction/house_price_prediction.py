
import pandas as pd

from sklearn.linear_model import LinearRegression

data = {
    "size" : [1000,1200,1500,1800,2000],
    "price" : [10,12,15,18,20]
}

df = pd.DataFrame(data)

X = df[["size"]]
y = df["price"]

model = LinearRegression()
model.fit(X,y)

prediction = model.predict([[2500]])
print(prediction)