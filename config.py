#!/usr/bin/env python

from flask_babel import _
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """ App configuration """
    CLIENT_SECRET_JSON = os.path.join(basedir, 'client_secrets.json')
    LANGUAGES = ['en', 'es']
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' \
                              + os.path.join(basedir, 'catalog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
