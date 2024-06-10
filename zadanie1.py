import random
import string
import re


'''
tu masz do sprawdzania mocy hasel np:
1qwe! - słabe
Qwe!456 - slabe
!_2QdFe4p_ - mocne
!34Fs4^dS23fDAA - bardzo mocne
'''
def check_password_strength(password):
    if len(password) < 8:
        return "Słabe"
    if not re.search("[a-z]", password):
        return "Słabe"
    if not re.search("[A-Z]", password):
        return "Słabe"
    if not re.search("[0-9]", password):
        return "Słabe"
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Słabe"
    if len(password) >= 12:
        return "Bardzo Mocne"
    return "Mocne"


#tu masz funkcje do generowania hasel
def generate_strong_password(length=16):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


##tu masz funkcje do tworzenia pliku z hasłami( jak ja wywolujesz to wpisujesz te 2 argumenty czyli nazwa pliku i ilosc)
def save_passwords_to_file(filename, num_passwords, length=16):
    with open(filename, 'w') as file:
        for _ in range(num_passwords):
            file.write(generate_strong_password(length) + '\n')


#tu masz main program czyli wybieranie co chcesz robic ja to ifami robilem mozna to tez zrobic match case
def main():
    while True:
        print("Wybierz opcję:")
        print("1. Sprawdź siłę hasła")
        print("2. Wygeneruj bardzo silne hasło i zapisz 100 haseł do pliku")
        print("3. Wyjście")
        choice = input("Wpisz swój wybór (1/2/3): ")

        if choice == '1':
            password = input("Wpisz hasło do sprawdzenia: ")
            strength = check_password_strength(password)
            print(f"Siła hasła: {strength}")
        elif choice == '2':
            strong_password = generate_strong_password()
            print(f"Wygenerowane bardzo silne hasło: {strong_password}")
            save_passwords_to_file("pass.txt", 100)
            print("100 bardzo mocnych haseł zostało zapisanych do pliku 'pass.txt'.")
        elif choice == '3':
            print("Do widzenia!")
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    main()
