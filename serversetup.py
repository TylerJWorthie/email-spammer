import os
path = "./servers"
try:
    #making path
    os.mkdir(path)
except:
    #skipping making path
    print("")
print("To find smtp server just search, 'Your email service smtp' i.e. gmail smtp")
srvrad = input("SMTP Server addresss: ")
serverport= input("Server port: ")
serveraddy = open(r"servers/smtpserver.txt","w+").writelines(srvrad)
serverprt = open(r"servers/serverport.txt", "w+").writelines(serverport)
