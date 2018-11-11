# coding=utf-8
# Данный файл описывает модели приложения

import os
import hashlib
from web import db, app


# Класс описывающий модель пользователя
class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(32), nullable=False)

    def __init__(self, login, name):
        self.login = login
        self.name = name

    # Функция сохранения нового пользователя в базе данных
    def save(self, password):
        self.password = hashlib.sha512(password.encode("utf-8")).hexdigest()
        db.session.add(self)
        db.session.commit()

    # Функция проверки пароля к аккаунту
    def check_pass(self, password):
        hash = hashlib.sha512(password.encode("utf-8")).hexdigest()
        return self.password == hash

    # Функция получения пользователя
    @staticmethod
    def get(id=None, login=None):
        if login:
            return User.query.filter_by(login=login).first()
        if id:
            return User.query.get(id)
        return User.query.all()
