import random
n = random.randint(1, 100)
print(n)

guess_count = 0
guess_limit = 5
while guess_count <= guess_limit :
    guess_count =+ 1
while True:

    if n > 100:
        print("not a number from 1-100, guess again")
    elif n < 0:
        print("not a number from 1-100, guess again")
    elif n == 80:
        print("You Win")
    elif n < 80:
        print("Sorry, your guess is to low try again")
    elif n > 80:
        print("Sorry, your guess is to high try again")
        raise ValueError("you loose")
