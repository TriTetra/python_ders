
'''
ogrenciler = {
    '120' : {
        'ad' : 'Ali',
        'soyad' : 'Yilmaz',
        'telefon' : '532 000 00 01'
    },
    '125' : {
        'ad' : 'Can',
        'soyad' : 'Korkmaz',
        'telefon' : '532 000 00 02'
    },
    '128' : {
        'ad' : 'Volkan',
        'soyad' : 'Yükselen',
        'telefon' : '532 000 00 03'
    }
}

 1 - Bilgileri verilen öğrencileri kullanicidan aldiğiniz bilgilerle
     dictionary içinde saklayiniz.

 2 - Öğrenci numarasini kullanicidan alip ilgili öğrenci bilgisini gösterin      

'''

import random

studenDictionary = {}

numSchool = str(random.randint(1, 150))
print("Öğrenci numaraniz : "+numSchool)
name = str(input("İsminizi giriniz : "))
surname = str(input("Soyadinizi giriniz : "))
phone = str(input("Telefon numaranizi giriniz : "))

studenDictionary[numSchool] = {
    'ad': name,
    'soyad': surname,
    'phone': phone
}

numSchool = str(random.randint(1, 150))
print("Öğrenci numaraniz : "+numSchool)
name = str(input("İsminizi giriniz : "))
surname = str(input("Soyadinizi giriniz : "))
phone = str(input("Telefon numaranizi giriniz : "))

studenDictionary[numSchool] = {
    'ad': name,
    'soyad': surname,
    'phone': phone
}

numSchool = str(random.randint(1, 150))
print("Öğrenci numaraniz : "+numSchool)
name = str(input("İsminizi giriniz : "))
surname = str(input("Soyadinizi giriniz : "))
phone = str(input("Telefon numaranizi giriniz : "))

studenDictionary[numSchool] = {
    'ad': name,
    'soyad': surname,
    'phone': phone
}

selectStudent = str(input("Görünlüemek istediğiniz öğrencinin numarasini girin : "))
if selectStudent in studenDictionary:
    student = studenDictionary[selectStudent]
    print("ismi {} | soyadi {} | telefonu {}".format(student['ad'],student['soyad'],student['phone']))
else:
    print("Bulunamadi")    