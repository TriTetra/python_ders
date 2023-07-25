

def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception('Parola 8 karakterden küçük olmalidir.')
    elif not re.search('[a-z]',psw):
        raise Exception('Parola küçük karakterler içermelidir.')
    elif not re.search('[A-Z]',psw):
        raise Exception('Parola Büyük karakterler içermelidir.')
    elif not re.search('[0-9]',psw):
        raise Exception('Parola sayisal karakterler içermelidir.')
    elif not re.search('[_@$]',psw):
        raise Exception('Parola alfa nümerik karakterler içermelidir.')
    elif re.search('\s',psw):
        raise Exception('Parola boşluk içermemelidir.')
    else:
        print('Geçerli parola')
    
password = '123456789aA@'    

try:
    check_password(password)
except Exception as ex:
    print(ex) 
finally:
    print('validation tamamlandi.')
    