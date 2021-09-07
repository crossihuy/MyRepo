guests = []
food_cost = []
def av():
    sum = 0
    for x in food_cost:
        sum += x
    p = len(food_cost)
    sum /= p
    return sum

while True:
    guests.append(input("what is your name? "))
    food_cost.append(float(input("How much was your food? ")))
    loop = input("Would you like to add another person? ")
    if loop == "y" or loop == "":
        continue
    elif  loop == "n" or loop == "N":
        break
average = av()
print(round(average,2))
print(f"The average food cost was {average}")

