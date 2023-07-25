
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
        # methods


    # object methods


# object (instance) 
p1 = Person('Kadirov',2001)
p2 = Person('Ali',2004) 

# update
p1.name = 'Ahmet'
p2.year = 2014

p1.address = 'Kocaeli'

# accessing object attributes
print(f'name : {p1.name}  year {p1.year}  address: {p1.address}')
print(f'name : {p2.name}  year {p2.year}  address: {p2.address}')


print(p1)
print(p2)
print(type(p1))
print(type(p2))