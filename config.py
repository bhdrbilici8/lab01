import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'change-this-in-production'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'

    # Azure SQL Database connection via SQLAlchemy + pyodbc
    DATABASE_URL = os.environ.get('DATABASE_URL', '').strip()
    DB_SERVER    = os.environ.get('DB_SERVER', '').strip()
    DB_NAME      = os.environ.get('DB_NAME', '').strip()
    DB_USERNAME  = os.environ.get('DB_USERNAME', '').strip()
    DB_PASSWORD  = os.environ.get('DB_PASSWORD', '').strip()

    if DATABASE_URL:
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
    elif DB_SERVER and DB_NAME and DB_USERNAME and DB_PASSWORD:
        SQLALCHEMY_DATABASE_URI = (
            f"mssql+pyodbc://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
            f"?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes&TrustServerCertificate=no"
        )
    else:
        # Local SQLite fallback — used automatically when no Azure config is provided
        SQLALCHEMY_DATABASE_URI = 'sqlite:///bookreview.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
