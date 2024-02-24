
import pandas as pd

films = pd.read_csv("imdb-1000 .csv")

# print(films.columns)


films = films.drop("content_rating",axis=1)# silmek icin axis = sutun secer 
films = films.drop("actors_list",axis=1)
# films.drop("content_rating",axis=0) silmek icin axis=0 satir secer

films = films.drop(975,axis=0) # filmlerde indexi 975 olan satiri siler

rowsToDrop = [0,1,2,3,4,5]
films = films.drop(rowsToDrop,axis=0) # filmler belirlediğimiz toplu index listesine gore siler

print(films.star_rating.mean())# rating(puan) ortalamasini alir

print(films.groupby("genre").star_rating.mean()) # films'ten genre(tür) leri alir ve rating ortalamalarini hesaplar
 





