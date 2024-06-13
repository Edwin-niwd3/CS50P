import random

while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            raise ValueError
        break
    except ValueError:
        pass
guess = -1
number = random.randint(1, level)
while guess < number or guess > number:
    try:
        guess = int(input("Guess: "))
        if guess < 0:
           raise ValueError
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
    except ValueError:
        pass
print("Just right!")
