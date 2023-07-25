
# https://www.w3schools.com/python/python_conditions.asp

x = 8
y = 13

if x < y :
    print("{} büyüktür".format(y))         # -> başlangıç olarak durumu buradan kontrole başlar 
elif x == y:
    print("{} ve {} sayilari eşittir".format(x,y))     # -> ikinci olarak burayı kontrol eder 
else:
    print("{} büyüktür".format(x))         # -> yukarıdaki iki durumda sağlamıyorsa son olarak burası çalışır


