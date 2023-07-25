  
def sayHello():   # -> Java daki metot gibi ayrı bir metotlar çağırıldaıklarında çalışırlar.
    print("Hello")


def sayHell(name): # -> içine bir parametre vererek o parametler ile işlem yapan aksi halde çalışmayan metotlar
    print("Hello {}".format(name))


nameOf = str(input("Enter name : "))  # -> oluşturduğumuz metot içine verdiğimiz parametreyi belirledik
sayHell(nameOf)    



def total(num1, num2):  # -> Return lu bir metot oluşturduk sadece değer döndürecek
    return num1+num2

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print(total(num1,num2))  # -> aldığı değerlerin yapılmasını istendiği işlemelri yapar ve değeri dödürür


        