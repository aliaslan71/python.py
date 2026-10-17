def ort_hesaplama(v,f):
    O=v*0.4 + f*0.6
    return O
while True:
    v=int(input("Vize notunuzu giriniz:"))
    f=int(input("Final notunuzu giriniz:"))

    O=ort_hesaplama(v,f)

    if O >= 85:
        print("Geçme notunuz:",ort_hesaplama(v,f),"(AA)" )
    elif O >= 70:
        print("Geçme notunuz:",ort_hesaplama(v,f),"(BB)")
    elif O >= 50:
        print("Geçme notunuz",ort_hesaplama(v,f),"(CC)")
    else:
        print(ort_hesaplama(v,f),"ile kaldınız:( (FF)")
    print("\n")