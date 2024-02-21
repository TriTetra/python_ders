sayilar = [1,3,5,7,9,12,19,21]

# 1 - saylar listesini while ile ekrana yazdırın.


i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i +=1


# 2 - Başlangıç ve bitiş değerlerini kullanıcıdan alıp arkadaki tüm tek sayıları ekrana yazdırın


start = int(input("Başlangıç değeri giriniz : "))
end = int(input("Bitiş değeri giriniz : "))

j = start
while j < end:
    j +=1
    print(j) 


# 3 - 1-100 arasındaki sayıları azalan şeklnde yazdırın


i = 100
while i != 1:
    i -=1


# 4 - kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın


numbers = []
read = int(input("Kaç adet sayı gireceksiniz : "))
while i != read+1:
    number = int(input("Sayı giriniz : "))
    numbers.append(number)
    i +=1
print(numbers)

# 5 - Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayın
# ** ürün sayısınıkullanıcıya sorun 
# ** dictionary listesi yapısı (name, price) şeklinde olsun.
# ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin

k = 0
products = []
go = int(input("Kaç adet ürün giriş yapacaksınız : "))
while k !=go:
    name = input("Ürün adı giriniz : ")
    price = input("Ürün fiyatı giriniz : ")
    products.append({
        "Ürün": name,
        "Fiyatı": price
    })
    k +=1;

for urun in products:
    print(f"Ürün adı : {urun['Ürün']} Ürün Fiyatı : {urun['Fiyatı']}")
    