import hashlib
from datetime import datetime
import getpass

import os
import time
 
def timestamp():
    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')
    return date

def new_user(name):
    while True:
            
        uName = input("What is your user name going to be? \n")
        pass1 = hashlib.md5(getpass.getpass("What is your password:").encode('UTF-8')).hexdigest()
        #above hashs password to md5 level and encodes to utf then to hex
        pass2 = hashlib.md5(getpass.getpass("Confirm your password:").encode('UTF-8')).hexdigest()
        #confirms password.  will not print on screen in program run
        if pass1 == pass2:
            with open("shadow.txt","a") as fShadow:
                fShadow.write(f"{uName} {pass1}\n")
            with open("log.txt","a") as fLog:
                fLog.write(f"New user: {uName}, created by: {name}, at: {timestamp()}\n")
                break

        else:

            print("Your passwords did not match" )
def login():
    while True:
        unames = []
        shadows = []
        state = False
        while True:
            try:
                with open ('shadow.txt','r') as fShadow:
                    for line in fShadow:
                        seperater = line.split()
                        unames.append(seperater[0])
                        shadows.append(seperater[1])
                break
            except FileNotFoundError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("No file found, starting for new user. ")
                time.sleep(2)          
                new_user("System")
                continue
        while state != True:
            print(state,unames,shadows)    
            user = input("What is your user name?\n")
            if user in unames:
                ##TODO: Add password section
                count = 0
                position = unames.index(user)
                while count < 2:
                    count += 1
                    passwd = hashlib.md5(getpass.getpass("Please enter your password:").endcode('UTF-8')).hexdigest()

                    if passwd == shadows[position]:
                        state = True
                        break
                else:
                    with open('log.txt','a') as fLog:
                        fLog.write(f"ATTEMPTED LOGIN WITH OUT CREDENTIALS: {timestamp()}")
                        getpass.getpass("Please enter your password:")
                        getpass.getpass("Please enter your password:")
                        getpass.getpass("Please enter your password:")
                        time.sleep(2)
                        quit()
             
      
login()                    
