import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    pass


class LiveConfig(Config):
    pass


config = {
    'dev': DevConfig,
    'test': TestConfig,
    'live': LiveConfig,
    'default': DevConfig
}
