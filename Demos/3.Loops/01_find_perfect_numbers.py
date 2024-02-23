number = int(input("Sayi giriniz :"))
result = 0

for x in range(1,number):
    remain = number % x
    if(remain == 0):
        print(x)
        result += x

if(result == number):
    print("Mükemmel sayidir değerler : {} = {}".format(number,result))
else:
    print("Mükemmel sayi değildir sonuç: ",result)

