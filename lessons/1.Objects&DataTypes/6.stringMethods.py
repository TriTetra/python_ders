
# https://www.w3schools.com/python/python_strings_methods.asp

message =  "Hello There. My name is Sadik Turan"


message = message.upper() # -> upper() metodu belirtilen değişkenin değerlerini büyütür (Hepsini)
print(message)

message = message.lower() # -> lower() metodu belirtilen değişkenin değerlerini küçültür (Hepsini)
print(message)

message = message.title() # -> title() metodu belirtilen değişkenin kelimelerin baş harflerini büyütür (Hepsini)
print(message)

message = message.capitalize() # -> capitalize() metodu belirtilen değişkenin en başındaki harfi büyütür
print(message)

message = message.strip() # -> strip() metodu belirtilen değişkenin en başındaki ve sonundaki boşluğu siler
print(message)

message = message.split() # -> split() metodu belirtilen değişkenin her kelimesini ayırır ve dizi gibi çıkarır
print(message)
print(message[0])
print(message[-1])

message = ' '.join(message) # -> .joing(değişken) değişkenin kelimelerini birleştirir ve araya istenilen str leri koyar
print(message)

message = message.split('.') # -> split() metodunun içine girilen değerden başlayaran diziye çevirir
print(message)

message = '-'.join(message) # -> .joing(değişken) değişkenin kelimelerini birleştirir ve araya istenilen str leri koyar
print(message)

index = message.find('sadik') # -> .find(aranmasını istenilen kelime) cümle içinde istenilen var mı bakar varda indexini verir
print(index)

isFound = message.startswith('H') # -> .startswith(değer) değerin değişkenin başında mı değil mi bakar
print(isFound)

isFound = message.endswith('.') # -> .endswith(değer) değerin değişkenin sonunda mı değil mi bakar
print(isFound)

message = message.replace("sadik","change") # -> .replace(değer) içindeki değeri istenilen ile değiştirir
print(message)

message = message.center(100,'*') # -> .center(istenilen boşluk) istenilen kadar boşluk bırakır başına ve sonuna ve değeri ekler
print(message)
