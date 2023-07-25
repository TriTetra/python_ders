'''
    1-100 arasinda rastgele uretilecek bir sayiyi asagi yukari ifadeleri ile buldurmaya calisin.
    ** "Random Modülü" için "Python Random" şeklinde arama yapin.
    ** 100 üzerinden puanlama yapin. Her soru 20 puan.
    ** Hak bilgisini kullanicidan alin  ve her soru belirtiler can sayisi üzerinden hesaplansin.
'''

import random


randomNumber = random.randint(1,100)

valueCycle = int(input("Enter Cycle number : "))

i = 0
while i < valueCycle:
    i += 1
    value = int(input("Guess the Number : "))
    
    if 100 < value & value < 1:
        print("Please enter between 1 - 100")
        continue

    difference = abs(randomNumber - value)

    if difference == 0:
        print("Congrat your the man who im looking for..")
    elif difference <= 5:
        print("So Hot")
    elif difference <= 10:
        print("Hot")
    elif difference <= 20:
        print("Warm")
    elif difference <= 35:
        print("Cold")
    else:
        print("So Cold")       

    if i == valueCycle:
        print("Good Game ")                  

    


