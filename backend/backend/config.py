
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///default.db')

    @staticmethod
    def init_app(app):
        pass
