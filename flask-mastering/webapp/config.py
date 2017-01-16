class Config(object):
    SECRET_KEY = "4ad2d8b02bd732fcf2cb8f57af74af00%"


class ProConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/test?charset=utf8'
    SQLALCHEMY_ECHO = True
    MONGODB_SETTINGS = {
        'db': 'local',
        'host': 'localhost',
        'port': 27017
    }
    CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
    CELERY_BACKEND = 'amqp://guest:guest@localhost:5672//'
