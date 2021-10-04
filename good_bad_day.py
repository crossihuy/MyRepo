# file asks how was your day and creates a file to store the answer then on replay 
# will remark on if it was a good or bad day.
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
# will print if no day.txt file exists
    print("You did not tell me about your day.")
today = open ("day.txt", "w") 

my_day = input("Did you have a good or bad day? \n").lower()
#will ask about day and create a day.txt file
if my_day == "good":
    today.write(my_day)
    today.close()
elif my_day == "bad":
    today.write(my_day)
    today.close()
else:
    print("Could you please answer with 'good' or 'bad', Thank you. ")
# if good or bad is not entered it will print above
