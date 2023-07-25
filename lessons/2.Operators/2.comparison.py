
# https://www.w3schools.com/python/python_operators.asp

# username , password => database
# 'sadikturan' , '123456'

a, b, c, d = 5, 5, 10, 4

result = (a==b) # -> a ile b birbirine eşit mi demek '==' eşitlemede kullanılır
result = (b==c)
print(result)

username = 'sadikturan'
password = '1234'

result = ('sdktrn' == username)       # FALSE
result = ('sadikturan' == username)   # TRUE

result = ('sdktrn' != username)   # TRUE demesinin nedeni '!=' işareti birbirlerine eşit değillerdir demek
result = (b != c)
print(result)

result (a > c)  # -> FALSE c değeri a dan büyüktür '>' 
result (b < d)  # -> TRUE b değeri d değerinden küçüktür '<'
result (a >= b) # -> TRUE a değeri b değerinden büyük veya eşit mi '>='
