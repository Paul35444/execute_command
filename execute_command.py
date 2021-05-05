#!/usr/bin/env python
import subprocess, smtplib

def send_mail(email, password, message):
#use google SMTP server and port 587 (google port for smtp)
    server = smtplib.SMTP("smtp.gmail.com", 587)

command = "msg * words words words"
subprocess.Popen(command, shell=True)
