website = "https://www.sadikturan.com"
course = "Python kursu : Baştan sona python programlama rehberi (40 saat)"

print(len(course))    # -> Kaç karakter olduğunu gösterecektir
print(website[8:11])  # -> Sadece www olan noktayı alacaktır
print(website[23:26]) # -> Sadece com olan noktayı alacaktır

head = course[:14] # -> Baştan 0.index to 14.index dahil olmak üzere hepsini okuyacak
tail = course[-15:] # -> Sonuncu indexten başlayarak sondan 15.index e kadar okuyacak
print(head +" -- "+ tail) # -> Sonuç

reverse = course[::-1] # -> Sondan başlayarak okuyacak
print(reverse) # -> Sonuç

name,surname,age,job = "Bora","Yilmaz",32,"Mühendis" # -> Bilgileri değişkenlere atayarak fomatladık
print("Benim adim {} {}, Yaşim {} ve mesleğim {}".format(name,surname,age,job)) # -> Sonuç

word = "Hello world!" # -> küçük 2 almayacak şekilde okuyarak onun yerine büyük W yerleştirebiliriz 
print(word[0:6]+" W"+word[-5:]) # -> Sonuç
print(word.title()) # -> title() fonksiyonu ile sadece baş harfleri büyültebiliriz.


multipleWord = "abc" * 3 # -> İstenilen sayıyı çoğaltmak istenilen sayı ile çarpabiliriz
print(multipleWord) # -> Sonuç

