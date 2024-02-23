

def perfect_numbers():
    for x in range(1,1001):
        result = 0
        for y in range(1,x):
            if(x % y == 0):
                result += y
        if(x == result):
             print(x)


perfect_numbers()


