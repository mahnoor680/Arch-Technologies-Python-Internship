import random

while True:
    print(random.randint(1,6))

    user_roll = input("Want to roll the dice again? (y/n): ")
    if user_roll.lower() == "y":
        continue
    else:
        break