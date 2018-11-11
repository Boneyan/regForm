# coding=utf-8
# Данный файл описывает формы приложения

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, FileField, HiddenField
from wtforms.validators import Length, EqualTo, ValidationError, DataRequired, Optional, Email
from web.models import User
from web.helper import cur_user


# Проверка на существование пользователя с текущим логином
def exist(form, field):
    if User.get(login=field.data):
        raise ValidationError("Такой пользователь уже существует")


# Проверка на несуществование пользователя с текущим логином
def not_exist(form, field):
    if User.get(login=field.data) is None:
        raise ValidationError("Такого пользователя не существует")


# Проверка заполненности поля
def not_null(form, field):
    if not field.data:
        raise ValidationError("Заполните поле")


# Проверка на наличие некорректных символов в имени\логине пользователя
def check_correct_name(form, field):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_"
    for i in field.data:
        if i not in alpha:
            error = "В имени пользователя могут быть только цифры, латинские буквы и нижние подчёркивания"
            raise ValidationError(error)


# Проверка совпадения паролей
def match(form, field):
    user = None
    if cur_user():
        user = cur_user()
    elif form.login.data is not '':
        user = User.get(login=form.login.data)
    if user and not user.check_pass(field.data):
        raise ValidationError("Неправильный пароль")


# Форма регистрации
class RegForm(FlaskForm):
    login = StringField("Ваш логин", validators=[Length(5, message='Логин слишком короткий'),
                                                 exist, check_correct_name],
                        render_kw={"placeholder": "От 5 символов"})
    name = StringField("Ваш псевдоним", validators=[Length(5, message='Псевдоним слишком короткий'),
                                                    exist, check_correct_name],
                       render_kw={"placeholder": "От 5 символов"})
    password = PasswordField("Пароль", validators=[Length(8, message='Пароль слишком короткий')],
                             render_kw={"placeholder": "От 8 символов"})
    confirm = PasswordField("Повторите пароль", validators=[Length(8, message='Пароль слишком короткий'),
                                                            EqualTo("password", message="Пароли должны совпадать")])
    submit = SubmitField("Зарегистрироваться")


# Форма авторизации
class LogForm(FlaskForm):
    login = StringField("Логин", validators=[not_exist, not_null])
    password = PasswordField("Пароль", validators=[match])
    submit = SubmitField("Войти")
