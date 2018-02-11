import smtplib
import datetime
from email.mime.text import MIMEText


def send_email_with_attach(error_message=None, subject=None, recipien="87bone@gmail.com",):
    msg = MIMEText(error_message)
    msg['From'] = 'useru009@gmail.com'
    msg['To'] = recipien
    msg['Subject'] = '{date} - {subject}'.format(date=datetime.datetime.now().strftime("%Y-%m-%d"), subject=subject)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login("useru009@gmail.com", "gmail4rever")
    server.sendmail(msg['From'], recipien, msg.as_string())
