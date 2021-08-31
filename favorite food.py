my_list = []
my_list.append(input("what is your favorite food? "))
while True:
    question = input("Do you have another favorite food: \n y|n: ").lower()
    if question == "y" or question == "":
        my_list.append(input("what is it: "))
#        my_list.append(input(" do you have another one: \ny|n: ").lower())
    elif question == "n":
        break
    else:
        print("You did not select y or n")
for i in my_list:
    print(i, end=" ")
print("are my favorite foods")








