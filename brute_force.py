import hashlib
import string
import itertools

with open("shadow.txt","r") as fshadow:
    for line in fshadow:
        for x in range(1,25):
            #below list product string is all printable charictures xcpt last 6 tab space etc
            res = itertools.product(string.printable[:-6],repeat = x)
            for i in res:
#               print("".join(i))
                hashed = hashlib.md5(''.join(i).encode("UTF-8")).hexdigest()
                print(f"{hashed}    {''.join(i)}")
                if hashed == line[:-1]:
                    print(f"\n\nCRACKED\n\n{hashed}    {''.join(i)}\n\nThe password is {''.join(i)}")
                
                    quit()
