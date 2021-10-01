def is_num(question):
    while True:
        try:
            x = int(input(question))
            break
        except ValueError:
            print("That is not a number")
            continue
    return x
class cat():
    def_ init_(self):
        self.name = input("What is your pet's name? \n")
        self.type = input(f"What type of pet is {self.name}? \n").lower()

