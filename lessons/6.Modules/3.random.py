
import random

# result = dir(random)   -> Bu şekilde random modülünün içindeki metotları görebiliriz 
# result = help(random)  -> Metotların ayrıntılarını görebiliyoruz

value = random.random()  # -> range belirlemedik rastgele noktalardan sayı seçiyor
value = random.randint(1,100) # -> int değerlerden rastgele bir sayı seçecektir a ve b arasında
value = random.uniform(1,10)  # -> float şeklinde a ve b arasında rastgele noktadan sayı seçecektir
print(value)

names = ['ali','mehmet','ayse','fatmagül','zehra']
result = random.choice(names) # -> bir liste ya da bir den fazla değer içeren nesnelerin içinden ratgele bir değer seçer
print(result)
