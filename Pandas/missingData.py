
import pandas as pd

url = 'http://bit.ly/uforeports'

data = pd.read_csv(url)
# print(data)

# print(data.columns)
# print(data.head())

print(data[['City',
            'Colors Reported',
            'Shape Reported',
            'State',
            'Time']].head()) # time ve state kolunlarındn ilk bes veriyi getirir
# print(data['Time'].head()) # time kolonunun ilk bes satirini getirir

print(data.isnull().head(100)) # NaN(bos) olma durumunu soyler true = bos demek
print(data.notnull().head()) # dolu yani veri olanlari soyler / true = dolu

print(data.isnull().sum()) # bos olan satir sayilarini toplar kolonlarin yaninda gosterir
print(data.notnull().sum()) # dolu olan satirlarin sayisini toplar kolonlarin yaninda gosterir

print(data[data.City.isnull()])





