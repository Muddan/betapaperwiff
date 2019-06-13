#   Flask packages
from flask import Flask, jsonify, request, redirect, current_app, flash, request, redirect, url_for
from flask_cors import CORS

#   JWT authentication
from flask_jwt_extended import JWTManager

#   Database initialization
from .main.services.database import Datebase

#   Import blueprints
from .main.routes.user import User
from .main.routes.story import Story
from .main.routes.auth import Auth

# Firebase initialization
import firebase_admin
from firebase_admin import credentials, auth
from .main.firebase.firebaseCredentials import firebaseCredentials

# Firebase Admin SDK Initialization
# DEV CREDS
# cred = firebaseCredentials().serviceAccountKeyDev()
#PROD
cred = firebaseCredentials().serviceAccountKey()
credObj = credentials.Certificate(cred)
firebase_admin.initialize_app(credObj)

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change this!
jwt = JWTManager(app)

CORS(app)

with app.app_context():
    # init the db
    Datebase().get_db()
    app.register_blueprint(User, url_prefix="/api/user")
    app.register_blueprint(Story, url_prefix="/api/story")
    app.register_blueprint(Auth, url_prefix="/api/auth")
