
# https://www.w3schools.com/python/python_casting.asp

# Değişkenlere sistemin en başında türünü bildirmezsen str olarak kabul eder.

x = input("1.Sayi : ")
y = input("2.Sayi : ")

toplam = x+y  # -> xy
print(type(toplam))
print(toplam)

# Her değeri tek tek istenen türe dönüştürülmesi gerekir

toplam = int(x) + int(y)
print(type(toplam))  # -> x+y
print(toplam)


x = 7                 # int
y = 9.4               # float
name = "Sadik"        # str
isStudent = True      # bool

print(type(x)) 
print(type(y)) 
print(type(name)) 
print(type(isStudent)) 

# Type Conversion ile değerin türünü istediğimize çevirebiliriz bazı durumlar haricinde

x = float(x)  # -> baştaki türü int şuanki türü float
print(x)
print(type(x))

y = int(y)    # -> baştaki türü float şuanki türü int
print(y)
print(type(y))