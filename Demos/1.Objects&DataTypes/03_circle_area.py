# Ternimalden input ile int değerinde aldığımız değerleri *yariCap* değişkenine atıyoruz

yariCap = int(input("Dairenin yari çapini giriniz : "))
print(yariCap)

# Aldığımız değeri *daireAlan* ve *daireCevre* için hesaplamalarda kullanıyoruz ve sonucu .format() yardımıyla sırayla ekrana yazdırıyoruz

daireAlan = 3.14 * yariCap**2
daireCevre = 2 * 3.14 * yariCap
print("Daire Alani: {}, Daire Cevresi: {}".format(daireAlan,daireCevre))

# İstersek sonuç değerlerin hangi tür bir değişken olduğunu da ekrana çıktı olarak yansıtabiliriz

print("Daire Alani Türü: {}, Daire Cevresi Türü: {}".format(type(daireAlan),type(daireCevre)))