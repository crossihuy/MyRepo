from random import shuffle as shuf

abcd = ["a", "b", "c", "d"]
my_list1 = ["Banana", "Grapefruit", "Mango", "Peach"]
print("What fruit is round?\n")
shuf(my_list1)
for ans1, i in zip(my_list1, abcd):
    print(i, ans1)
answer = input("What letter is your answer? ")
ans1 = my_list1.index("Grapefruit")
if ans1  == "answer":
    print("Correct, Yeah!")

elif answer == ["a","c","d"]:
    print("Sorry wrong answer")
else:
    print("You did not select a letter")

print(my_list1)
answer = my_list1.index("Grapefruit")
print(answer)
#elif question == "n":
#    for i in my_list:
#    print(i + " is my friend")




#my_list2 = ["Sleepy", "Dopey", "Sneezy", "Doc", "Happy", "Bashful", "Grumpy"]
#print(import("What is the name of one of the seven dwarfs? \n")
