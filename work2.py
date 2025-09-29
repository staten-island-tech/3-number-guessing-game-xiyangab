import random

random_integer = random.randint(1,10)

guess = int(input("guess a number 1-10"))
guess_history = []

while guess != random_integer:
    if guess > random_integer:
        print("your guess is greater")
        guess_history.append(guess)
        print (f"your guesses: {guess_history}")
        guess = int(input("guess a number 1-10"))
    elif guess < random_integer:
        print("your guess is less")
        guess_history.append(guess)
        print (f"your guesses: {guess_history}")
        guess = int(input("guess a number 1-10"))

if guess == random_integer:
    print("woohoo you guessed the number!!")
    guess_history.append(guess)
    print(f"you guessed {len(guess_history)} times")
    print(f"your guesses were: {guess_history}")