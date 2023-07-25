

# YÖNTEM 1
# -> Bu yöntem ile modüüleri import ettiğimizde sadece istediğimiz metotları çağırarak kullanabilriz
import math  # -> Şuanda aktif olarak python içinde bulunan bir kütüphane olan math i ekledik

# -> istersek modüllere takma yani istediğimiz kendi isimlerimizi verebiliriz kolaylık olsun diye
import random as salla

value = dir(math)  # -> Bu şekilde bu modülün içinde bulunan fonksiyonları görebiliriz
value = help(math) # -> Bu şekilde ise daha ayrıntılı şekilde inceleyebiliriz 

value = math.sqrt(49)
value = math.factorial(5)
value = math.floor(4.9)
value = math.ceil(4.7)


random = dir(salla) # -> Görüdğünüz gibi vermiş olduğumuz nick ile kullanıyoruz
random = help(salla)

print(random)
print(value)

# YÖNTEM 2 
# -> Bu yöntem ile modülün içindeki neredeyse tüm metotlara erişim sağlamış oluruz

from math import *  # -> artık math içindeki bütün metotlara erişimimiz bulunuyor

value = sqrt(49)
value = factorial(5)
value = floor(4.9)
value = ceil(4.7)
