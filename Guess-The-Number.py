import random
import time

# Intro
print("\nWelcome To The Number Guessing Game!"
    "\nI Am Going To Choose Number Between 1 and 100."
    "\nYour attempts will vary depending on the difficulty.")
time.sleep(1)
# Difficulty selection
print("\nPlease Select The difficulty.")
time.sleep(0.5)
print("\n1. Easy: 10 attempts"
      "\n2. Medium: 5 attempts"
      "\n3. Hard: 3 attempts")

difficulty = input()
try:
    difficulty = int(difficulty)
# error handling
except ValueError:
    print("Input is not a number! choose 1 , 2 or 3!")
    print("\nTry again! If you fail again restart the game.")
    difficulty = input()
if difficulty == 1:
    attempts = 10
elif difficulty == 2:
    attempts = 5
if difficulty == 3:
    attempts = 3
elif difficulty > 3 or difficulty < 1:
    print("Unknown difficulty! please select 1 , 2 or 3.")
    print("\nRestart game to try again.")
    time.sleep(2)

playing = True
player_score = 0
try:
    previous_attempts = attempts
except NameError:
    pass

# The Game
number = random.randint(1 , 100)
try:
    while True:
        if attempts > 0:
            if playing:
                guess = input("Choose a number:")
                try:
                    guess = int(guess)
                except ValueError:
                    print("Please enter a number.")
                try:
                    if guess > number and guess < 101 and guess > 0:
                        print(f"Number is lower than {guess}")
                        attempts -= 1
                        print(f"{attempts} left.")
                    elif guess < number and guess < 101 and guess > 0:
                        print(f"Number is bigger than {guess}")
                        attempts -= 1
                        print(f"{attempts} left.")
                    if guess == number:
                        print("\nYou win!")
                        time.sleep(0.3)
                        print("\nDo you want to continue? Y/N")
                        player_input = input().lower()
                        player_score += 1
                        playing == False
                        if player_input == "y":
                            attempts = previous_attempts
                            number = random.randint(1 , 100)
                            print(f"\nYour score is: {player_score}")
                            playing = True
                        if player_input == "n":
                            break
                        if player_input != "n" and player_input != "y":
                            print("\nPlease enter Y or N.")
                            playing = False
                            player_input = input().lower()
                            time.sleep(0.3)
                    if guess < 1 or guess > 100:
                        print("Enter a number from 1 to 100.")
                except TypeError:
                    pass        
        elif attempts == 0:
            print("\nYou are out of attempts! Do you want to try again? Y/N")
            player_input = input().lower()
            player_score = 0
            if player_input == "y":
                number = random.randint(1 , 100)
                attempts = previous_attempts
                playing = True
            if player_input == "n":
                break
            if player_input != "n" or "y":
                print("\nPlease enter Y or N.")
                time.sleep(0.3)
except NameError:
    pass