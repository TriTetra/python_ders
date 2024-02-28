
onlar = ["","On","Yirmi","Otuz","Kirk","Elli","Altmiş","Yetmiş","Seksen","Doksan"]
birler = ["","Bir","İki","Üç","Dört","Beş","Alti","Yedi","Sekiz","Dokuz"]


def check_number():
    number = input("Sayi giriniz: ")

    if(len(number) == 2):
        number = int(number)
        ilk_sayi = number % 10
        ikinci_sayi = number // 10
        return print("{} {}".format(onlar[ikinci_sayi],birler[ilk_sayi]))
        


print(check_number())


    