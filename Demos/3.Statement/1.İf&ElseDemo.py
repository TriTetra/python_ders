# 1 - Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. 
#     Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

name = input("Adınızı giriniz :")
age = int(input("Yaşınızı giriniz : "))
education = int(input("Eğitim seviyenisi sayı olarak giriniz :"))

if (age>=18) & (education>12):
    print("{} Ehliyet alabilirsiniz.".format(name))
else:
    print("{} Ehliyet almazsınız.".format(name))

# 2 - Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık 
#     gelen not bilgisini yazdırın.
#     0  - 24  => 0
#     25 - 44  => 1
#     45 - 54  => 2
#     55 - 69  => 3
#     70 - 84  => 4
#     85 - 100 => 5     

firstExam = int(input("1.Yazılı Puanı : "))
secondExam = int(input("2.Yazılı Puanı : "))
project = int(input("Sözlü puanı giriniz : "))

result = (firstExam+secondExam+project)/3

if (0<=result) and (result<24):
    print("0")
elif (24<=result) and (result <44):
    print("1")
elif (44<=result) and (result <54):
    print("2")
elif (54<=result) and (result <69):
    print("3")
elif (70<=result) and (result <84):
    print("4")
elif (84<=result) and (result <=100):
    print("5")
else:
    print("Hatalı giriş yaptınız")    
