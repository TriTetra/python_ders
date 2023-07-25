# 1 - "BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir dizi oluşturunuz.
list = ["BMW","Mercedes","Opel","Mazda"]

# 2 - Liste kaç elemanlıdır ? 
lastIndex = len(list)
print(lastIndex)

# 3 - Listenin ilk ve son elemanı
first = list[0]
end = list[lastIndex-1]
print("{} and {}".format(first,end))

# 4 - Mazda değerini Toyota ile değiştirin
list[-1] = "Toyota"
print(list)

# 5 - Mercedes listenin bir elemanı mıdır ? 
isMeredes = "Mercedes" in list
print(isMeredes)

# 6 - Listenin -2 değeri nedir ?
print(list[-2])

# 7 - Listenin ilk 3 elemanını alın 
print(list[0:3])

# 8 - Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin
list[-1] = "Toyota"
list[-2] = "Renault"
print(list)

# 9 - Listenin üzerine "Audi" ve "Nissan" değerini ekleyin
result = list + ["Audi","Nissan"]
print(result)

# 10 - Listenin son elemanını silin
del result[-1]
print(result)

# 11 - Lise elemanlarını tersten yazdırın
print(result[::-1])

# 12 - Aşağıdaki verileri bir liste içine saklayınız
        # studentA : Yiğit Bilgi 2012, (70,60,70)
        # studentB : Sena Turan 1999, (80,80,70)
        # studentC : Ahmet Turan 1998, (80,70,90)
studentA = ["Yiğit Bilgi",2012,[70,60,70]]
studentB = ["Sena Turan",1999,[89,80,70]]
studentC = ["Ahmet Turan",1998,[80,70,90]]

# 13 - Liste elemanlarını ekrana yazdırınız
students = studentA+studentB+studentC
print(students)