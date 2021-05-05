#!/usr/bin/env python
import subprocess, smtplib

def send_mail(email, password, message):
#create google SMTP server and port 587 (google port for smtp)
    server = smtplib.SMTP("smtp.gmail.com", 587)
#init TLS connection for the SMTP server that was created above
    server.starttls()
#login method using email and password
    server.login(email, password)
#sendmail method to send from email, to self, using message
    server.sendmail(email, email, message)

command = "msg * words words words"
subprocess.Popen(command, shell=True)
