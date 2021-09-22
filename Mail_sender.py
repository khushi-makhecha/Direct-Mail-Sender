from email.mime.multipart import MIMEMultipart
# MIME :- Multipurpose Internet Mail Extensions
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()
# Primary purpose of the class MIMEMultipart() is to allow the use of attach() method.

msg["from"] = "My Trial"
msg["to"] = "makhechakhushi@gmail.com"
msg["subject"] = "Hey there, successful test 1!"

msg.attach(MIMEText("Congratulations !! I nailed it"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    # SSL :- Secure Sockets Layer
    # TLS :- Transport Layer Security
    smtp.ehlo()
    # Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command
    # sent by an email server to identify itself
    # when connecting to another email server to start the process of sending an email.
    # The EHLO command tells the receiving server it supports extensions
    # compatible with ESMTP.
    smtp.starttls()
    # Put the SMTP connection in TLS (Transport Layer Security) mode.
    # All SMTP commands that follow will be encrypted.
    # (Remember, we have used the port number of TLS. Hence, we are supposed to use this.)
    smtp.login("sparkler.star001@gmail.com", "YouC@n'tGuessR8")
    smtp.send_message(msg)
    print("Mail Sent")


# Please refer to the below given link for more understanding:-
'''https://www.knowledgehut.com/tutorials/python-tutorial/python-send-email'''


# Briefly executed in Advanced_Exercises -> Sending_Emails.py
