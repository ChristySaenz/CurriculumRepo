# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]
display_names = ["rock", "paper", "scissors"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

if user_choice in options: 
    message = f"You chose {display_names[options.index(user_choice)]}. The computer chose {display_names[options.index(computer_choice)]}."

    # Run Conditionals
    if (user_choice == computer_choice):
        print(message + " It's a tie!")
    else:
        if (user_choice == "r" and computer_choice == "p" or user_choice == "p" and computer_choice == "s" or user_choice == "s" and computer_choice == "r"):
            print(message + " Sorry. You lose.")

        elif (user_choice == "r" and computer_choice == "s" or user_choice == "p" and computer_choice == "r" or user_choice == "s" and computer_choice == "p"):
            print(message + " Yay! You won.")

else:
    print("I don't understand that!")
    print("Next time, choose from 'r', 'p', or 's'.")
