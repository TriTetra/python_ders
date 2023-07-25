website = "https://www.sadikturan.com"
course = "Python kursu : Baştan sona python programlama rehberi (40 saat)"

"""
1- 'course' karakter dizinin de kaç karakter bulunmaktadır ?
2- 'website' içinden www karakterlerini alın
3- 'website' içinden com karakterlerini alın
4- 'course' içinden ilk 15 ve son 15 karakterlerini alın
5- 'course' ifadesindeki karakterleri tersten yazdırın
"""

print(len(course))    # First
print(website[8:11])  # Second
print(website[23:26]) # Third

head = course[:14]
tail = course[-15:]
print(head +" -- "+ tail) # Fourth

reverse = course[::-1]
print(reverse)            # Fifth

name,surname,age,job = "Bora","Yılmaz",32,"Mühendis"

"""
6- Yukarıdaki verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın
   'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim Mühendis.'
7- 'Hello world' ifadesindeki w harfini W olarak değiştirin.
8- 'abc' ifadesini yan yana 3 defa yazdırın   
"""
print("Benim adım {} {}, Yaşım {} ve mesleğim {}".format(name,surname,age,job)) 

word = "Hello world!"
print(word[0:6]+" W"+word[-5:])

multipleWord = "abc"*3
print(multipleWord)

