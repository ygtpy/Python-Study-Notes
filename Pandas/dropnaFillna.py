
import pandas as pd


url = "http://bit.ly/uforeports"


data = pd.read_csv(url)



# print(data.shape)
data = data.dropna() # satirlarda bozuk, okunmayan veri varsa o satiri siler
data = data.dropna(how = "any") # herhangi bir satirda NaN degeri varsa siler
data = data.dropna(how = "all") # tum satirlarin NaN olmasi gerekir aksi halde sonuc degismez

data = data.dropna(subset=['City','Colors Reported'],how = "all")
# yukarida .dropna fonksiyonu ile bos,bozuk veri silme ornegi var
# subset=[] ile bos veri bulunan satirlari silmek istedigimiz kolonu secebiliriz

# how = 'all' ile bir satirdaki 'City' ve 'Colors Reported' verisi yoksa siler ( all = 'hepsi)
# how = "any" bir satirda 'City' veya 'Colors Reported' verisi yoksa siler ( any = 'herhangi)


data['Shape Reported'].fillna(value= "BELİRSİZ",inplace=True)
# burada Sahpe Reportedin icindeki NaN verileri doldurmamizi saglar yani value ile belirledigimiz isimi koyar
# inplace = True ise bellekte de degistirir

print(data["Shape Reported"].value_counts(dropna=False)) # dropna = False / boş(NaN) olanlari silmeden goster demek
# value_counts()= shape reported cesitleri ve karsisisnda sayisiyle gosterir















print(data.shape) # kac tane data old. gosterir






