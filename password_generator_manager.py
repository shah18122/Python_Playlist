import random

characters = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '!', '@', '#', '$', '%', '^', '&', '*', '(', ')')

print("Welcome to Password Generator and Manager!")

while True:
    choice = input("Press 1 to generate password\nPress 2 to view passwords\nPress 3 to exit: ")

    if choice == '1':
        length = int(input("Enter the length of the password: "))
        site = input("Enter the site name: ")
        password = ''
        for i in range(length):
            password += str(random.choice(characters))
        with open('passwords.txt', 'a') as file:
            file.write(f"{site} : {password}\n")

    elif choice == '2':
        try:
            with open('passwords.txt', 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("No passwords saved yet.")

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
