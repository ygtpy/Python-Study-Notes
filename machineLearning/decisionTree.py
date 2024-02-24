import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("positions.csv")


level = data.iloc[:,1].values.reshape(-1,1) # data.iloc ile indexi 1 olan veri sutununu cektik reshape ile düzenledik
salary = data.iloc[:,2].values.reshape(-1,1)


regression = DecisionTreeRegressor()

regression.fit(level, salary)

print(regression.predict(np.array(8.5).reshape(-1, 1)))

plt.scatter(level, salary, color = "red")
x = np.arange(min(level), max(level),0.01)
plt.plot(x, regression.predict(np.array(x).reshape(-1, 1)), color ='orange')
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Decision Tree Model")
plt.show()


#(np.array(8.5).reshape(-1, 1)