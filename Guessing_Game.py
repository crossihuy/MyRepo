import random
min = 1
max = 100
n = random.randint(1, 100)
guess_count = 0
guess_limit = 4
while guess_count <= guess_limit:
    guess = int(input("Guess a number between 1-100 \n"))
    guess_count += 1

    if guess > max:
        print("not a number from 1-100, guess again")
    elif guess < min:
        print("not a number from 1-100, guess again")
    elif guess < n:
        print("your guess is to low")
    elif guess > n:
        print("your guess is to high. ")
    elif guess == n:
        print(" you win, it was %d" % n)

else:
    print("you loose, it was %d" % n)

while True:
    guess = input("Do you want to play again? : \ny|n: ").lower()
    if guess == "y" or guess == "":
        continue