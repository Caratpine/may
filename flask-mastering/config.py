class Config(object):
    pass


class ProConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/tofu?charset=utf8'
    SQLALCHEMY_ECHO = True
