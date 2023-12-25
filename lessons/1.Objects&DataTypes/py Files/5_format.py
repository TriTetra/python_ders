
# https://www.w3schools.com/python/python_strings_format.asp

# Java'nın aksine uzun bir satır kod yerine format adında komuta değişkenleri index olarak atar ve kullanır

name = "Çinar"
surname = "Turan"

# '.format' bize print metodunun içine koyduğumuz süslü parantezin yerine ne getireceğimizi
# hem kısaltmış hemde kolay bir şekilde yerleştirmemizi sağlar. 
print("My name is {} {}".format(name,surname))    # -> Sırayla çalıştırır sırası önemlidir
print("My name is {1} {0}".format(name,surname))  # -> Bu şekilde değişken değerle sıralarını değiştirebiliriz
print("My name is {n} {m}".format(n=name,m=surname)) # -> Değerlere göre de sıralamaları yapabilriz


result = 200/1000
print("the result is {}".format(result))