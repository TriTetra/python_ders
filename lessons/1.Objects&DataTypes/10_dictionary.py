
# https://www.w3schools.com/python/python_dictionaries.asp

# key - value 
# 42 => kocaeli  , 34 => İstanbul

sehirler = ['kocaeli','istanbul']
plakalar = [42,34]

print(plakalar[sehirler.index('kocaeli')]) # -> kocaeli nin indexini alır ve onu plakalara koyarak plakaların o indexini bulur
print(plakalar[sehirler.index('istanbul')])

plakalar = {'kocaeli' : 41 , 'istanbul' : 34} 
print(plakalar['istanbul'])  # -> dictionary bir key-value türü olduğu için key in value sini getirir her zaman
print(plakalar['kocaeli'])
print(plakalar)

plakalar['ankara'] = 6  # -> yeni key atayarak o değere value veriyoruz
plakalar['kocaeli'] = 'new value' 
print(plakalar)


users = {
    'sadikturan' : {
        'age' : 36,
        'role' : ['admin','user'],
        'email' : 'sadikturan@gmail.com',
        'address' : 'kocaeli',
        'phone' : '1231232'
    },
    'çinarturan' : {
        'age' : 29,
        'role' : ['user'],
        'email' : 'çinarturan@gmail.com',
        'address' : 'istanbul',
        'phone' : '98778654'
    },
    'kovakturan' : {
        'age' : 43,
        'role' : ['user','asistant'],
        'email' : 'kovakturan@gmail.com',
        'address' : 'ankara',
        'phone' : '3452346'
    }
}     # -> iç içe de dictionary ler oluşturabiliriz

print(users['çinarturan']) # -> istediğimiz key çağırdığımızda o key sahip olduğu bütün value leri çağirir
print(users['kovakturan']['role']) # -> dictionary içinde liste oluşturarak ta örnekteki gibi çalıştırabiliriz.