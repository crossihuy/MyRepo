with open("phone_book_b","w") as file:
    name = input["what is your full name? \n"]
    phone = input["what is your phone number? \n"]
    email = input["what is your email address? \n"]
    file.write(f"{name}\n" + "{phone}\n" + "{email}\n" + "{}\n")





