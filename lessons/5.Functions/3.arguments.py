
def changeName(n):  # -> metodu çağırarak direkt olarak değer değiştimek zor olur
    n = 'ada'


name = 'yiğit'

changeName(name)  # -> görüdüğünü gibi değişmedi
print(name)


def change(name):   # -> Referans ile değişim yapıyoruz daha hızlı ve kolay oluyor
    name[0] = 'istanbul'

sehirler = ['ankara','izmit']
change(sehirler)  
print(sehirler)  