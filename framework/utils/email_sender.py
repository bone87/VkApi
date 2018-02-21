import smtplib
import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email_with_attach(message=None, attached_file=None, subject=None, recipien="87bone@gmail.com", ):
    msg = MIMEMultipart(message)
    if attached_file:
        part = MIMEApplication(open(str(attached_file), "rb").read())
        part.add_header('Content-Disposition', 'attachment', filename=str(attached_file))
        msg.attach(part)
    msg['From'] = 'useru009@gmail.com'
    msg['To'] = recipien
    msg['Subject'] = '{date} - {subject}'.format(date=datetime.datetime.now().strftime("%Y-%m-%d"), subject=subject)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login("useru009@gmail.com", "gmail4rever")
    server.sendmail(msg['From'], recipien, msg.as_string())
