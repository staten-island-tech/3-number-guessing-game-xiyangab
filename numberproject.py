import random

random_integer = random.randint(1,10)

print(random_integer)

guess = int(input("guess a number 1-10"))
guess_count = 0
guess_history = []

while guess != random_integer:
    guess_count = guess_count + 1
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
    guess_count = guess_count + 1

if guess_count == 1:
    print(f"you guessed the number first try!!")
    print (f"your guesses: {guess_history}")
else:
    print(f"it took you {guess_count} tries to get the number!!")
    print (f"your guesses: {guess_history}")