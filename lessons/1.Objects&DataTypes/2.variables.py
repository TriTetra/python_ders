
# https://www.w3schools.com/python/python_variables.asp

# Değer atılmayı plananlanan değişken her zaman sağa yazılır
# KeySensitive 

maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli -(maasAli*vergi))
print(maasAhmet - (maasAhmet*vergi))

# Değişken Tanımlama Kuralları

# Rakam ile Başlayamaz
# Türkçe değer kullanılamaz
 
x = 1                 # int
y = 2.4               # float
name = "Çinar"        # str
isStudent = True      # bool

x,y,name,isStudent = (1,4.2,"Mehmet",False)  # -> Tekte birden fazla atama yapılabilir



a = '10'
b = '20'
print(a+b)  # =>1020
# toplanan değerlerin türü str olduğu için toplama yapmaz birleştirme yapar

firstName = 'Sadik'
lastName = ' Turan'
print(firstName+lastName)


