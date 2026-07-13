# Run this command in terminal before running the project:-
# pip install colorama

import random
from colorama import Fore

print (Fore.CYAN + "\n"*2 + "==============================================================================================================\n" + "                               Welcome to the Number Guessing Game!!!!!\n" + "==============================================================================================================" + "\n"*2 + Fore.RESET)

print (Fore.GREEN + "Choose a difficulty level:\n 1. Easy\n 2. Medium\n 3. Hard\n" + Fore.RESET)

while True:
    try:
        level = int(input(Fore.YELLOW + "Enter the number corresponding to your chosen difficulty level: " + Fore.RESET))
        
        if level < 1 or level > 3:
            print(Fore.RED + "Invalid Choice. Try Again!!\n" + Fore.RESET)
        else:
            break

    except ValueError:
        print(Fore.RED + "Please enter a valid number!\n" + Fore.RESET)
print ("")

# Levels Data
levels = {
    1: {"range": (1, 20), "attempts": 10},
    2: {"range": (1, 50), "attempts": 7},
    3: {"range": (1, 100), "attempts": 5}
}

number_to_guess = random.randint(*levels[level]["range"])
print (Fore.BLUE + f"You have chosen level {level}. \nYou will have {levels[level]['attempts']} attempts to guess the number between {levels[level]['range'][0]} and {levels[level]['range'][1]}.\n" + Fore.RESET)
attempts = levels[level]["attempts"]
    
while attempts > 0:
    try:
        guess = int(input(Fore.YELLOW + "Enter your guess: " + Fore.RESET))
    except ValueError:
        print(Fore.RED + "Invalid input! Please enter a number.\n" + Fore.RESET)
        continue
    if guess < levels[level]["range"][0] or guess > levels[level]["range"][1]:
        print(Fore.RED + "Please enter a number within the allowed range.\n" + Fore.RESET)
        continue
    elif guess < number_to_guess:
        print (Fore.MAGENTA + "Too low! Try again.\n" + Fore.RESET)
    elif guess > number_to_guess:
        print (Fore.MAGENTA + "Too high! Try again.\n" + Fore.RESET)
    else:
        print (Fore.GREEN + "Congratulations! You guessed the number correctly!\n" + Fore.RESET)
        print (Fore.GREEN + "You Win!!\n" + Fore.RESET)
        print (Fore.GREEN + "Thanks for playing! Goodbye!!\n" + Fore.RESET)
        exit()
        
    attempts -= 1
    print("")
    print (Fore.CYAN + "Attempts remaining:" + str(attempts) + Fore.RESET)
        
    if attempts == 0:
        print (Fore.RED + "\nSorry, you've used all your attempts. The number was:"+ Fore.RESET + Fore.GREEN + str(number_to_guess) + Fore.RESET +"\n")
        print (Fore.RED + "Better luck next time! Thanks for playing! Goodbye!!\n" + Fore.RESET)
        exit()

    