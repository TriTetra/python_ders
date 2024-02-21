heigh = float(input("Boyunuzu giriniz (Örnek: 1.82) :"))
size = float(input("Kilonuzu giriniz (Örnek: 88) :"))

result = size / pow(heigh,2)

if(result < 18.5):
    print("Zayif")
elif(18.5 <= result and result <25):
    print("Normal")
elif(25 <= result and result <30):
    print("Fazla Kilolu")
else:
    print("Tekrar Kontrol Edin..")

print(result)