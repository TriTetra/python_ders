number = input("Sayi giriniz :")

number_length = len(number)

number = int(number)

gecici_sayi = number
toplam = 0

 
while gecici_sayi > 0:
    basamak = gecici_sayi % 10
    toplam += basamak ** number_length
    gecici_sayi //= 10



if toplam == number:
    print(f"{number} bir Armstrong sayidir.")
else:
    print(f"{number} bir Armstrong sayisi değildir.")
