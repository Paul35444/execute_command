#!/usr/bin/env python
import subprocess, smtplib

def send_mail(email, password, message):
    server = smtplib.SMTP()

command = "msg * words words words"
subprocess.Popen(command, shell=True)
