'''
    Soru: Girilen bir sayinin asal olup olmadiğini bulun.
    ** Asal sayi 1 ve kendisi hariç tam böleni olmayan sayilara denir.
'''

number = int(input("Enter Number : "))

isPrime = True
if number < 2:
    print("Please enter correct number")

for i in range(2,number):
    if(number % i == 0):
        isPrime = False
        break

if isPrime:
    print("This number is prime")
else:
    print("This number is not prime")    