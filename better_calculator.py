def main():
    function = ""
num1 = 0
num2 = 0
q = "y"
function = input("""Do you want to +(add), -(subtract), *(multiply), or /(divide) \n""")

num_1 = float(input("What is your first number? "))

num_2 = float(input("What is your second number? "))

if function == "+":
    print("{} + {} = ".format(num_1, num_2))
    print(num_1 + num_2)

elif function == "-":
    print("{} - {} = ".format(num_1, num_2))
    print(num_1 - num_2)

elif function == "*":
    print("{} * {} = ".format(num_1, num_2))
    print(num_1 * num_2)

elif function == "/":
    print("{} / {} = ".format(num_1, num_2))
    print(num_1 / num_2)
    q = input("do you want to continue? y/n\n ").lower