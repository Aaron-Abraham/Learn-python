import random
import time

print("Welcome to the guessing game. I am going to pick a number between 1 and 100")
time.sleep(2)
print("Picking a number...")
time.sleep(2)
guess = int(input("What is your guess? :"))
correct_number = random.randint(1,100)
guess_count = 1

while guess != correct_number:
    guess_count += 122
    if guess < correct_number:
        guess = int(input("Wrong, you have to guess higher. What's your guess? : "))
    else:
        guess = int(input("Wrong, you have to guess lower. What's your guess? : "))

print(f"Kudos!! The right answer was {correct_number}. It took you {guess_count} guesses.")