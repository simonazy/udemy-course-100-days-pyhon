
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random 

def compete(computer_choice, user_choice):
    if computer_choice == "scissors" and user_choice == "paper":
        print("You lose")
    elif computer_choice == "scissors" and user_choice == "rock":
        print("You win")
    elif computer_choice == "rock" and user_choice == "scissors":
        print("You win")
    elif computer_choice == "rock" and user_choice == "paper":
        print("You lose")
    elif computer_choice == "paper" and user_choice == "rock":
        print("You lose") 
    elif computer_choice == "paper" and user_choice == "scissors":
        print("You win")
    else:
        print("No one wins")


def day_4_project(): 
    user_choice = input("what is your choice? Please choose from scissors, paper, rock ") 
    choices_key = ["scissors", "paper", "rock"] 
    choices_value = {"scissors":scissors, "paper":paper, "rock": rock} 
    while user_choice:
        computer_choice = random.choice(choices_key) 
        if user_choice not in choices_key:
            user_choice = input("Hey, only choose from scissors, paper, rock ") 
        else:
            print("Computer: \n", choices_value[computer_choice])
            print("User: \n", choices_value[user_choice])
            compete(computer_choice, user_choice) 
            user_choice = input("what is your choice? Please choose from scissors, paper, rock ") 
   

if __name__ == "__main__":
    day_4_project()

