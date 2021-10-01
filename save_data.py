gbday = ""
try:
    with open("day.txt", "r") as fileday:
        yesterday = fileday.readlines()
        if yesterday == "good":
            print("Glad you had a good day yesterday")
        elif yesterday == "bad":
            print("Sorry you had a bad day, tomorrow will be better.")

except FileNotFoundError:
    print("Not sure how your day was yesterday.  Hope tomorrow is better.")
 

gbday = input("Did you have a good or bad day? ").lower()
    with open("day.txt", "w") as fileday:       
#    fileday.write(day)

  #  gbday = input("Did you have a good or bad day? ").lower()
#    fileday.readlines(f"{gbday}") 
