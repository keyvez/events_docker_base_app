# config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
    SQLALCHEMY_DATABASE_URI = \
        'mysql+mysqldb://{0}:{1}@{2}/{3}'.format(
        os.environ.get("DB_ENV_MYSQL_USER"),
        os.environ.get("DB_ENV_MYSQL_PASSWORD"),
        "mysql-dev",
        os.environ.get("DB_ENV_MYSQL_DATABASE"))
    DEBUG_TB_ENABLED = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = \
        'mysql+mysqldb://{0}:{1}@{2}/{3}'.format(
        os.environ.get("DB_ENV_MYSQL_USER"),
        os.environ.get("DB_ENV_MYSQL_PASSWORD"),
        "mysql-dev",
        os.environ.get("DB_ENV_MYSQL_DATABASE"))
    DEBUG_TB_ENABLED = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = \
        'mysql+mysqldb://{0}:{1}@{2}/{3}'.format(
        os.environ.get("DB_ENV_MYSQL_USER"),
        os.environ.get("DB_ENV_MYSQL_PASSWORD"),
        "mysql-dev",
        os.environ.get("DB_ENV_MYSQL_DATABASE"))
    DEBUG_TB_ENABLED = False
