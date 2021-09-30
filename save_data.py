try:
    with open("day.txt", "r") as fileday:
    yesterday = fileday.readlines()
if yesterday.lower() == "good":
print("Glad you had a good day yesterday")
elif yesterday.lower() == "bad":
print("Sorry you had a bad day, tomorrow will be better.")

except FileNotFoundError:
print("Not sure how your day was yesterday.  Hope tomorrow is better.")
 

with open("day.txt", "w+"): as fileday:       
fileday.write(day)


    
