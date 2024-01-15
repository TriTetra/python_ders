
import random

# -> boş bir dict oluşturduk 
studenDictionary = {}

numSchool = str(random.randint(1, 150)) # -> Random schoolID
print("Öğrenci numaraniz : "+numSchool)

# -> Öğrenci bilgilerini input olarak alıyoruz
name = str(input("İsminizi giriniz : "))
surname = str(input("Soyadinizi giriniz : "))
phone = str(input("Telefon numaranizi giriniz : "))

# -> Her yeni öğrencilerin bütün bilgilerini dicte giriyoruz
studenDictionary[numSchool] = {
    'ad': name,
    'soyad': surname,
    'phone': phone
}

numSchool = str(random.randint(1, 150)) # -> Random schoolID
print("Öğrenci numaraniz : "+numSchool)
# -> Öğrenci bilgilerini input olarak alıyoruz
name = str(input("İsminizi giriniz : "))
surname = str(input("Soyadinizi giriniz : "))
phone = str(input("Telefon numaranizi giriniz : "))

# -> Her yeni öğrencilerin bütün bilgilerini dicte giriyoruz
studenDictionary[numSchool] = {
    'ad': name,
    'soyad': surname,
    'phone': phone
}

numSchool = str(random.randint(1, 150))# -> Random schoolID
print("Öğrenci numaraniz : "+numSchool)
# -> Öğrenci bilgilerini input olarak alıyoruz
name = str(input("İsminizi giriniz : "))
surname = str(input("Soyadinizi giriniz : "))
phone = str(input("Telefon numaranizi giriniz : "))

# -> Her yeni öğrencilerin bütün bilgilerini dicte giriyoruz
studenDictionary[numSchool] = {
    'ad': name,
    'soyad': surname,
    'phone': phone
}

# -> Eklediğimiz öğrencilerin dict e bilgilerini varsa görüntülüyoruz yoksa bulunamadi sonucunu çıkarıyoruz.
selectStudent = str(input("Görünlüemek istediğiniz öğrencinin numarasini girin : "))
if selectStudent in studenDictionary:
    student = studenDictionary[selectStudent]
    print("ismi {} | soyadi {} | telefonu {}".format(student['ad'],student['soyad'],student['phone']))
else:
    print("Bulunamadi")    