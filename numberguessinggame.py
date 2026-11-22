import random

num = random.randint(1,50)
guess = int(input("Guess a number between 1 to 50: "))

while guess !=num:
    if guess>num:
        print("Your guess is too high.")
    elif guess<num:
        print("Your guess is too low.")

    guess = int(input("Guess Again: "))

print("Yooooooooo! You guessed it right.")
