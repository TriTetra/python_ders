website = "https://www.sadikturan.com"
course = "Python kursu : Baştan sona python programlama rehberi (40 saat)"

# 1 - ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result = " Hello World ".strip()
print(result)
# 2 - 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
result = website.strip("h/tps:")
print(result)
# 3 - 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result = course.lower()
print(result)
# 4 - 'website' içinde kaç tane a karakteri vardır ? (count(a))
result = website.count("a")
print(result)
# 5 - 'website' www ile başlayıp com ile bitiyor mu ?
head = website.startswith("www")
tail = website.endswith("com")
print(head)
print(tail)
# 6 - 'website' içinde .com ifadesi var mı ?
result = website.find(".com")
print(result)
# 7 - 'course' içindeki karakterlerin hepsi alfabetik mi ? (isAlpha, isDigit)
result = course.isalpha()
print(result)
# 8 - 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz
result = "Contents".center(50,"*")
print(result)
# 9 - 'course'  karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin
result = course.replace(" ","-")
print(result)
