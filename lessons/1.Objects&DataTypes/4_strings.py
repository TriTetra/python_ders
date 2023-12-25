
# https://www.w3schools.com/python/python_strings.asp

#  str türündeki değeri  '' veya "" içine yazabiliriz

name = 'Sadik'
surname = "Turan"
age = 36


# -> Hata vermesinin nedeni int değeri topluyor olarak algılamasıdır str olarak girilmesi gerekiyor arada int değer kullanilacaksa
# print("My name is "+ name +" Surname "+ surname +" Age " + age + "years old.") 

print("My name is "+ name +" Surname "+ surname +" Age " + str(age) + "years old.")  # -> Bu şekilde çalışır

age = '36'
print("My name is "+ name +" Surname "+ surname +" Age " + age + "years old.") # -> Bu şekilde çalışır

meeting = "My name is "+ name +" Surname "+ surname +" Age " + age + "years old."
print(meeting)  # -> Bu şekilde çalışır



# STRING INDEXLEMEK

print(meeting[0])  # -> değişkenin istenen indexindeki veriyi çağırır
print(meeting[6])

print(len(meeting)) # -> değişkenin kaç adet indexe sahio olduğunu gösterir

length = len(meeting)
print(meeting[length-1]) # -> length meeting toplam indexini alır ve dizi içine koyarak 1 çıkarınca son indexine ulaşırız hızlıca
print(meeting[-1]) # -> Bu da aynı zamanda hızlıca son indexi çağırır

print(meeting[2:5]) # -> 2.index ten 5.index e kadar çağırır
print(meeting[:13]) # Baştan başlar ve 13.index e kadar çağırı
print(meeting[7:])  # 7.index ten başlar ve sona kadar çağırır 

print(meeting[2:40:2]) # -> 2.index ten 40.index e kadar 2 şer atlayarak çağırır