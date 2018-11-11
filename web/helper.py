# coding=utf-8
# Файл со вспомогательными функциями

from flask import session
from web.models import User


# Функция для получения текущего пользователя
def cur_user():
    if 'Login' in session:
        return User.get(login=session['Login'])
    return None
