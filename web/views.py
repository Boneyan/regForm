# coding=utf-8
# Файл описывает поведение страниц сайта

from web import app
from flask import redirect, render_template, session, url_for
from web.forms import RegForm, LogForm
from web.models import User
from web.helper import cur_user


# Главная страница
@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html', user=cur_user())


# Страница регистрации
@app.route('/reg', methods=['GET', 'POST'])
def registration():
    form = RegForm()

    if form.validate_on_submit():
        user = User(form.login.data, form.name.data)
        user.save(form.password.data)
        session["Login"] = user.login
        return redirect(url_for("main"))

    return render_template('registration.html', form=form, user=cur_user())


# Страница входа
@app.route('/log', methods=['GET', 'POST'])
def login():
    form = LogForm()

    if form.validate_on_submit():
        session["Login"] = form.login.data
        return redirect(url_for("main"))

    return render_template('log.html', form=form, user=cur_user())


# Выход из аккаунта
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'Login' in session:
        session.pop('Login')
    return redirect('/')


# Личный кабинет
@app.route('/user', methods=['GET', 'POST'])
def profile():
    user = cur_user()
    if user:
        return render_template('user.html', user=user)
    else:
        return redirect(url_for("login"))
