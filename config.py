import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'cheese cake'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MONEYMAN_MAIL_SUBJECT_PREFIX = '[MONEYMAN]'
    MONEYMAN_MAIL_SENDER = 'MONEYMAN admin <moneyman@example.com>'
    MONEYMAN_ADMIN = 'GEORGE PAMFILIS' # os.environ.get('MONEYMAN_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}
