# coding=utf-8
# Created by JTProg
# Date: 25/09/2018
# https://jtprog.ru/

__author__ = 'jtprog'
__version__ = '0.0.1'


import getpass


# Класс пользователя
class GMailUser:
    login = input('Enter your Gmail account: ')
    password = getpass.getpass()


# Класс сервера
class GMailServer:
    address = 'smtp.gmail.com'
    port = '587'

