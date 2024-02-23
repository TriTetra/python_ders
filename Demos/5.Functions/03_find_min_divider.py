
# Kullanıcıdan iki sayıyı giriş olarak alır.
def take_info():
    first_number = int(input("İlk sayiyi giriniz: "))
    second_number = int(input("İkinci sayiyi giriniz: "))
    return first_number, second_number


def find_ekok(a, b):
    max_number = max(a, b) # -> İki sayının çarpımından başlayarak artan bir sayıyı kontrol eder.
    print(max_number)
    
    while True:
        # Eğer bu sayı hem a'ya hem de b'ye tam bölünebiliyorsa,
        # bu sayı EKOK'dur ve fonksiyon bu değeri döndürür.
        if max_number % a == 0 and max_number % b == 0:
            return max_number
        # Sayıyı bir bir artırarak devam eder.
        max_number += 1
        print(max_number)

a, b = take_info()
result = find_ekok(a, b)
print(f"{a} ve {b} sayilarinin EKOK'u: {result}")
