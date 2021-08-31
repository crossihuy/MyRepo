my_list = []
while True:
    question = input("Do you want to add a name: \ny|n: ").lower()
    if question == "y" or question == "":
        my_list.append(input("Give me a friend's name: "))
        continue
    elif question == "n":
        break
    else:
        print("You did not select y or n")
for i in my_list:
    print(i + " is my friend")

