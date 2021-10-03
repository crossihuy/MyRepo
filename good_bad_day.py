try:
    with open("day.txt", "r") as gbday:
        answer = gbday.readline()
        if answer.lower() == "good":
            print("I'm glad you had a good day. 'Yeah'.")
        elif answer.lower() == "bad":
            print("Sorry You had a bad day. Tomorrow will be better. ")
        else:
            print("You did not tell me if you had a good or bad day! Why??  \n ")


except FileNotFoundError:
    print("You did not tell me about your day.")
today = open ("day.txt", "w") 

my_day = input("Did you have a good or bad day? \n").lower()

if my_day == "good":
    today.write(my_day)
    today.close()
elif my_day == "bad":
    today.write(my_day)
    today.close()
else:
    print("Could you please answer with 'good' or 'bad', Thank you. ")
