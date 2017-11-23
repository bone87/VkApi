from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib

import datetime


def send_email_with_attach(attached_file, recipien="87bone@gmail.com",):
    msg = MIMEMultipart()
    msg['From'] = 'useru009@gmail.com'
    msg['To'] = recipien
    msg['Subject'] = '{date}'.format(date=datetime.datetime.now().strftime("%Y-%m-%d"))
    msg.preamble = 'Multipart massage.\n'
    part = MIMEApplication(open(str(attached_file), "rb").read())
    part.add_header('Content-Disposition', 'attachment', filename=str(attached_file))
    msg.attach(part)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login("useru009@gmail.com", "gmail4rever")
    server.sendmail(msg['From'], recipien, msg.as_string())
