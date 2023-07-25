
# https://www.w3schools.com/python/python_operators.asp

x = 5
y = 7
z = 9
 # -> Yukarıdaki gibi arama yapılabilir ama python kolaylık olsun diye
x, y, z = 1,2,3  # -> şeklinde de atama yapabilmemizi sağlar ama kodun okunmasını zorlaştırabilir () olmadan da çalışır
print(x,y,z)

x , y = y , x  # -> şeklinde de değerlerin değiştirebiliriz
print(x,y)


x = x +5  # -> x in son değerine 5 ekle ve x e tekrar eşitle demek oluyor uzun şekilde 
x += 5  # -> Bu örnek x e direkt 5 veya istenilen değeri ekle şeklinde çalışıyor (çoğunlukla bu yöntem kullanılır)
x -= 5
x /= 5
x *= 5
x %= 5
x **=5 # -> Görüldüğü üzere her matematiksel ifadeler kullanılabilir


values = 1,2,3  # -> Tuple () ihtiyacımız yok ama okunabilirlik için önemli () lar
print(type(values))  

x,y,z = values # -> tuple içindeki değerleri değişkenler bu şekilde de atayabiliriz ama sayıları eşit olmalı


