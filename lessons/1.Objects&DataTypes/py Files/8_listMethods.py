
# https://www.w3schools.com/python/python_lists_methods.asp

number = [1,10,4,17,11,9,10]
letters = ['a','g','n','m','ç','z']

value = min(number)   # -> listenin en küçük elemanını getirir
value = max(number)   # -> listenin en büyük elemanını getirir
print(value)
value = min(letters)  # -> listenin en küçük rakamsal karşılığa gelen harfini seçer
value = max(letters)  # -> listenin en büyük rakamsal karşılığa gelen harfini seçer
print(value)

value = number[3:]    # -> listenin 3.indexin sonuna kadarki değerleri getirir
value = letters[:4]   # -> listenin başından 4.indexine kadarki değerleri getirir
value = number[1:-1:2]  # -> [başlangıç index : gideceği index : nasıl ilerleyeceği] 
print(value)

number[4] = 40  # -> istediğimiz indexi çağırarak değiştirebiliriz
print(number)
letters[2] = 10 # -> listeler türe göre ayrılmadığı için içine her tür değişken atabiliriz
print(letters)

number.append(100)  # -> .append(değişken) metodu listenin sonuna yeni değeri ekler
print(number)
letters.insert(2,'Merhaba') # -> .insert(değişecek index , yeni değişken) şeklinde çalışır
print(letters)

number.pop()  # -> .pop(index) metodu ile istenilen index silinir  

number.sort() # -> .sort() metodu istenilen listenin içindeki değerleri sıralar
number.reverse() # -> .reverse() metodu büyükten küçüğe sıralar
print(number)

print(number.count(10)) # -> .count(değer) metodu istenilen değeri listenin içinde kaç defa olduğunu arar