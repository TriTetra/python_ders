

try:       # -> try-exept blokları ile oluşabilecek errorların önünü alıyoruz
    file = open('newFile2.txt','r')  # -> Read türünde bir file oluşturuyoruz
except FileNotFoundError:
    print('Dosya bulundamadi.')
finally:
    print('Dosya kapatildi.')        # -> finally metodunu ekleyerek sonuç ne olursa olsun dosya işlemleri kapatıyoruz
    file.close


file = open('newFile.txt','r',  encoding='utf-8')

# -> dosyanın içindeki verileri okumak istediğimizde for döngüsü ile bu işlemleri yapabliriz

for i in file:
    print(i,end='\n')
file.close    

# -> read() fonksiyonu ile dosya içeriğini olduğu gibi de okuyabiliriz
file = open('newFile.txt','r',  encoding='utf-8')

content = file.read()  # -> read(len) len değeri vererek kaç karakter okuması gerektiğini bildirebiliriz..
print(content)

contentLine = file.readline()  # -> readline() ile satır satır okumasını da sağlayabilriz
print(contentLine)





