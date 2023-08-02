import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
print("Welcome to the Password Generator !")
while True:  # Used while loop for restart the app if user wants. 
    nr_of_letters = int(input("How many letters would you like in your password?\n: ")) # Converting numbers to integer for not getting TypeError 
    nr_of_symbols = int(input("How many symbols would you like in your password?\n: "))
    nr_of_numbers = int(input("How many numbers would you like in your password?\n: "))

    password_list = [] # I'm making this list because i will randomize the order of numbers, symbols and letters.

    for char in range(1, nr_of_letters + 1):
        password_list.append(random.choice(letters))  # Adding the letters to the list

    for sym in range(1, nr_of_symbols + 1):
        password_list.append(random.choice(symbols)) # Adding the symbols to the list

    for num in range(1, nr_of_numbers + 1):
        password_list.append(random.choice(numbers)) # Adding the numbers to the list

    random.shuffle(password_list) # Randomizing the order of numbers, symbols and letters.

    password = ""
    for pass_char in password_list:
        password += pass_char # Adding the numbers, symbols and letters from the password_list to the password 

    print(f"Your password is: {password}")
    user_another_password = input("Do you want another password ? y/n \n: ").lower() # We ask the user if he/she wants to create a password again
    if user_another_password == "n":
        print("Closing Password Generator...")
        break
