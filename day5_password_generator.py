#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
def main():
    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    password = ""
    for i in range(nr_letters):
        char = random.choice(letters)
        password += char 
    for i in range(nr_symbols):
        sym = random.choice(symbols)
        password += sym 
    for i in range(nr_numbers):
        num = random.choice(numbers)
        password += num 

    password_list = list(password)
    random.shuffle(password_list) 
    print(f"This is your unorderedpassword: {''.join(password_list)}")
    print(f"This is your password: {password}")


if __name__ == "__main__":
    main() 