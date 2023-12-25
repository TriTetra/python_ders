
# https://www.w3schools.com/python/python_tuples.asp

list = [1,2,3]

tuple = 1, 'iki' ,3  # tuple listesi olıştururken parantezlere ihtiyaç duymaz ama okunurluk için kullanılır
tuple = (4,'beş',6)

print(type(list))  # -> liste türünden olduğunu görüyoruz
print(type(tuple)) # -> tuple türünde olduğunu görüyoruz aynılar burada

print(list[2])   # -> listenin istenilen indexindeki değeri çağırıyoruz
print(tuple[2])  # -> tuple dan istediğimiz değeri çağırıyoruz  aynılar burada

print(len(tuple))  # -> index toplamını görebiliyoruz
print(len(list))   # -> index toplamını görebiliyoruz aynışar burada

list = ['ali','veli']      
tuple = ('damlar','ayşe','ayşe')  

list[0] = 'deniz'     # -> list içinden index e göre eleman değişimine izin verir
# tuple[0] = 'ahmet'    # -> tuple indexten eleman değiştirmeye izin vermez

print(tuple.count('ayşe'))
print(tuple.index('ayşe'))

# tuple liste türü içindeki değerleri karışık olarak alır ve tam index olarak işlem yapamaz

print(list)
print(tuple)