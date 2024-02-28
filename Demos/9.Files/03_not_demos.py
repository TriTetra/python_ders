
isContinue = True


def notlariOku():
    try:
        with open('notlar.txt','r+',encoding='utf-8') as file:
           for satir in file:
               print(notHesaola(satir))
    except FileNotFoundError:
        print('Dosya Bulunmadi')



def notGir():
    try:
        ad = input('Öğrenci adi :')
        soyad = input('Öğrenci soyadi :')
        not1 = input('not 1 :')
        not2 = input('not 2 :')
        not3 = input('not 3 :')

        with open('notlar.txt','a',encoding='utf-8') as file:
            file.seek(0)
            file.write(ad+ ' '+soyad+':'+not1+','+not2+','+not3+'\n')
    except:   
        print('Bir hata oluştu..!') 


def notHesaola(satir):
    satir = satir[:-1]
    liste = satir.split(':')

    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1+not2+not3)/3

    if ortalama >= 90 and ortalama<=100:
        harf = 'AA'
    elif ortalama >=85 and ortalama <=89:
        harf = 'BA'
    elif ortalama >=65 and ortalama <=84:
        harf = 'BB'
    else:
        harf = 'CC'

    return ogrenciAdi + ' : '+ harf + ' -> '+ str(ortalama)+''



def processMain():
    global isContinue
    print('***********************************')
    process = int(input('1 - Notlari oku\n2 - Not gir\n3 - Notlari kaydet\n4 - Çikiş\n -> '))        
    if process == 1:
        notlariOku()
    elif process == 2:
        notGir()
    elif process == 3:
        pass
    elif process == 4:
        isContinue = False
    else:
        print('Hatali giriş yaptiniz..!')
  

while isContinue:
    processMain()