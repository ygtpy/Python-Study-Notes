import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("positions.csv")

print(data.columns)

# x
level = data.iloc[:,[1]].values.reshape(-1,1)
# y
salary = data.iloc[:,[2]].values.reshape(-1,1)


regression = LinearRegression()
regression.fit(level, salary)

tahmin = regression.predict(np.array(8.3).reshape(-1, 1))

#%% polynom modeli kullanarak tahmini daha dogru alabiliriz
regressionPoly = PolynomialFeatures(degree = 4)
# degree=4 hassasiyet derecesi

levelPoly = regressionPoly.fit_transform(level)
# veriyi polynom modeline donusturme

regression2 = LinearRegression()
regression2.fit(levelPoly, salary)

tahmin2 = regression2.predict(regressionPoly.fit_transform(8.3))

#%%
plt.scatter(level, salary, color="red")
plt.plot(level,regression.predict(level),color = "blue")
# tahmini artis cizgisi cizer

# plt.plot(level, regression2.predict(levelPoly))

plt.show()
# plt. ile tahmini gorsellestiriyoruz

