"""

1 - Bir müşterinin aşağıdaki bilgileri için değişken oluşturnuz

Müşteri adı
Müşteri soyadı
Müşteri ad + soyad
Müşteri cinsiyeti
Müşteri tc kimlik
Müşteri doğum yılı
Müşteri adres bilgisi
Müşteri yaşı 

"""

musteriAdi = "Muhammed"
musteriSoyadi = "Yakup"
print(musteriAdi+" "+musteriSoyadi)

musteriCinsiyeti = "Erkek"
musteriTC = "5423657851142"
musteriDogum = "1984"
musteriAdres = "Güngören / İstanbul"
musteriYas = "39"
print("Cinsiyet : "+musteriCinsiyeti+" TC : "+musteriTC+" Dogum Tarihi : "+ musteriDogum +" Adres : "+musteriAdres+" Yaşı : "+musteriYas)

"""

2 - Aşağıdaki siparişlerin toplam bilgisinin hesaplayınız

Sipariş 1 => 110      TL
Sipariş 2 => 1100.5   TL
Sipariş 3 => 356.95   TL 

"""
order1 = 110
order2 = 1100.5
order3 = 365.95

total = order1+order2+order3
print(total)