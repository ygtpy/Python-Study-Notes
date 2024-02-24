

lights = ["Red","Yellow","Green","naber"]

currentLight = lights[3]
print(currentLight)

# EĞER(if) currentLight kırmızıya eşitse DUR! yazdır;
if currentLight == "Red":
    print("STOP!")
 
    
#yukarıdaki komut geçerli DEĞİLSE(elif) ve tanımlanan veri Yellow'a eşitse;
elif currentLight =="Yellow":
    print("READY!")
  
    
#yukarıdaki komut geçerli DEĞİLSE(elif) ve tanımlanan veri Green'e eşitse;
elif currentLight == "Green":
    print("GO!")
 
    
 # yukarıdaki komutlar gerçekleşmediğinde her halukarda gerçekleşecek dizin 
else:
    print("Not Avalible")