

import pandas as pd

filmler = pd.read_csv("imdb-1000 .csv")


print(filmler)


print(filmler.query("star_rating>=9.0 & star_rating <=9.2")
      [["title","star_rating"]])
# bu sekilde daha kolay filtreleme yapariz
# star ratingi 9 dan buyuk ve 9.2 den
# kucuk filmlerin title ve star_ rating'lerini yazar

