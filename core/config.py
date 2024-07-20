# core/config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))

def get_config():
    return {
        'DEBUG': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + os.path.join(basedir, '..', 'store.sqlite3'),
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        # Add other configurations as needed
    }