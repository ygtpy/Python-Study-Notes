
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("positions.csv")
level = data.iloc[:,1].values.reshape(-1,1)
salary = data.iloc[:,2].values
regression = RandomForestRegressor(n_estimators=100)# kac tane decisionTree olusturayım = 5 tane dedik # estimator arttıkca gercekcilik artar
# regression = RandomForestRegressor(n_estimators=100, random_state=0) # yaparsak aynı algoritmayı calıstırır
regression.fit(level, salary)


print(regression.predict(np.array(8.3).reshape(-1,1)))


# bu algoritma daha gercekci tahminsel veri ogrenme tipidir