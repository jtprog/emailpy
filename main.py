#!/usr/bin/env python3
# coding=utf-8

import sys
from base_util import *


# Вводим адрес получателя
destination = [input('Enter the recepients address: ')]

# Вводим тему
subject = input('Enter the subject of email: ')

UNAME = user.login
UPASS = user.password
# text_subtype = 'plain'


def main():

    # С новой строки вводится текст письма в одну сроку
    print("Enter message, end with ^D (Unix: Ctrl + D) or ^Z (Windows: Ctrl + Z):")

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

        # print("Message length is", len(msg))

        connection = connectionToServer(UNAME, UPASS)
        try:
            # Отправляем сообщение
            connection.sendmail(UNAME, destination, msg)
        finally:
            # Отключаемся от сервера
            connection.quit()

    # Обработка исключений:
    # Коды ошибок выдаются со ссылками на саппорт гугла
    except Exception as e:
        sys.exit("mail failed: %s" % str(e))

    sys.exit(0)


if __name__ == '__main__':
    main()
