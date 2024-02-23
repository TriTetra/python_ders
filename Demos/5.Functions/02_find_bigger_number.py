

# Java adı metoto python adı da fonksiyonlar 
# BU fonksiyonun görevi sayıları userdan almak ve döndürmek
def take_numbers():
    first_number  = int(input("İlk sayiyi giriniz : "))
    second_number = int(input("İkinci sayiyi giriniz :"))
    return first_number,second_number

# Bu fonksiyonun görevi aldiği sayiların ebobunu bulmak
def find_bigger():
    a ,b = take_numbers()
    min_number = min(a,b)
    list = []
    
    # Burada for ile ortak bölenleri buluyoruz ve liste atıyoruz
    for x in range(1,min_number+1):
        y = x
        if (a % x == 0 and b % y == 0):
            if (x == y):
                list.append(x)
    
    return list
    
# Listemizin içindeki en büyük sayıyı buluyoruz oda bizim Ebobumuz oluyor
final = find_bigger()



if final:
    print("En büyük ortak bölen : ", max(final))
else:
    print("Ortak bölen bulunamadi..")

    

