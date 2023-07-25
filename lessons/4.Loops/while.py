
# https://www.w3schools.com/python/python_while_loops.asp

# 1 - 100 kada sayıları tek tek yazmak istiyoruz diyelim for döngüsü ile uğraştırıcı olabilir
# ama while döngüsü ile daha kolay bir şekilde bütün elemanlarını tek tek yazdırabiliriz.

# while döngüsünde önemli nokta sonlandırabilmektir sonsuz döngüye sokmamaktır..

x = 0

'''
        while True:      # -> bu döngü sonuza kadar dönecektir çünkü nerede bitmesi gerektiğini söylemedik
          print(x)
'''    

while x < 100:           # -> ama burada nereye kadar dönmesi gerektiğini yani sınırını veriyoruz geriye oraya kadar 1 artması gerek
    x += 1               # -> o işlemi de bu satırdaki kod ile sağlıyoruz her döngü sıfılandığında x in değeri 1 artacak
    print(x)             # -> ve yazdırma aşaması istediğiniz değerin çıktısını her döngü görmek isterseniz


isName = True            # -> boolean türünde bir durum belirterek True ya da False durumlarıyla kodu bitirebiliriz
while isName:            # -> örnek olarak isName True olduğu sürece kod çalışacaktır 
    name = str(input("İsim giriniz : "))
    if name == 'merhaba':   # -> ama input merhaba olarak girilince while otomatik olarak duracaktır çünkü isName False olacak
        isName = False
    else:
        print(name)      # -> merhaba girilmediğinde de while son bulamaycak ve döngü devam edecektir
