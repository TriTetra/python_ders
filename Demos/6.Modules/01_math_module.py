
key_word = None
isContue = True

def select_page_choose(index):
    words = []
    start = "Yapmak istediğiniz işlemi seçin: \n1- Basit hesam makinesi\n2- Karmaşik hesap makinesi"
    info = "Bilgi almak için help giriniz.."
    finish = "Baştaki menüye gitmek için q giriniz.."
    words.append(start)
    words.append(info)
    words.append(finish)

    return words[index-1]


def simple_calculator():
    print("Basit Hesap Makinesi")

    while True:
        print("\nYapmak istediğiniz işlemi seçin:")
        print("1- Toplama")
        print("2- Çikarma")
        print("3- Çarpma")
        print("4- Bölme")
        print("5- Çikiş")

        choice = input("Seçiminizi yapin (1-5): ")

        if choice == "5":
            print("Çikiliyor...")
            break

        if choice in ("1", "2", "3", "4"):
            num1 = float(input("İlk sayiyi girin: "))
            num2 = float(input("İkinci sayiyi girin: "))

            if choice == "1":
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")

            elif choice == "2":
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")

            elif choice == "3":
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")

            elif choice == "4":
                if num2 != 0:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
                else:
                    print("Bir sayiyi sifira bölemezsiniz.")
        else:
            print("Geçersiz seçim. Lütfen 1-5 arasinda bir rakam girin.")



if __name__ == "__main__":
    simple_calculator()
