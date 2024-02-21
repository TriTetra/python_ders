vize1 = float(input("Vize 1 giriniz: "))
vize2 = float(input("Vize 2 giriniz: "))
final = float(input("Final giriniz: "))

vize1 = vize1 * 0.30
vize2 = vize2 * 0.30
final = final * 0.40

average = vize1+vize2+final

if(average >= 90):
    print("AA")
elif(average >= 85):
    print("BA")
elif(average >= 80):
    print("BB")
elif(average >= 75):
    print("CB")
elif(average >= 70):
    print("CC")
elif(average >= 65):
    print("CD")
elif(average >= 60):
    print("DD")
elif(average >= 55):
    print("FD")
elif(average > 0):
    print("FF")
else:
    print("Hatali giriş..")

print(average)