
# class

class Person:
    # class attributes
    address = 'no information'
    # constructor (yapıcı)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        print('init metodu çalişti')

    # instance methods
    def intro(self):
        print('Hello there, I am '+ self.name)

    def calculate(self):
        return 2023 - self.year 
    



# object (instance) 
p1 = Person('Kadirov',2001)
p2 = Person('Ali',2004) 

p1.intro()
p2.intro()
 
print(f'adim : {p1.name}  yaşim : {p1.calculate()}')
print(f'adim : {p2.name}  yaşim : {p2.calculate()}')


class Circle:
    # Class object attributes
    pi = 3.14

    # constructor (yapıcı)
    def __init__(self,yaricap=1):
        self.yaricap = yaricap

    # Methods
    def cevre_hesapla(self):
        return 2*self.pi *self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)
    

c1 = Circle() 
c2 = Circle(5)

print(f' c1 : alan = {c1.alan_hesapla()}  çevre = {c1.cevre_hesapla()}')
print(f' c1 : alan = {c2.alan_hesapla()}  çevre = {c2.cevre_hesapla()}')

        

