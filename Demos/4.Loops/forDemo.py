sayilar =[1,3,5,7,9,12,19,21]

# 1 - Sayılar listesindeki hangi sayılar 3'ün katıdır.

for say in sayilar:
    if (say%3==0):
        print(say)
  

# 2 - Sayılar listesindeki sayıların toplamı kaçtır ?

result = 0
for topla in sayilar:
    result += topla
print("Sayıların toplamı : {}".format(result))    

# 3 - Sayılar listesindeki tek sayıların karesini alınız 

for kati in sayilar:
    if (kati%2==1):
        power =kati*kati
        print(power) 
     

sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]

# 4 - Şehirlerden hangileri en fazla 5 karakterlidir ? 

for sehir in sehirler:
    if(len(sehir) <= 5):
        print(sehir)


urunler = [
    {"name":"Samsung S6","Price":"3000"},
    {"name":"Samsung S7","Price":"4000"},
    {"name":"Samsung S8","Price":"5000"},
    {"name":"Samsung S9","Price":"6000"},
]

# 5 - Ürünlerin fiyatları toplamı nedir ?

total = 0
for urun in urunler:
    price = int(urun("Price"))
    total +=price
print(total)    