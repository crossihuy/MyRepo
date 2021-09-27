def main():
    q = "y"
while True:
    try:
        print("Please enter five numbers. ")
        num_1 = float(input("What is your first number? "))

        f1 = input("""Do you want to +(add), -(subtract), *(multiply), or /(divide) \n""")
    
        num_2 = float(input("What is your second number?\n "))
        num_3 = float(input("What is your third number?\n "))
        num_4 = float(input("What is your fourth number?\n "))
        num_5 = float(input("What is your fith number?\n "))
    except ValueError:
        print("You did not enter a number. ")
        continue	

    if f1 == "+":
        print("{} + {} + {} + {} + {} = ".format(num_1, num_2, num_3, num_4, num_5 ))
        print(num_1 + num_2 + num_3 + num_4 + num_5 )
    elif f1 == "-":   
        print("{} - {} - {} - {} - {} = ".format(num_1, num_2, num_3, num_4, num_5))
        print(num_1 + num_2 + num_3 + num_4 + num_5 )
    elif f1 == "*":	
        print("{} * {} * {} * {} * {} = ".format(num_1, num_2, num_3, num_4, num_5))
        print(num_1 + num_2 + num_3 + num_4 + num_5 )
    elif f1 == "/":
        print("{} / {} / {} / {} / {} = ".format(num_1, num_2, num_3, num_4, num_5))
        print(num_1 + num_2 + num_3 + num_4 + num_5 )
    else:
        print("Enter a valid function, ")
        break
while True:	
    q = input("do you want to continue? y/n\n ").lower
    if q == "y" or q == "" or q == "n":
        continue
else:
    print("you did not make a selection. ")
