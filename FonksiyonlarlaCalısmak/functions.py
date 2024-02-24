# def fonksiyonu yanında verilen değeri tutar ve kullanım kolaylığı sağlar
# parantez içindeki parametreleri ister
# altında ne kadar kod varsa çalıştırır


def selamVer(isim):
    print("Hoş Geldin " + isim)
    
    
selamVer("yiğit")   
#%%
# default değer verirsek değer girmeden te çalışır

def selamVer2(isim = "Ziyaretçi" ):
    print("Hoş Geldin " + isim)
    
selamVer2()   
#%% 
# görüldüğü üzre birden fazla parametre tanımlayabilirim 
# default parametre de tanımlanır
# en sonda selmaVer3() parantezin içine girilen değerler tanımlanan parametlerein sırasına karşılık gelir 
# virgül "," ile ayırarakbirden fazla parametre tanımlanabilir girilebilir
# örn = isim parametresinin karşılığı ("yiğit ali"
# soyİsim parametresinin karşılığı ise , "sunal") şeklinde yazılır.

def selamVer3(isim, soyİsim = "sucuk"):
    print("Hoş Geldin " + isim+" "+soyİsim)
    
selamVer3("yigit ali")