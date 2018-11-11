# Файл начальной инициализации приложения

import os



CSRF_ENABLED = True

SECRET_KEY = '9)6odj22tkx_yxti%!$p*q!_k8eiw0z8bv2q)-y7zhg6*1^027'



basedir = os.path.abspath(os.path.dirname(__name__))

SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_DATABASE_URI = 'postgres://lylymyqhigjzss:1c3b489f259e7b2c54e499815645815a23677a054f009024fde9fd9eab608bc4@ec2-50-19-127-158.compute-1.amazonaws.com:5432/dc07g7o33t2kt4'
DATABASE_URI = 'postgres://lylymyqhigjzss:1c3b489f259e7b2c54e499815645815a23677a054f009024fde9fd9eab608bc4@ec2-50-19-127-158.compute-1.amazonaws.com:5432/dc07g7o33t2kt4'