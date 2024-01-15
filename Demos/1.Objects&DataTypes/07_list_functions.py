names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]

# 1 - "Cenk" ismini listenin sonuna ekleyiniz
names.append("Cenk")

# 2 - "Sena" değerini listenin başına ekleyiniz
names.insert(0,"Sena")

# 3 - "Deniz" isminin indeksi nedir ? 
index = names.index("Deniz")

# 4 - "Deniz" ismini listeden siliniz
names.remove("Deniz") 

# 5 - "Ali" listenin bir elemanı mıdır ? 
result = "Ali" in names

# 6 - Liste elemanlarını ters çevirin
names.reverse()

# 7 - Liste elemanlarını Alfabetik olarak sıralayınız
names.sort()

# 8 - years listesini rakamsal büyüklüğe göre sıralayınız 
years.sort()

# 9 - str = "Chevroler,Dacia" karakter dizisini listeye çeviriniz
str = "Chevrolet, Dacia"
result = str.split(",")

# 10 - years dizisinin en büyük ve en küçük elmanı nedir ?
min = min(years)
max = max(years)

# 11 - years dizisinde kaç tane 1998 değeri vardır ? 
result = years.count(1998)

# 12 - years dizisinin tüm elemanlarını siliniz 
years.clear()

# 13 - Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız
markalar = []
marka = input("Marka ismi giriniz : ")
markalar.append(marka)
marka = input("Marka ismi giriniz : ")
markalar.append(marka)
marka = input("Marka ismi giriniz : ")
markalar.append(marka)
print(markalar)
