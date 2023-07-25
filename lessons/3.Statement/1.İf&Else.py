
# https://www.w3schools.com/python/python_conditions.asp

username = 'sadikturan'
password = '1234'

isLoggedin = (username == 'sadikturan' and password == '1234')

if(isLoggedin):   # -> if - else durumları eğer bu koşul bana verilen koşulu karşılıyorsa çalışırım mantığı ile çalışır
    print('Welcome back')
else:
    print('Wrong')    