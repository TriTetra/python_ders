
# error handling  => hata yönetimi

try:
    x = int(input('x :'))
    y = int(input('y :'))
    
except ZeroDivisionError:                   # -> y = 0 olduğu takdirde bilinmezlik hatasında ne yapacağını sisteme söylüyoruz
    print('payda 0 olamaz..')     
except ValueError:                          # -> int değere str veya farklı tür veri girildiğinde çalışacak 
    print('sayisal değer girmelisiniz..')     
except (ZeroDivisionError, ValueError):     # -> ya da birden fazla değerleri bu şekilde gruplayarak bildirebiliriz
    print('sistemde hata var')

# -> bir çok hata olabileceğini varsayıyorsak  sadece exept diyerek bütün hataları kapsamış oluruz.