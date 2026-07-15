from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate

#obj conn sqllite,tablecreation,perform crud operation
db = SQLAlchemy()
#Protect routes using @login_required
login_manager = LoginManager()
mail = Mail()
#Whenever we add or modify models, Flask-Migrate updates the database without deleting existing data.
migrate = Migrate()