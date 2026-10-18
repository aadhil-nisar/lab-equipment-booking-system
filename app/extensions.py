
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = "auth.login"

csrf = CSRFProtect()


@login_manager.user_loader
def load_user(user_id):
    from .models.user import User

    try:
        return db.session.get(User, int(user_id))
    except (ValueError, TypeError):
        return None
