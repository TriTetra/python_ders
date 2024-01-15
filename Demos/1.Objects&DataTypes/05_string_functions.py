website = "https://www.sadikturan.com"
website1 = "www.sadikturan.com"
course = "Python kursu : Baştan sona python programlama rehberi (40 saat)"


result = " Hello World ".strip() # -> strip() ile cümlenin baş ve sondaki boşlukları siliyoruz
print(result)


result = website1.strip("w.com") # -> strip(x) x yerine cümlenin içinde bulunan karakterleri siler 
print(result)


result = course.lower() # -> lower() hedef cümlenin bütün karakterlerini küçültür
print(result)


result = website.count("a") # -> count(x) hedef cümlenin içinde kaç adet x olduğunu sayar
print(result)


head = website1.startswith("www") # -> startwith(x), hedef cümlenin x ile başlayıp başlamadığını kontrol eder
tail = website.endswith("com") # -> endwith(x), hedef cümlenin x ile bitip bitmediğini kontrol eder
print("başlangiç {}, bitiş {}".format(head,tail))


result = website.find(".com")  # -> find(x), hedef cümle içinde x olup olmadığını kontrol eder
print(result)



result = course.isalpha() # -> 'course' içindeki karakterlerin hepsi alfabetik mi ? (isAlpha, isDigit)
print(result)


result = "Contents".center(50,"*")# -> 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekler
print(result)


result = course.replace(" ","-")# -> 'course'  karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirir
print(result)
