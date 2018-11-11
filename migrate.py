# coding=utf-8
# Файл миграции приложения

from web import db

db.reflect()
db.drop_all()
db.create_all()
db.session.commit()
