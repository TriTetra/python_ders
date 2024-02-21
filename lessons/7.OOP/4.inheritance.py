
# Inheritance (Kalıtım): Miras alma

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print('Person created')

    def who_am_i(self):
        print('I am a Person')    

    def eat(self):
        print('I am eating')    
        


class Student(Person):
    def __init__(self, fname, lname, number):
        super().__init__(fname, lname)   
        self.number = number
        print('Student Created')     

    def who_am_i(self):
        print('I am a Student')

    def sayHello(self):
        print('Hello im a Student')    


class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname) 
        self.branch = branch     
        print('Teacher Created')  

    def who_am_i(self):
        print('I am a Teacher')    

    def whichBranch(self):
        print(f'Hello i am {t1.firstname} and my branch is {t1.branch}')    


p1 = Person('Ali','Yilmaz') 
s1 = Student('Çinar','Turan',1256)
t1 = Teacher('Muhammed','Ziya','Math101')

print(p1.firstname + ' ' + p1.lastname)
print(s1.firstname + ' ' + s1.lastname + ' ' + str(s1.number))
print(t1.firstname + ' ' + t1.lastname + ' ' + t1.branch)

p1.who_am_i()
s1.who_am_i()
s1.eat()
p1.eat()

s1.sayHello()
t1.whichBranch()