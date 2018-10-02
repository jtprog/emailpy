# coding=utf-8
# Created by JTProg
# Date: 25/09/2018
# https://jtprog.ru/

__author__ = 'jtprog'
__version__ = '0.0.1'
__all__ = ['connectionToServer', 'GMailServer', 'GMailUser', 'user', 'server']


from base_class import GMailServer, GMailUser
from smtplib import SMTP


# Создаем объект класса Пользователя
user = GMailUser()
# Создаем объект класса Сервер
server = GMailServer()


def connectionToServer(uname, upass):
    # Подключение к хосту Gmail
    conn = SMTP(host=server.address, port=server.port)
    conn.set_debuglevel(False)
    # Приветствие TLS
    conn.ehlo()
    conn.starttls()
    conn.ehlo()
    # Логинимся
    conn.login(uname, upass)

    return conn
