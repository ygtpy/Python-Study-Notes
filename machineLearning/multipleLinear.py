# linear = doğrusal demek

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("insurance.csv")

print(data.columns)
print(data.describe()) # data hakkinda bilgi almak icin

# y ekseni
expenses = data.expenses.values.reshape(-1,1)


# x ekseni
ageBmis = data.iloc[:,[0,2]].values
# datanin icinden : = tüm veriler & 0 ve 2 inc ikolonu cektik ageBmis in icinde koyduk

regression = LinearRegression()
# bu sekilde kullanimi daha kolay
regression.fit(ageBmis, expenses)



print(regression.predict(np.array([[20,20],[20,21],[20,22],[20,23]])))
# bu sekilde makinemizi egitmis olduk 
# su anda age si ve bmi endexi verilen bir kisinin ortalama harcamalarini tahmin edebiliriz

