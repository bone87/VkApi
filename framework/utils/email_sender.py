from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib

import datetime


def send_email_with_attach(subject, attached_file, recipien="87bone@gmail.com", ):
    msg = MIMEMultipart()
    msg['From'] = 'useru009@gmail.com'
    msg['To'] = recipien
    msg['Subject'] = '{date}_{subject}'.format(date=datetime.datetime.now().strftime("%Y-%m-%d"),
                                               subject=subject)
    msg.preamble = 'Multipart massage.\n'
    part = MIMEApplication(open(str(attached_file), "rb").read())
    part.add_header('Content-Disposition', 'attachment', filename=str(attached_file))
    msg.attach(part)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login("useru009@gmail.com", "gmail4rever")
    server.sendmail(msg['From'], recipien, msg.as_string())


def send_log():
    send_email_with_attach(
        attached_file='C:/!Git/VkApi/project/tests/reports/likes/log_{pref_data}_add_likes.html'.format(
            pref_data=datetime.datetime.now().strftime("%Y-%m-%d")),
        subject="add_likes")
