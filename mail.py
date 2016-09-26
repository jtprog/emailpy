#!/usr/bin/env python3.5
import sys
from smtplib import SMTP
from email.mime.text import MIMEText


destination = []
serverSMTP = 'smtp.gmail.com'
serverPORT = '587'

# Вводим свой логин на Gmail
# Чтобы это сработало на вашем аккаунте Gmail
# необходимо разрешить небезопасный доступ в настройках аккаунта
sender = input('Enter your Gmail account: ')
# Вводим свой пароль от Gmail
password = input('Enter your Gmail password: ')

# Вводим адрес получателя
destination.append(input('Enter the recepients address: '))
# Вводим тему
subject = input('Enter the subject of email: ')

UNAME = sender
UPASS = password

text_subtype = 'plain'

# С новой строки вводится текст письма в одну сроку
content = input('Enter your text message and press Enter to send:\n')

try:
    msg = MIMEText(content, text_subtype)
    msg['Subject'] = subject
    msg['From'] = sender

	# Подключение к хосту Gmail
    connection = SMTP(host=serverSMTP, port=serverPORT)
    connection.set_debuglevel(False)
	# Приветствие TLS
	connection.ehlo()
    connection.starttls()
    connection.ehlo()
	# Логинимся
    connection.login(UNAME, UPASS)
    try:
		# Отправляем сообщение
        connection.sendmail(sender, destination, msg.as_string())
    finally:
		# Отключаемся от сервера
        connection.quit()

# Обработка исключений:
# Коды ошибок выдаются со ссылками на саппорт гугла
except Exception as exc:
    sys.exit("mail failed; %s" % str(exc))

sys.exit(0)
