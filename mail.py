import sys
from smtplib import SMTP
from email.mime.text import MIMEText


destination = []
serverSMTP = 'smtp.gmail.com'
serverPORT = '587'
sender = input('Enter your Gmail account: ')
password = input('Enter your Gmail password: ')
destination.append(input('Enter the recepients address: '))
subject = input('Enter the subject of email: ')

UNAME = sender
UPASS = password

text_subtype = 'plain'

# print('Enter your text message and press Ctrl-D to save it.')
content = input('Enter your text message and press Enter to send:\n')

try:
    msg = MIMEText(content, text_subtype)
    msg['Subject'] = subject
    msg['From'] = sender

    connection = SMTP(host=serverSMTP, port=serverPORT)
    connection.set_debuglevel(False)
    connection.ehlo()
    connection.starttls()
    connection.ehlo()
    connection.login(UNAME, UPASS)
    try:
        connection.sendmail(sender, destination, msg.as_string())
    finally:
        connection.quit()

except Exception as exc:
    sys.exit("mail failed; %s" % str(exc))
