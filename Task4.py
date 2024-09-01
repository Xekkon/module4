import random

random_number = random.randint(1, 10)

print("The program is thinking of a number between 1 and 10.")

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < random_number:
        print("Too low")
    elif guess > random_number:
        print("Too high")
    else:
        print("Correct")
        break


