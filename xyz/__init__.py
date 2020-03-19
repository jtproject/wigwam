from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from xyz.config import Config

# objects
_D = SQLAlchemy()
_E = Bcrypt()
_L = LoginManager()
_M = Mail()

def build(config_class=Config):
    _A = Flask(__name__)
    _A.config.from_object(Config)

    _D.init_app(_A)
    _E.init_app(_A)
    _L.init_app(_A)
    _M.init_app(_A)

    from xyz.main.routes import main
    _A.register_blueprint(main)
    from xyz.cal.routes import cal
    _A.register_blueprint(cal)

    return _A