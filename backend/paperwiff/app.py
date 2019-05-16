#   Flask packages
from flask import Flask, jsonify, request, redirect, current_app, flash, request, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename

#   JWT authentication
from flask_jwt_extended import JWTManager

#   Database initialization
from paperwiff.main import get_db

#   Import blueprints
from .main.routes.user import User
from .main.routes.story import Story
from .main.routes.auth import Auth


UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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


@app.route('/')
def index():
    response = current_app.make_response('/')
    response.set_cookie('csrf_token', value='your are an idiot')
    return response
