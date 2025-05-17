import random
random_no=random.randint(1,100)
userguess=None
guesses=0

print("Welcome !! In the Game of Perfect Guess")
a=input("Enter your Name : ")
print(f"Hello,{a} Lets Start the Game....")

import random

random_no = random.randint(1, 100)  # Generate a random number between 1 and 100
guesses = 0

while True:
    userguess = int(input("Enter any number between 1 to 100: "))
    guesses += 1

    if userguess==random_no:
        print("Congrats! Your Guess is Correct.")
        break
    elif userguess > random_no:
        print("Your Guess is Wrong! Please select a smaller number.")
    else:
        print("Your Guess is Wrong! Please select a greater number.")

print(f"You guessed the correct number in {guesses} guesses.")