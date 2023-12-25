
# https://www.w3schools.com/python/python_lists.asp

message = "Hello There. My name is Sadik Turan"

myList = [1,2,3]
myList = ["bir",2,True,5.6]  # -> Farklı türlerde veriler listede saklanabilir
print(myList)

list1 = ['one','two','three']
list2 = ['four','five','six']

numbers = list1+list2
print(numbers)
print(len(numbers))  # -> listenin kaç elemanlı olduğunu öğreniyoruz

userA = ["Sadik", 36]
userB = ["Çinar", 2]
print(userA)
print(userB)

users = [userA,userB]  # -> liste başka bir liste içine alırsak iç içe listeler oluşturmuş oluruz
print(users)
print(users[0][1])