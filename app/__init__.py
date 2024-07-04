from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'login'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    CORS(app)  # Enable CORS

    with app.app_context():
        from app import models
        db.create_all()

    # Register Blueprints
    from app.views import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
