 
# https://www.w3schools.com/python/python_operators.asp

x = 6

hak = 5
devam = 'e'

result = 5 < x < 10  # -> iki sayının arasını kod içinde belirmek istediğimizde parlamalıyız
print(result)

# and
# TRUE  and TRUE  = TRUE 
# TRUE  and FALSE = FALSE
# FALSE and FALSE = TRUE

result = 5 < x and x < 10 # -> şeklinde kullanılır ilk parça parça bakar sonra birleştirir
result = (0 < hak) and (devam == 'e')
 
# or
# TRUE  or TRUE  = TRUE
# TRUE  or FALSE = TRUE
# FALSE or FALSE = FALSE

result = (x > 0) or (x % 2 == 0)  # -> or operatörü ikisinden birisinin true olması durumunda çalışmaya devam eder

# not

result = not(x > 0)  # -> değilse çalıştır gibi düşünebilirsiniz.
print(result)