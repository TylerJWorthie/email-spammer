import os
path = "./creds"
try:
    #making path
    os.mkdir(path)
except:
    #skipping making path
    print("")
print("Just type in email and password")
email = input("What email would you like to use? ")
pswrd = input("What pswrd is connected to this email? ")
eml = open(r"creds/email.txt","w+").writelines(email)
password = open(r"creds/pswrd.txt", "w+").writelines(pswrd)
