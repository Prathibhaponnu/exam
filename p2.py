import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv("customer_data.csv")
x=dataset.iloc[:6,3:]
y=dataset.iloc[6:12,3:]
print(x)
print(y)
plt.xlabel("Annual income")
plt.ylabel("Spending score")
plt.scatter(x,y,color="green")
plt.show()

