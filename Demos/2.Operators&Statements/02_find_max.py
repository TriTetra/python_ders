"""

list_number = []

number_one = int(input("İlk Sayi: "))
number_two = int(input("İkinci Sayi: "))
number_three = int(input("Üçüncü Sayi: "))


list_number.append(number_one)
list_number.append(number_two)
list_number.append(number_three)

max_number = max(list_number)
print(max_number)

"""


number_one = int(input("İlk Sayi: "))
number_two = int(input("İkinci Sayi: "))
number_three = int(input("Üçüncü Sayi: "))

if (number_one <= number_two and number_two >= number_three):
    print("En büyük sayi ", number_two)
elif(number_two <= number_one and number_one >= number_three):
    print("En büyük sayi",number_two)
elif(number_one <= number_three and number_three >= number_two):
    print("En büyük sayi ",number_three)
else:
    print("Hatali giriş")
