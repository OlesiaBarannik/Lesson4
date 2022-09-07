import random
print("The Guessing Game")

while True:
    number = random.randint(1, 10)
    question = int(input("Guess the number from 1 to 10 :\n"))
    if number == question:
        print("you guess")
        break
    else:
        print("you were wrong")
