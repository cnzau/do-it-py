from flask import Flask
from flask_bcrypt import Bcrypt, check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# Create the application object
app = Flask(__name__)

# Create a Bcrypt instance
bcrypt = Bcrypt(app)

# Create a LoginManager instance and configure for login
login_manager = LoginManager()
login_manager.init_app(app)

#  Development environment
app.config.from_object('config')
