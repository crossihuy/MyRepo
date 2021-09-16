import random

# This fucntion gets an int from the user, it only allows ints and prevents
# numbers less then 1 and great then 100
def get_int():
    while True:
        try:
            num = int(input("What is your guess: "))
            if num < 1:
                print("You can't have a number less then 1.")
            elif num > 100:
                print("You can't have a number greater then 100.")
            return num
        except ValueError:
            print("You did not give a number.")
            continue

again = "y" # again is set to y to hard code the start of the first game
while again != "n": # The game keeps playing on a yes and defult, stops on no
    rand_num = random.randint(1, 100)
    trys = 0
    print("Guess a number between 1 and 100.")
    while trys < 5:
        guess = get_int()
        if guess > rand_num:
            print("Your guess is to high.")
            trys = trys + 1
        elif guess < rand_num:
            print("Your guess is to low.")
            trys = trys + 1
        else:
            print("You guessed the number!")
            break
    if trys > 4:
        print(f"The number was {rand_num}. Better luck next time.")
    # This loop makes sure that we only get one of three answers
    # The defult answer "", a yes "y", and no "n"
    while True:
        again = input("Do you want to play again? Y|n: ")
        if again == "y" or again == "" or again == "n":
            break
        else:
            print("Invaid input.")
