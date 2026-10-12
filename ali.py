    # This is a test script
import random
gizlisayı = random.randint(1,100)

sayac=0
sayac+=1

while True:
    tahmin = int(input("Tahmin giriniz: "))
    if gizlisayı < tahmin:
        print("daha kucuk dene")
    elif gizlisayı > tahmin :
        print("daha buyuk dene")
    else :
        print("tebrikler [sayac] denemede buldunuz ")
        break


