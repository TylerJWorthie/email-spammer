import os
path = "./creds"
try:
    #making path
    os.mkdir(path)
except:
    #skipping making path
    print("")
print("Must use gmail, working on update to use multiple types of email servies")
email = input("What gmail would you like to use? ")
pswrd = input("What pswrd is connected to this gmail? ")
eml = open(r"creds/email.txt","w+").writelines(email)
password = open(r"creds/pswrd.txt", "w+").writelines(pswrd)
