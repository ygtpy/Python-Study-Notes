
import pandas as pd

# join = iki farkli datanin belli kolonlara kriterlere gore bir araya getirilmesidir
# genellikle iliskisel sistemlerde goruruz


data1 = {
            'id':[1,2,3,4],
            'ad':["Ayşe","Hatice","Fatma","Mehmet"],
            'soyad':["x","x","x","x"]
        }

data2 = {
            "id":[1,3,4,7],
            "ad":["Yiğit","Zeynep","merve","mehmet"],
            "soyad":["x","x","x","x"]
        }

data1df = pd.DataFrame(data1,index=[1,2,3,4])
data2df = pd.DataFrame(data2,index=[1,2,3,4])


print(data1df)
print("")
print(data2df)
print("")


# pd.merge fonksiyonu kullanilir
print(pd.merge(data1df, data2df,on="id",how="inner"))
print("")
# "inner" = iki tabloda da (on='id') sine gore olan verileri birlestirir

print(pd.merge(data1df, data2df,on='id',how='left'))
print("")
# "left" = data1 de olan ve data2 de olmayan 'id'leri birlestirir yani data1 de 1,2,3,4 indexler var bunlari yazar data2 de 2 olmadigi icin onun karsiligi NaN dir
# sadece data1 deki id'ler yazilir

print(pd.merge(data1df, data2df,on="id",how="right"))

# "right" = data2 de olan 'id'leri getirir data1 ile birlestirir bazi datalar ortak olmadigi icin (örn:3 ve 7) onlarin karsiligi NaN dir
# sadece data2 deki id'ler yazilir



# örn bir alısveris sitesinde sitene uye olan ama hic urun almayan musterileri bulmak icin left veya right kullanabilirsin 
# ve filitreleme secenekleri ile urun almayanari bulabilirsin



