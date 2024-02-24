
import pandas as pd

films = pd.read_csv("imdb-1000 .csv")

print(films.head()) # ilk 5 veriyi gösterir

print(films.columns) # kolonlari goserir

print(films.star_rating.mean()) # ortalama hesaplar
print("         ")

print(films.groupby('genre').star_rating.mean()) # films'ten genre(tür) leri alir ve rating ortalamalarini hesaplar

