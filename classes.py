class Pet:
    def __init__(self):
        self.name = input("what is your pets name?\n")
        self.breed = input(f"what is {self.name}'s breed?\n")
        self.color = input(f"what is {self.name}'s color?\n")
dog = Pet()
print(f"{dog.name} is a {dog.breed} and is {dog.color}")

