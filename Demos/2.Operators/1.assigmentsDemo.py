x, y, z = 2, 5, 107
numbers = 1, 5, 7, 10, 6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z taplamının farkı nedir ?

a = input("a için sayı giriniz : ")
b = input("b için sayı giriniz : ")

result = (x+y+z)-int(a)*int(b)
print(result)

# 2- y'nin x'e kalansız bölümünü hesaplayınız

result = y/x

# 3- (x,y,z) toplamının mod 3'ü nedir ?

result = x+y+z%3
print(result)

# 4- y'nin x. kuvvetini hesaplayınız 

result =y*y
print(result)

# 5- x, *y, z numbers işlemine göre z nin küpü kaçtır?

numbers = 1, 5, 7, 10, 6
x,*y,z = numbers
result = z**3
print(result)


# 6- x, *y, z numbers işlemine göre y nin değerleri toplamı kaçtır?

numbers = 1, 5, 7, 10, 6
x,*y,z = numbers
result = y[0]+y[1]+y[2]
print(result)

