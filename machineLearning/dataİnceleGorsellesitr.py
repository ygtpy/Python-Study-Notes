
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.read_csv("hw_25000.csv")
# verileri cektik

## x 
boy = data.Height.values.reshape(-1,1)
# boy adinda veri olusturup icine veriyi aktardik
# .reshape ile uygun bicime duzenledik (25000,1)


## y
kilo = data.Weight.values.reshape(-1,1)
# kilo adinda veri olusturup icine veriyi aktardik
# .reshape ile uygun bicime duzenledik (25000,1)


regression = LinearRegression()
regression.fit(boy,kilo)
# LinearRegression modulunu kullanarak elimizdeki boy ve kilo verilerini 
# orn: boy 1 birim arttığında diger kilo değişkeni ne kadar değişeceğini gösteren degeri yazar.

print(regression.predict(np.array([[60],[62],[64],[66],[69],[70]]).reshape(-1, 1)))
# .predict fonksiyonu ile degiskenleri tahmin ettiriyoruz orn: boy 70 iken kilo ortalama kac olabilir tahmin ediyor verileri kullanarak

print(data.columns)

plt.scatter(data.Height,data.Weight)
# 2 boyutlu verinin tablo icindeki dagılımlarını gosterir (nokta nokta )

x = np.arange(min(data.Height), max(data.Height)).reshape(-1, 1)
# diyoruz ki; her x degeri icin bana y nin karsiligini goster
plt.plot(x, regression.predict(x),color="red")
# bana line fit ciz yani her x degeri icin y degerini yahmin eden cizgiyi goster ve rengi red olsun

plt.xlabel("BOY (inc)")
plt.ylabel("KİLO (lb)")
# burada y ve x ekseninin isilerini duzenledik

plt.title("Simple Linear Regression Model")
# tabloya isim verdik (en ustte gozukur)

plt.show()
# grafigi cizdirmemizi saglar

print(r2_score(kilo, regression.predict(boy)))
# bu komut sayesinde algoritmamizin tahminin ne kadar sapmaya ugradigini gormus oluyoruz
# 1 e ne kdr yakinsa o kdr iyi demek oluyor




