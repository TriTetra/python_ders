
# https://www.w3schools.com/python/python_for_loops.asp

number = [1, 2, 3, 4, 5, 6]

print(number[0])
print(number[1])
print(number[2])
print(number[3])
print(number[4])
print(number[5])    

# -> loops kullanmadığımızda liste içindeki elemanları tek tek kendimiz yazdırmamık gerekiyor

for num in number:  # -> number içindeki değerlerin sayısı kadar çalışır 
    print(num)      # -> for döngüleri sayesinde bir den fazla değerleri bir kaç satırda yama imkanı sağlar
    print('hello')


names = ['ayse', 'fatma', 'zehra']

for name in names:    # -> Burada names içindeki değerli f türünde yazdırıyoruz
    print(f'my name is {name}')



name = 'sadik turan'

for n in name:       # -> for içine girilen neredeyse çoğu elemanın ya indexine göre sayar ya da değerine göre
    print(n)


tuple = (1, 2, 3, 4, 5, 6, 7, 8)
tuples = ((1,2),(3,4),(5,6),(7,8))

for t in tuple:
    print(t)    

for tt in tuples:
    print(tt)       # -> tuple, liste ve setler gibi çoğu şeyide rahtalıkla çalıştırır