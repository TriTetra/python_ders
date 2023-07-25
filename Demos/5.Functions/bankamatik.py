
# Bankamatik Uygulaması

hesapA ={
    'ad' : 'Sadik Turan',
    'hesapNo': '13245678',
    'bakiye' : '3000',
    'ekHesap' : '2000'
}

hesapB ={
    'ad' : 'Ali Turan',
    'hesapNo': '13245612',
    'bakiye' : '2000',
    'ekHesap' : '1000'
}

bankList = [hesapA,hesapB]
bankAccount = None
isContinue = True


def selectProcess():
    while isContinue:
        message = ' Akarlar bankasina hoş geldiniz '
        message = message.center(120,'*')
        print(message)
        bankProcess()


def bankProcess():
    
    bankID = input("Hesap numaranizi giriniz : ")
    for hesap in bankList:
        if hesap['hesapNo'] == bankID:
            bankAccount = hesap
            break

    
    if bankAccount:
        print("Hoş geldiniz {}".format(bankAccount))
    else:
        print("Account is not found")     

    paraCek(bankAccount)              


def paraCek(account):
    money = int(account['bakiye'])
    withdraw = int(input("Ne kadar para çekeceksiniz : "))

    if money >= withdraw:
        money -= withdraw
        print("Başarili bir şekilde para çekilmiştir")
        print("Çekilen {}  | Kalan {}".format(withdraw,money))
    else:
        print("Yeterli bakiyeniz bulunmamaktadir")   

 
selectProcess()