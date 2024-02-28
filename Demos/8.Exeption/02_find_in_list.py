
liste = [3,5,2,7,77,34,76,13,654,23,76,3,99,23,15,17]

def sayi_kontrol(sayi):
    
    if sayi % 2 == 0:
        return sayi
    else:
        raise ValueError
    


for eleman in liste:
    try:
        print(sayi_kontrol(eleman))
    except ValueError:
        pass