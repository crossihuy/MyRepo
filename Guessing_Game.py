import random
while True:
    n = random.randint(1, 100)
    if n > 100:
        print("not a number from 1-100, guess again")
    elif n < 0:
        print("not a number from 1-100, guess again")
    else:
        break

print(n)
count = 0
while count < 5:
    while True:
        try:
            num1 = int(input("Guess a number "))
            break
        except ValueError:
            print("Please guess a number. ")
            continue
    if num1 < n  :
        print("your guess is to low")
    elif num1 > n :
        print("your guess is to high. ")

    count += 1