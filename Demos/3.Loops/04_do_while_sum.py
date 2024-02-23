isContinue = True
sum = 0

while(isContinue):
    check_str = input("işlemi sonlandirmak için q basin\nşuana kadar toplanan sayi = {}\nSayi giriniz :".format(sum))
    if(check_str == "q"):
        isContinue = False
    else:
        check_str = int(check_str)
        sum += check_str
