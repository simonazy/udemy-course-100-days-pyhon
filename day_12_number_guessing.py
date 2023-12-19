import random 

def get_and_check_level():
    levels = ['easy', 'hard']
    level = input("Type 'easy' or 'hard': ")
    while level not in levels:
        level = input("Type 'easy' or 'hard': ")
    if level=="easy":
        return 10
    else:
        return 5 


def compare(num1, num2, attempts):
    while attempts>0:
        if num2 > num1:
            attempts -= 1
            print(f"Too high. \nGuess again. \nYou have {attempts} remaining to guess the number.") 
        elif num2 < num1:
            attempts -= 1
            print(f"Too low. \nGuess again. \nYou have {attempts} remaining to guess the number.") 
        else:
            print("Bingo")
            return
        num2 = int(input("Make a guess: "))   
    print("You failed:>")
    return 

def main():
    print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
    attempts = get_and_check_level()
    computer_number = random.randint(1, 100) 
    user_guessing = int(input("Make a guess: "))
    compare(computer_number, user_guessing, attempts) 
    
    
main()