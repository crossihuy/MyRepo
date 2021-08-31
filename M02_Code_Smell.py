food_stuff = float(input("How much was your meal? "))
uncle_sam = 1.08
pay_the_server = 1.15
corporate_cut = uncle_sam * food_stuff
pocket_book_pain = corporate_cut + pay_the_server
rounded = round(pocket_book_pain, 2)
string_value = str(rounded)
print("You need to leave " + string_value + " on the table to cover tax and tip.")






