max_tries = 5
while   max_tries > 0:
    num1 = int(input("pick a number from 1-100. "))
    if num1 > 100:
        print("not a number from 1-100, guess again")
    if num1 < 0:
        print("not a number from 1-100, guess again")
    if num1 == 17:
        print("You Win")
    elif num1 < 17:
        print("Sorry, your guess is to low try again")
    elif num1 >17, ==100:
        print("Sorry, your guess is to high try again")
max_tries -= 1
raise ValueError("you loose")

