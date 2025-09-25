import random

random_integer = random.randint(1,10)

print(random_integer)

guess = input("guess a number 1-10")

while guess == random_integer:
    