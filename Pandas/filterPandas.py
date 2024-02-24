
import pandas as pd

films = pd.read_csv("imdb-1000 .csv")

print(films)
print(films.columns) # kolon basliklarini gosterir

print(films.head())
print(films.tail())

print(films[["title","star_rating"]].head())
# print(films.title.head()) # ikisi de ayni
# films verisinin icinden title vr star rating yazar

print(films[:9][["title","star_rating"]])
# tum filmlerden 9 a kdar olanlarin title ve star ratinglerini yazar

print(films[
    (films["star_rating"]>=8.5)&(films["star_rating"]<=9.0)
            ][["title","star_rating"]])
#filmlerde rating'i 8.5 dan buyuk olan ve 9.0 dan kucuk esit
# olanlarin title ve star rating lerini yazar

print(films[(films["star_rating"]>=9.5) | (films["star_rating"]<=8.0)
            ][["title","star_rating"]])
# filmlerde rating'i 9.5 dan buyuk esit
# veya 8.0 den kucuk esit olanlarin title ve star rating leri yaz




