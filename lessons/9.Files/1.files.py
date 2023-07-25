
# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi, dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amçla açtığımızı berlirtir.

# 'w': (Write) yazma modu. Dosyayi konumda oluşturur.
#    ** Dosyayı konumda oluşturur.
#    ** Dosya içeriğini siler ve yeniden ekleme yapar.

file = open('newFile.txt','w',encoding='utf-8')
file.write("Hello, World")
file.close

# 'a': (Append) ekleme. Dosya konumda yoksa oluşturur.

file = open('newFile.txt','a',encoding='utf-8')
file.write("Hello, World")
file.close

# 'x': (Create) oluşturma. Dosya zaten varsa hata verir.

file = open('newFile2.txt','x',encoding='utf-8')

# 'r': (Okuma) okuma. varsayılan. dosya konumda yoksa hata verir.

