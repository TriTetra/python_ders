
# 1 - Girilen 2 sayıdan hangsisi büyüktür ? 

numOne = int(input("ilk sayiyi giriniz : "))
numTwo = int(input("İkinci sayiyi giriniz : "))

if numOne > numTwo:
    print("{} Büyüktür".format(numOne))
else:
    print("{} Büyüktür".format(numTwo))    

# 2 - Kullanıcıdan vize (%60) ve final (%40) notunu alıp ortalamasını hesaplayınız.
#     eğer ortalama 50 ve üstüyse geçti değilse kaldı yazınız.

vize = float(input("Vize sonucunuzu giriniz : "))
final = float(input("Final sonucunuzu giriniz : "))

vize *= 0.60
final *= 0.40
result = vize+final
if result >= 50:
    print("Geçtiniz : {}".format(result))
else:
    print("Kaldiniz : {}".format(result))

# 3 - Girilen bir sayının tek mi çift mi olduğunu yazınız.

number = int(input("Değer girini :"))

if number%2==0:
    print("Bu sayi çifttir")
else:
    print("Bu sayi tektir")    

# 4 - Girlien bir sayının negatif veya pozitif durumunu yazınız.

number = int(input("Değer girinz : "))

if number < 0:
    print("Negatif sayilar ")
else:
    print("Pozitif sayilar")    

# 5 - Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#     (email : email@sadikturan.com parola : abc123)

email = str(input("E-mail : "))
password = str(input("Password : "))

if email == 'email@sadikturan.com' and password == 'abc123':
    print("Hoş geldiniz..")
else:
    print("Yanliş giriş yapriniz")    
    
