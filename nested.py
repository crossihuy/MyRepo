count = 0
num = int(input("Give me a number "))
if num < 0:
    print("your number is negative.")
elif num > 0:
    while count < num:
        count = count + 1
        print(count)



