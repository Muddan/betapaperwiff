#   Flask packages
from flask import Flask
from flask_cors import CORS

#   JWT authentication
from flask_jwt_extended import JWTManager

#   Database initialization
from paperwiff.main import get_db

#   Import blueprints
from .main.routes.user import User
from .main.routes.story import Story
from .main.routes.auth import Auth

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

CORS(app)

with app.app_context():
    # init the db
    get_db()
    app.register_blueprint(User, url_prefix="/api/user")
    app.register_blueprint(Story, url_prefix="/api/story")
    app.register_blueprint(Auth, url_prefix="/auth")
