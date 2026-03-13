from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'warning'


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Create tables if they don't exist
    with app.app_context():
        db.create_all()

    return app
