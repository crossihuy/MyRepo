letter_grades = {"A":4, "B":3, "C":2, "D":1, "F":0}   # A is the key place, 4.0 is the value place
print(letter_grades)
letter_grades.update({"A":4.0, "B":3.0, "C":2.0, "D":1.0, "F":0.0})#to up date all,

print(letter_grades)
print(letter_grades.keys())# to print keys in above
for i in letter_grades.keys():
    print(i)

print(letter_grades.values())
for i in letter_grades.values():
    print(i)
print(letter_grades.items())  # i for the keys place, j is for the values place
for i, j in letter_grades.items():
    print(i,j)

print(letter_grades["A"])

def get_key(arg, dictionary):  # arg can be any value name
    for key, value in dictionary.items():
        if value == arg:   # arg is for argument can be any name value
            return key
x = get_key(2.0, letter_grades)
print(x)

 #how to count from a list use a dictionary
 grades = ["A", "B", "A", "F", "D", "A", "F", "C", "A", "A", "A", "B", "A", "B"]
 count = {}
 for i in grades:
     count[i] = count.get(i, 0) + 1  #counts from 0 if none there
 print(count)  # not working with other code above this code starting on 27-31