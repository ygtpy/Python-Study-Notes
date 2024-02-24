
import pandas as pd

orders = pd.read_table("orders.tsv")

print(orders.head())
print(orders.columns)

print(orders.shape)

orders.item_name = orders.item_name.str.upper()
print(orders.item_name)
# butun item_name leri .upper() fonksiyonu ile buyuk harf yazdirdik

print(orders.item_name.str.contains('Chicken'.upper()))
# contain ile veri icinde arama yapabiliriz
# buyuk kucuk harf duyarliligi olmadigi icin .upper() veya .lower() fonksiyonlariylaveri aramasi yapabiliriz

orders.choice_description = orders.choice_description.str.replace('[','').str.replace(']','')
# bu sekilde veriyi esitleyerek kalici deisim yapariz

# str etiketiyle string fonksiyonlarini kullanabiliriz
# replace eskiyi yeniyle degistirmemizi saglar




# bu orneklerdeki gibi bir cok string fonksiyonunu data duzenlerken kullanabiliriz



