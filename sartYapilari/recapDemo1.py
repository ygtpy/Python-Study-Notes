

lights = ["Red","Yellow","Green"]

currentLight = lights[2]
print(currentLight)

# tanımladığımız veri(currentLight) EĞER(if) red ise komutu uygular
if currentLight == "Red":
    print("STOP!")
 
# tanımladığımız veri(currentLight) EĞER(if) yellow ise komutu uygular   
if currentLight =="Yellow":
    print("READY!")

# tanımladığımız veri(currentLight) EĞER(if) green ise komutu uygular
if currentLight == "Green":
    print("GO!")
    
    
    
    
    
    
# if currentLight == "Red":
#     print("STOP!")
    

#yukarıdaki komut geçerli değilse ve tanımlanan veri yellow'a eşitse;
# elif currentLight =="Yellow":
#     print("READY!")


# yukarıdaki her iki komut gerçekleşmediğinde her halukarda gerçekleşecek dizin 
# else:
#     currentLight == "Green"
#     print("GO!")