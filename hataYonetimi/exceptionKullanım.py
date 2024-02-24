

#try = dene demek
# hatayı yönetirsek uygulama kesintiye girmeden devam eder
try:
    sayi = int(input("SAYI GİR = "))
    
    
# except = hata olursa ne yapayım demek    
except ValueError:
    print("Tip Uyuşmazlığı")
    
# birden fazla hata icin kullanim    
except (ValueError,ZeroDivisionError):
    print("hata")
    
    
except:
    print("Bir Hata Oluştu")
    
    
    
print("devam")