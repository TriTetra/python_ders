liste = ['1','2','5a','10b','abc','10','50']

# 1 - Liste elemanları içindeki sayısal değerleri bulunuz.

for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue    


# 2 - Kullanici 'q' değerini girmedikçe aldiğiniz her inputun sayi
# olduğundan emin olunuz aksi halde hata mesaji yazin.

isNumber = True
while isNumber:
    value = input('Enter value : ')
    if value == 'q':
         isNumber = False

    try:
        result = float(value)
    except :
        print('Sayisal bir değer giriniz..')
        continue


# 3 - Girilen parola içinde türkçe karakter hatası veriniz.

turkce_karakterler = 'şçöğüıİ'
parola = input('parola : ')

for i in parola:
    if i in turkce_karakterler:
        raise TypeError('Parola türkçe karakterler içeremez.')
    else:
        pass

print('geçerli parola '+ parola)    

# 4 - Faktöreiyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajlari verin.

