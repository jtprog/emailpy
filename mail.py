#!/usr/bin/env python3.5
import sys
from smtplib import SMTP


# Класс пользователя
class MailUser:
    login = input('Enter your Gmail account: ')
    password = input('Enter your Gmail password: ')


# Класс сервера
class MailServer:
    address = 'smtp.gmail.com'
    port = '587'


# Создаем объект класса Пользователя
user = MailUser()
# Создаем объект класса Сервер
srv = MailServer()

destination = []
# serverSMTP = 'smtp.gmail.com'
# serverPORT = '587'

# Вводим свой логин на Gmail
# Чтобы это сработало на вашем аккаунте Gmail
# необходимо разрешить небезопасный доступ в настройках аккаунта
# sender = input('Enter your Gmail account: ')
# Вводим свой пароль от Gmail
# password = input('Enter your Gmail password: ')

# Вводим адрес получателя
destination.append(input('Enter the recepients address: '))
# Вводим тему
subject = input('Enter the subject of email: ')

UNAME = user.login
UPASS = user.password

text_subtype = 'plain'

# С новой строки вводится текст письма в одну сроку
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

try:
    msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n"
           % (UNAME, ", ".join(destination), subject))
    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            break
        msg = msg + line + "\n"

    print("Message length is", len(msg))

    # Подключение к хосту Gmail
    connection = SMTP(host=srv.address, port=srv.port)
    connection.set_debuglevel(False)
    # Приветствие TLS
    connection.ehlo()
    connection.starttls()
    connection.ehlo()
    # Логинимся
    connection.login(UNAME, UPASS)
    try:
        # Отправляем сообщение
        connection.sendmail(UNAME, destination, msg)
    finally:
        # Отключаемся от сервера
        connection.quit()

# Обработка исключений:
# Коды ошибок выдаются со ссылками на саппорт гугла
except Exception as exc:
    sys.exit("mail failed; %s" % str(exc))

sys.exit(0)
