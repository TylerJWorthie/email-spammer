import tkinter as tk
import os
import smtplib

#Server Logins#
email = open(r"creds/email.txt","r").read()
password = open(r"creds/pswrd.txt", "r").read()
#Server Info#
serveradd = open(r"servers/smtpserver.txt", "r").read()
serverport = open(r"servers/serverport.txt", "r").read()

root = tk.Tk()

root.geometry('500x200')

def labels_input(intext, lblRow, lblColumn):
	lbl = tk.Label(root, text = intext)
	lbl.grid(row=lblRow, column = lblColumn)

labels_input("Receivier's Email: ", lblRow = 0, lblColumn = 0)
reciv_input = tk.Entry(root)
reciv_input.grid(row=0, column=1)


labels_input("Message to: ", lblRow = 1, lblColumn = 0)
msg_input = tk.Entry(root)
msg_input.grid(row=1, column=1)

labels_input("Times sent: ", lblRow = 2, lblColumn = 0)
sent_input = tk.Entry(root)
sent_input.grid(row=2, column=1)


def sendingEmails():
	reciv_output =reciv_input.get()
	msg_output = msg_input.get()
	sent_output = sent_input.get()
	server = smtplib.SMTP(serveradd, serverport )
	server.starttls()
	server.login(email,password)
	for i in range(int(sent_output)):
		i = i+1
		server.sendmail(gmail, reciv_output, msg_output)
		label = tk.Label(text = f"Email sent {i} times").grid(row = 4, column = 0)
getInput_button = tk.Button(text = 'Send them out!', command = sendingEmails)
getInput_button.grid(row = 3, column = 0)

credit = tk.Label(text = "Made by Worthie!").grid(row = 3, column = 1)

root.mainloop()
