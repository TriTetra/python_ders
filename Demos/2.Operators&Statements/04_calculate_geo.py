geometri = input("İstediğiniz şekli seçiniz\n üçgen\n kare\nseçiniz : ")

if(geometri == "kare"):
    koşe1 = int(input("1.Köşe sayisi girin:"))
    koşe2 = int(input("2.Köşe sayisi girin:"))
    koşe3 = int(input("3.Köşe sayisi girin:"))
    koşe4 = int(input("4.Köşe sayisi girin:"))
    if(koşe1 == koşe2 == koşe3 == koşe4):
        print("Karedir")
    elif(koşe1 == koşe2 and koşe3 == koşe4):
        print("Dikdörtgen")
    elif(koşe3 == koşe1 and koşe4 == koşe2):
        print("Dikdörgen")
    else:
        print("Dörtgen")
        
elif(geometri == "üçgen"):
    koşe1 = int(input("1.Köşe sayisi girin:"))
    koşe2 = int(input("2.Köşe sayisi girin:"))
    koşe3 = int(input("3.Köşe sayisi girin:"))
    if ( abs(koşe1+koşe2) > koşe3 and abs(koşe1+koşe3) > koşe2 and abs(koşe2+koşe3) > koşe1):
        if (koşe1 == koşe2 and koşe1 == koşe3 ):
            print("Eşkenar Üçgen...")
        elif ((koşe1 == koşe2 and koşe1 != koşe3) or (koşe1 == koşe3 and koşe1 != koşe2) or (koşe2 == koşe3 and koşe2 != koşe1)):
            print("İkizkenar Üçgen....")
        else:
            print("Çeşitkenar Üçgen...")
    else:
        print("Üçgen belirtmiyor...")

else:
    print("Geçersiz Şekil...")
