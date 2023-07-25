
with open('newFile.txt','r+', encoding='utf-8') as file:  # -> with ile dosyayı açtığımızda close.dosya gibi metot gerekmez
    file.seek(20)            # -> seek(değer) metodu ile cursor u istediğimiz indexe taşıyabiliriz
    file.write('deneme')     # -> ve o indeğer write(değer) metotu ile o indexe bu değeri yazdırabiliriz

with open('newFile.txt', 'r+', encoding='utf-8') as file:
    print(file.read())  # -> file ı okuyoruz içindekileri index olarak ama line olarak değil


with open('newFile.txt','a',encoding='utf-8') as file:  # -> a file yani append dosyanın sonuna istenilen değeri yazdırır
    file.write('\n Emel Turan')   


# **************** Sayfa başında güncelleme *********************

with open('textFile.txt','r+',encoding='utf-8') as file:
    content = file.read()  # -> file ın içindeki değerlerin hepsini contente eşitledik
    content = 'Efe Turan\n' + content   # -> contentin başına değeri ekledik ve contente tekrar eşitledik
    file.seek(0)   # -> seek() metodu ile cursor u file ın en başına yani 0.index ine gönderdik
    file.write(content)  # -> 0.indexten başlayarak istenilen değeri yazdırdık


with open('newFile.txt', 'r', encoding='utf-8') as file:
    print(file.readlines())