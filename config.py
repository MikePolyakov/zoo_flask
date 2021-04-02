import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'zoo-dbserver.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'admin1149'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Pass1149'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'storage1149z'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') \
                       or 'BPoTX4S8yu8JgGTQHNmd8aqr9Kc1l8CC6M9l2HS8BO3CmeLyIXH2wXq9fOAjPbsUKR+Fvdugrx6nwJMD9JTt3Q=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'