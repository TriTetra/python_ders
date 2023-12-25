
# https://www.w3schools.com/python/python_sets.asp

fruits = {'apple' , 'orange' , 'lemon'}  # -> Örnek olarak bir set

# -> Setler index şeklinde çalışmaz içindeki veriler karışık olarak kayır edilir

fruits.add('grape')  # -> .add(değer) ile istenilen sete değer atabiliriz
fruits.update(['banana' , 'tomato']) # -> .update([değer]) ile de aynı şekilde eklenebilir

fruits.remove('orange') # -> .remove(değer) metodu ile set içindeki bir değeri silebiliriz
fruits.discard('apple') # -> .discard(değer) metodu ile set içindeki değerleri silebiliriz

fruits.pop() # -> Liste veya setin sonundaki değeri siler ya da daha doğrusu bir ileriye kaydırır

for x in fruits:
    print(x)         # -> for döngüsü ile setin içindeki değerleri yazdırıyoruz


mySet = {1,2,3,4,2,3,1,5,6,1,2}  # -> Örnek olarak set aynı zamanda aynı değerleri tutmaz 
print(mySet)   

myList = [1,2,3,4,5,6,1,2,3]  # -> Normal listeler aynı olsada değerler saklar
print(myList)
