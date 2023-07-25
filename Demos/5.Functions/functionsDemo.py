# 1 - Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

word = str(input("Enter the word : "))
cycle = int(input("How many time do want to write it : "))

for i in range(cycle):
    print(word)

# 2 - Kendine gönderilen sınırsız sayıdaki parametreyi listeye çeviren fonksiyon yazınız.

list = []
isContinue = True

while(isContinue):
    values = input("Enter the value : ")
    if values == 'Exit':
        isContinue = False
    else:
        list.append(values)

print(list)        

# 3 - Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

def isPrime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0 :
            return False
    return True     

def findPrime(start,end):
    primNumber = []
    for num in range(start,end+1):
        if isPrime(num):
            primNumber.append(num)
    return primNumber

startNumber = int(input("Başlandgiç sayinizi giriniz : "))          
endNumber = int(input("Bitiş sayinizi giriniz : "))
primeList = findPrime(startNumber,endNumber)

print(primeList)


# 4 - Kendisine gönderilen bir sahyının tam bölenlerini bir liste şeklinde döndüren liste.



