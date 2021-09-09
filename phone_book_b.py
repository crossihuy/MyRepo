q = "y"
while q != "n":
    name = input("please give me a name ")
    email = input("please give me a email ")
    phone = input("please give me a phone ")

    with open("phone_book_b","a") as file:
        file.write(f"{name} {phone} {email}\n")
                        
    while True:
        q = input("do you want to add another contact y/n ")
        if q == "y" or q == "" or q == "n":
            break
        else:
            print("you didn't make a correct selection")