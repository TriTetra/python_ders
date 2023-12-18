'''
    Daire Alani   : πr^2
    Daire Çevresi : 2πr

    * Yari çapi verilen bir dairenin alan ve çevresini hesaplayiniz.. (π: 3.14)

'''

yariCap = int(input("Dairenin yari çapini giriniz : "))

daireAlan = 3.14*yariCap**2
daireCevre = 2*3.14*yariCap

print(type(daireAlan))
print(type(daireCevre))

print("Daire Alani Türü: {}, Daire Cevresi Türü: {}".format(type(daireAlan),type(daireCevre)))

print(daireAlan)
print(daireCevre)